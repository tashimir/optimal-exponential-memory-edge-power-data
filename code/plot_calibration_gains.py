"""Render measured cost savings and magnified losses from the calibration data."""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator

NAVY = '#005A8D'
BLUE = '#54A4BF'
ORANGE = '#B45113'
GRAY = '#999999'


def configure():
    mpl.rcParams.update({'text.usetex': True,
        'text.latex.preamble': r'\usepackage{lmodern}',
        'font.family': 'serif', 'font.serif': ['Latin Modern Roman'],
        'mathtext.fontset': 'cm', 'font.size': 9, 'axes.labelsize': 9,
        'axes.titlesize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
        'axes.linewidth': .6, 'lines.linewidth': 1.05,
        'pdf.fonttype': 42, 'ps.fonttype': 42})


def style(ax, loss=False):
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(direction='out', length=2.5, pad=2)
    ax.set_axisbelow(True)
    ax.grid(axis='y', color='#dfdfdf', linewidth=.45)
    if not loss:
        ax.set_ylim(-1.0, 29.7)
        ax.set_yticks([0, 10, 20])
        ax.axhline(0, color='#444444', linewidth=.65)
        ax.set_ylabel(r'Cost saving (\%)', labelpad=3)


def draw_curve(ax, x, g, color, ls='-', marker='o', z=3, lw=1.0):
    y = g.saving_estimate_pct.to_numpy()
    lo, hi = g.saving_lower95_pct.to_numpy(), g.saving_upper95_pct.to_numpy()
    ax.fill_between(x, lo, hi, color=color, alpha=.17, linewidth=0, zorder=z)
    ax.plot(x, y, color=color, ls=ls, marker=marker, markersize=2.2,
            markeredgewidth=.45, markerfacecolor='white', linewidth=lw, zorder=z+1)


def scaled_panel(ax, data):
    style(ax)
    group = data[data.family == 'scaled_r']
    horizons = sorted(group.N.unique())
    for N in horizons[1:-1]:
        g = group[group.N == N].sort_values('r')
        draw_curve(ax, g.r.to_numpy(), g, '#ababab', marker='.', z=2, lw=.65)
    for N, color, ls in [(horizons[0], BLUE, '--'), (horizons[-1], NAVY, '-')]:
        g = group[group.N == N].sort_values('r')
        draw_curve(ax, g.r.to_numpy(), g, color, ls=ls, z=4)
    ax.set_xlim(-.035, 3.06)
    ax.set_xticks([0, .5, 1, 1.5, 2, 2.5, 3])
    ax.set_xlabel(r'Scaled power $r=(\alpha-1)\log N/\lambda^\star(2)$', labelpad=3)
    ax.axvline(1, color='#777777', linewidth=.7, linestyle=':', zorder=1)
    ax.text(1.035, 2.8, r'$r=1$: theoretical scale change', color='#555555', fontsize=8)
    ax.set_title(r'(a) Savings across the joint window', loc='left', pad=5)
    mid = group[np.isclose(group.r, .5)].saving_estimate_pct
    message = rf'${mid.min():.1f}$--${mid.max():.1f}\%$ saved'
    ax.annotate(message+'\n'+r'at $r=0.5$, across all horizons',
        xy=(.5,mid.max()), xytext=(1.48,17.8), color=NAVY, fontsize=8.5,
        ha='left', va='center', linespacing=1.1,
        arrowprops=dict(arrowstyle='-', color=NAVY, lw=.65,
                        connectionstyle='angle,angleA=180,angleB=50,rad=2'))
    for y,color,ls,label in [(28.0,NAVY,'-',r'$N=2^{20}$'),
                              (24.6,BLUE,'--',r'$N=2^8$'),
                              (21.2,'#aaa','-',r'Five intermediate horizons')]:
        ax.plot([2.05,2.22],[y,y],color=color,ls=ls,lw=1)
        ax.text(2.27,y,label,fontsize=8,va='center')


def fixed_panel(ax, data):
    style(ax)
    fixed=data[data.family=='fixed_alpha']
    for alpha,g in fixed.groupby('alpha',sort=True):
        g=g.sort_values('N')
        color=NAVY if alpha==1.01 else BLUE if alpha==1.03 else GRAY
        draw_curve(ax,np.log2(g.N.to_numpy()),g,color,
                   ls='-' if alpha<=1.03 else '--',
                   marker='o' if alpha<=1.03 else '.',z=3 if alpha<=1.03 else 2,
                   lw=1.1 if alpha<=1.03 else .7)
    ax.set_xlim(7.8,20.25)
    ax.set_xticks([8,12,16,20],labels=[r'$2^8$',r'$2^{12}$',r'$2^{16}$',r'$2^{20}$'])
    ax.set_xlabel(r'Horizon $N$ (logarithmic spacing)',labelpad=3)
    ax.set_title(r'(b) Savings at fixed powers',loc='left',pad=5)
    ax.text(14,28.1,r'$\alpha=1.01$',color=NAVY,fontsize=8.5,ha='center')
    ax.text(10.9,16.4,r'$\alpha=1.03$',color=BLUE,fontsize=8.5)
    endpoint = fixed[np.isclose(fixed.alpha,1.03)].sort_values('N').iloc[-1]
    ax.annotate(rf'${endpoint.saving_estimate_pct:.4f}\%$',
                xy=(np.log2(endpoint.N),endpoint.saving_estimate_pct),xytext=(18.9,7.5),
                fontsize=8.5,color=BLUE,ha='center',
                arrowprops=dict(arrowstyle='-',color=BLUE,lw=.65))
    ax.text(8.2,5.5,r'Other four powers',color='#666666',fontsize=8)


