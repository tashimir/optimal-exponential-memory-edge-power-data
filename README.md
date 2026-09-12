# Data and figures for finite-horizon exponential-memory optimization

Scientific data, figures and reproducible checks for Pedro M. M. de Castro, *Finite-horizon phase transitions in optimal exponential memory for Euclidean connections*. The underlying study is also available in a broader [preprint](https://arxiv.org/abs/2608.27777v2).

Version `v1.1.0` uses descriptive scientific identifiers. Figure numbering can change between article versions without changing these names.

## Figures

| Scientific figure | PDF | Data |
|---|---|---|
| Geometric construction | [geometric_construction.pdf](figures/geometric_construction.pdf) | [geometric_construction](data/geometric_construction) |
| Joint-window phase diagram | [joint_window_phase_diagram.pdf](figures/joint_window_phase_diagram.pdf) | Analytical diagram derived from the article's results |
| Finite-horizon phase transitions | [finite_horizon_phase_transitions.pdf](figures/finite_horizon_phase_transitions.pdf) | [finite_horizon_phase_transitions](data/finite_horizon_phase_transitions) |
| Local objective geometry | [local_objective_geometry.pdf](figures/local_objective_geometry.pdf) | [local_objective_geometry](data/local_objective_geometry) |

[FIGURE_CATALOG.csv](FIGURE_CATALOG.csv) provides the same map in machine-readable form. The four PDF figures retain their full panels and insets. Render the numerical figures from the supplied arrays:

```sh
python -m pip install -r requirements.txt
python code/render_figures.py --output reproduced_figures
```

Rendering requires LaTeX with Latin Modern fonts and the normal Matplotlib LaTeX dependencies. The two analytical illustrations are supplied as vector PDFs; the rendering command regenerates the two numerical multipanel figures.

## Measured calibration gains

[The paired experiment](data/calibration_experiment) compares the convex finite-horizon rule, the analytical stationary scale and an archived numerical reference. It uses independent uniform points in the unit disk, the initial site x_0=p_0, horizons 256, 1024 and 4096, and scaled powers r=0, 0.5, 1 and 2. All twelve scenarios are reported, including negative savings above the threshold. Each scenario has 32,768 independent complete trajectories; policies within a horizon share their inputs.

- [Results and pointwise 95% intervals](data/calibration_experiment/calibration_results.csv)
- [Experimental design and seed](data/calibration_experiment/calibration_experiment_design.json)
- [Complete trajectory costs](data/calibration_experiment/calibration_trajectory_costs.npz)
- [Experiment program](code/calibration_experiment.py)

Run the experiment with:

```sh
python code/calibration_experiment.py --output reproduced_experiment
```

Savings are ratios of mean costs, with paired uncertainty estimates. The stationary baseline is an analytical asymptotic scale. The archived reference is a numerical parameter evaluated again on the same simulated inputs. Neither comparison certifies global finite-horizon optimality. The reference is unavailable at horizon 256. The experiment measures costs within the stated stochastic model.

## Analytical checks and related datasets

[Analytical benchmarks](data/analytical_benchmarks) cover geometric constants, the exact one-dimensional finite objective, the scalar balance and a separate three-case Monte Carlo cost check. Their programs are `code/analytical_benchmarks.py` and `code/finite_cost_monte_carlo.py`.

Additional datasets from the broader study are organized by topic:

- [Uniform and adversarial tradeoff](data/uniform_adversarial_tradeoff)
- [Endpoint bifurcation](data/endpoint_bifurcation)
- [High-power adversarial bounds](data/high_power_adversarial_bounds)
- [High-dimensional correction](data/high_dimensional_correction)
- [Dimension constants and policy comparisons](data/tables)
- [Numerical resolution and sampling diagnostics](data/validation)

The multidimensional radial-Poisson solver that produced the original finite-size arrays is available from the author on reasonable request. The distributed rendering code uses those arrays; the paired Monte Carlo experiment is independently executable.

## Interpretation, integrity and citation

[DATA_DICTIONARY.md](DATA_DICTIONARY.md) defines units, parameters and columns. [FILE_MANIFEST.csv](FILE_MANIFEST.csv) records dataset paths, formats, dimensions and checksums. [SHA256SUMS.txt](SHA256SUMS.txt) covers repository files. CSV files have headers and comma delimiters; JSON is UTF-8; NPZ arrays use NumPy's format. `delta_N` and `Delta_N` identify different analytical scales. Empty reference fields mean unavailable quantities.

The fifty original datasets are unchanged in content. [LEGACY_PATH_MAP.csv](LEGACY_PATH_MAP.csv) maps paths in `v1.0.1-data` to descriptive paths in this version. The earlier tag remains available for exact reproduction of citations to that release.

[CITATION.cff](CITATION.cff) supplies metadata. Cite the associated study and version `v1.1.0`; record the repository commit for an immutable identifier.

Copyright 2026 Pedro M. M. de Castro. See [COPYRIGHT.md](COPYRIGHT.md). No open license is granted by this repository.
