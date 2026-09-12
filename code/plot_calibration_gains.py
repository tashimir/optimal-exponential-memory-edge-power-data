"""Render measured gains and losses for the prespecified calibration experiment."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator,NullLocator
import numpy as np
import pandas as pd

COLORS=['#0072B2','#B87500','#009E73','#AA4499','#56A5CE','#D55E00','#222222']
MARKERS=['o','s','^','D','v','P','X']


def validate(data):
    assert len(data)==259 and data[['N','family','case']].duplicated().sum()==0
    assert (data['trajectories']==32768).all()
    assert np.isfinite(data.select_dtypes('number').to_numpy()).all()
    assert (data.saving_lower95_pct<=data.saving_estimate_pct).all()
    assert (data.saving_upper95_pct>=data.saving_estimate_pct).all()
    assert data.query("family == 'scaled_r'").groupby('N').size().eq(31).all()
    assert data.query("family == 'fixed_alpha'").groupby('alpha').size().eq(7).all()


def configure():
    mpl.rcParams.update({'text.usetex':True,'text.latex.preamble':r'\usepackage{lmodern}',
        'font.family':'serif','font.serif':['Latin Modern Roman'],'mathtext.fontset':'cm',
        'font.size':9,'axes.labelsize':9,'axes.titlesize':9,'legend.fontsize':8,
        'xtick.labelsize':8,'ytick.labelsize':8,'axes.linewidth':.65,
        'lines.linewidth':1.1,'pdf.fonttype':42,'ps.fonttype':42})


def curve(axis,x,group,index,label):
    y=group.saving_estimate_pct.to_numpy()
    lo=group.saving_lower95_pct.to_numpy()
    hi=group.saving_upper95_pct.to_numpy()
    axis.fill_between(x,lo,hi,color=COLORS[index],alpha=.15,linewidth=0,zorder=2)
    axis.plot(x,y,color=COLORS[index],marker=MARKERS[index],markersize=2.7,
        markeredgewidth=.45,markerfacecolor='white',label=label,zorder=3)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    data=pd.read_csv(args.data)
    validate(data); configure()
    fig,axes=plt.subplots(1,2,figsize=(6.06,3.55),sharey=True)
    fig.subplots_adjust(left=.145,right=.965,bottom=.29,top=.90,wspace=.14)
    ticks=[-.1,-.001,0,.001,.1,10]
    labels=[r'$-0.1$',r'$-0.001$',r'$0$',r'$0.001$',r'$0.1$',r'$10$']
    for ax in axes:
        ax.set_yscale('symlog',linthresh=.0001,linscale=.5,base=10)
        ax.set_ylim(-.28,45)
        ax.yaxis.set_major_locator(FixedLocator(ticks))
        ax.set_yticklabels(labels)
        ax.yaxis.set_minor_locator(NullLocator())
        ax.set_axisbelow(True)
        ax.grid(axis='y',color='#d6d6d6',linewidth=.4)
        ax.axhline(0,color='#444444',linewidth=.65,zorder=1)
        ax.tick_params(direction='out',length=2.5)
        ax.spines[['top','right']].set_visible(False)
    for index,(N,group) in enumerate(data[data.family=='scaled_r'].groupby('N',sort=True)):
        group=group.sort_values('r')
        curve(axes[0],group.r.to_numpy(),group,index,r'$2^{'+str(int(np.log2(N)))+'}$')
    axes[0].axvline(1,color='#777777',linewidth=.65,linestyle=':',zorder=1)
    axes[0].set_xlim(-.045,3.045)
    axes[0].set_xticks([0,.5,1,1.5,2,2.5,3])
    axes[0].set_xlabel(r'$r=(\alpha-1)\log N/\lambda^\star(2)$')
    axes[0].set_ylabel(r'Saving versus stationary scale (\%)',labelpad=5)
    axes[0].set_title(r'(a) Joint-window paths',loc='left',pad=9)
    axes[0].legend(title=r'$N$',ncol=4,loc='upper left',bbox_to_anchor=(.135,.16),
        bbox_transform=fig.transFigure,
        borderaxespad=0,frameon=False,handlelength=1.2,handletextpad=.3,columnspacing=.65,
        title_fontsize=8,labelspacing=.25)
    for index,(alpha,group) in enumerate(data[data.family=='fixed_alpha'].groupby('alpha',sort=True)):
        group=group.sort_values('N')
        curve(axes[1],np.log2(group.N.to_numpy()),group,index,r'$'+f'{alpha:g}'+'$')
    axes[1].set_xlim(7.8,20.2)
    axes[1].set_xticks([8,12,16,20],labels=[r'$2^8$',r'$2^{12}$',r'$2^{16}$',r'$2^{20}$'])
    axes[1].set_xlabel(r'Horizon $N$')
    axes[1].set_title(r'(b) Fixed-power sensitivity',loc='left',pad=9)
    axes[1].legend(title=r'$\alpha$',ncol=3,loc='upper left',bbox_to_anchor=(.565,.16),
        bbox_transform=fig.transFigure,
        borderaxespad=0,frameon=False,handlelength=1.2,handletextpad=.3,columnspacing=.65,
        title_fontsize=8,labelspacing=.25)
    fig.savefig(args.output/'measured_calibration_gains.pdf',metadata={
        'Title':'Measured calibration gains for exponential memory',
        'Author':'Pedro M. M. de Castro','Subject':'Paired trajectory simulations in the unit disk'})
    fig.savefig(args.output/'measured_calibration_gains.png',dpi=220)
    plt.close(fig)
    print('Rendered measured_calibration_gains from all 259 prespecified scenarios.')


if __name__=='__main__':
    main()