def loss_panel(ax, data):
    style(ax,True)
    losses=data[data.saving_estimate_pct<0].copy()
    losses['increase']=-losses.saving_estimate_pct
    for family,marker in [('scaled_r','o'),('fixed_alpha','^')]:
        g=losses[losses.family==family]
        x=np.log2(g.N.to_numpy())
        y=g.increase.to_numpy()
        ax.errorbar(x,y,yerr=np.array([y+g.saving_upper95_pct.to_numpy(),
            -g.saving_lower95_pct.to_numpy()-y]),fmt=marker,color='#929292',
            markersize=2.2,markeredgewidth=.3,markerfacecolor='white',
            elinewidth=.4,capsize=0,zorder=2)
    maxima=losses.loc[losses.groupby('N').increase.idxmax()].sort_values('N')
    ax.plot(np.log2(maxima.N.to_numpy()),maxima.increase.to_numpy(),color=ORANGE,
        lw=1,zorder=4)
    for family,marker in [('scaled_r','o'),('fixed_alpha','^')]:
        g=maxima[maxima.family==family]
        ax.plot(np.log2(g.N.to_numpy()),g.increase.to_numpy(),ls='',color=ORANGE,
            marker=marker,markersize=3.5,markerfacecolor='white',markeredgewidth=.8,zorder=5)
    ax.set_yscale('log')
    ax.set_ylim(1e-6,.80)
    ax.set_xlim(7.6,20.5)
    ax.set_xticks([8,14,20],labels=[r'$2^8$',r'$2^{14}$',r'$2^{20}$'])
    ax.set_yticks([1e-5,.001,.1],labels=[r'$0.00001$',r'$0.001$',r'$0.1$'])
    ax.yaxis.set_minor_locator(NullLocator())
    ax.set_xlabel(r'Horizon $N$',labelpad=3)
    ax.set_ylabel(r'Cost increase (\%)',labelpad=2)
    ax.set_title(r'(c) Magnified view of losses',loc='left',pad=5)
    ax.text(20,.37,r'Log scale',fontsize=7.5,color='#555555',ha='right')
    ax.text(14.3,.019,r'Largest observed'+'\n'+r'increase',fontsize=8,
            color=ORANGE,va='center',linespacing=1.1)
    ax.text(8.5,.00017,r'All $91$ cases'+'\n'+r'with losses',fontsize=8,
            color='#666666',va='center',linespacing=1.1)
    ax.annotate(rf'${maxima.increase.iloc[0]:.4f}\%$',xy=(8,maxima.increase.iloc[0]),xytext=(9.0,.36),
        color=ORANGE,fontsize=8.5,ha='left',
        arrowprops=dict(arrowstyle='-',color=ORANGE,lw=.6))
    ax.annotate(rf'${maxima.increase.iloc[-1]:.7f}\%$',xy=(20,maxima.increase.iloc[-1]),xytext=(13.6,4.2e-6),
        color=ORANGE,fontsize=8.5,ha='center',
        arrowprops=dict(arrowstyle='-',color=ORANGE,lw=.6))


def validate(data):
    assert len(data)==259 and not data[['N','family','case']].duplicated().any()
    assert data.trajectories.eq(32768).all()
    assert np.isfinite(data.select_dtypes('number').to_numpy()).all()
    assert (data.saving_lower95_pct<=data.saving_estimate_pct).all()
    assert (data.saving_upper95_pct>=data.saving_estimate_pct).all()
    assert data.query("family == 'scaled_r'").groupby('N').size().eq(31).all()
    assert data.query("family == 'fixed_alpha'").groupby('alpha').size().eq(7).all()
    assert sorted(data.N.unique())==[2**k for k in range(8,21,2)]
    negative=data[data.saving_estimate_pct<0]
    assert len(negative)==91 and (negative.saving_upper95_pct<0).all()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    data=pd.read_csv(args.data)
    validate(data);configure()
    args.output.mkdir(parents=True,exist_ok=True)
    fig=plt.figure(figsize=(6.06,4.08))
    a=fig.add_axes([.085,.585,.895,.345])
    b=fig.add_axes([.085,.105,.435,.335])
    c=fig.add_axes([.665,.105,.315,.335])
    scaled_panel(a,data)
    fixed_panel(b,data)
    loss_panel(c,data)
    fig.savefig(args.output/'measured_calibration_gains.pdf',metadata={
        'Title':'Cost savings and losses from finite-horizon calibration',
        'Author':'Pedro M. M. de Castro',
        'Subject':'Paired trajectory simulations in the unit disk',
        'CreationDate':None,'ModDate':None})
    fig.savefig(args.output/'measured_calibration_gains.png',dpi=220)
    plt.close(fig)
    print('Rendered 217 joint-window cases, 42 fixed-power cases and all 91 losses.')


if __name__=='__main__':
    main()
