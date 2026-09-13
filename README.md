# Data and figures for finite-horizon exponential-memory optimization

Scientific data, figures and reproducible checks for Pedro M. M. de Castro, *Finite-horizon phase transitions in optimal exponential memory for Euclidean connections*. An earlier version of the present study is [arXiv:2608.27777v2](https://arxiv.org/abs/2608.27777v2).

Version `v1.2.2` provides the figures, data and programs accompanying the finite-horizon study. Scientific names identify the figures and their datasets.

[Online Resource 1](OnlineResource1.zip) is the supplementary package supplied with the article. Its [data dictionary](FINITE_HORIZON_DATA_DICTIONARY.md) explains every included file, parameter and reported statistic.

## Figures

| Scientific figure | PDF | Data |
|---|---|---|
| Geometric construction | [geometric_construction.pdf](figures/geometric_construction.pdf) | [geometric_construction](data/geometric_construction) |
| Joint-window phase diagram | [joint_window_phase_diagram.pdf](figures/joint_window_phase_diagram.pdf) | Analytical diagram derived from the article's results |
| Finite-horizon phase transitions | [finite_horizon_phase_transitions.pdf](figures/finite_horizon_phase_transitions.pdf) | [finite_horizon_phase_transitions](data/finite_horizon_phase_transitions) |
| Local objective geometry | [local_objective_geometry.pdf](figures/local_objective_geometry.pdf) | [local_objective_geometry](data/local_objective_geometry) |
| Measured calibration gains | [measured_calibration_gains.pdf](figures/measured_calibration_gains.pdf) | [measured_calibration_gains](data/measured_calibration_gains) |

[FIGURE_CATALOG.csv](FIGURE_CATALOG.csv) provides the same map in machine-readable form. The five figures are supplied as vector PDFs with their magnified details. Render the numerical figures from the supplied arrays:

```sh
python -m pip install -r requirements.txt
python code/render_figures.py --output reproduced_figures
```

Rendering requires LaTeX with Latin Modern fonts and the normal Matplotlib LaTeX dependencies. The two analytical illustrations are supplied as vector PDFs; the rendering command regenerates all three numerical figures.

## Measured calibration gains

[The expanded experiment](data/measured_calibration_gains) compares the finite-horizon scalar rule with the analytical stationary scale for independent uniform points in the unit disk and initial site x_0=p_0. It covers seven horizons from 256 to 1,048,576, 31 scaled powers r from 0 to 3, and six fixed powers from 1.01 to 1.20. The 259 scenarios use 32,768 independent trajectories per horizon. The same inputs evaluate all 74 policies at that horizon, so the scenario estimates within a horizon are dependent. Input sequences are independent across horizons.

- [Results and pointwise 95% intervals](data/measured_calibration_gains/expanded_calibration_results.csv)
- [Paired block moments](data/measured_calibration_gains/expanded_calibration_block_moments.csv)
- [Design, random generator and seed mapping](data/measured_calibration_gains/expanded_calibration_design.json)
- [Fixed policy parameters](data/measured_calibration_gains/scenarios.csv)
- [Observed zero-gain brackets](data/measured_calibration_gains/observed_zero_crossing_brackets.json)

Reconstruct every reported estimate and interval directly from the supplied moments:

```sh
python code/calibration_statistics.py --output reproduced_intervals.csv
python code/plot_calibration_gains.py --data data/measured_calibration_gains/expanded_calibration_results.csv --output reproduced_figures
```

Savings are 100 times one minus the ratio of mean costs. Positive values favor the finite rule. The stationary baseline is an analytical asymptotic scale. Pointwise paired normal delta-method intervals describe sampling uncertainty. In (a), the figure shows the 189 joint-window cases with r <= 2, with a circular magnification of the segment intersections near r = 0.5. The 28 cases with r > 2 remain in the data. In (b), the same linear saving scale shows all 42 fixed-power cases. In (c), all 91 negative estimates appear as positive percentage cost increases on a logarithmic axis, including those with r > 2. Circles identify joint-window cases and triangles fixed-power cases. The highlighted curve joins the largest observed increase among the 37 scenarios at each horizon. Shading in (a) and (b) and bars in (c) represent the same pointwise intervals. The smallest and largest horizons are highlighted in (a), and powers 1.01 and 1.03 are highlighted in (b). The observed gain-zero brackets describe the sampled grid. Fixed-power scenarios provide finite-sample sensitivity evidence.

The supplied moments are sufficient to reconstruct all reported means, variances and intervals. Complete trajectory-cost arrays are retained by the author. A full regeneration uses the supplied C++17 kernel and a GNU/Linux OpenMP compiler:

```sh
python code/reproduce_expanded_calibration.py --output reproduced_trajectories --threads 8
```

The full experiment is computationally intensive. A small check of the first 128 trajectories at N=256 uses:

```sh
python code/reproduce_expanded_calibration.py --output small_check --horizons 256 --trajectories 128 --threads 4
```

This checks only that subset. Completed blocks can be reused after their parameters and checksums are verified. The documented random streams do not depend on the number of threads or block boundaries. Exact bitwise agreement can depend on the compiler and mathematical library. The published parameters are included verbatim; regenerate them independently with:

```sh
python code/prepare_calibration_parameters.py --benchmarks code --root regenerated_parameters
```

[A separate twelve-scenario experiment](data/calibration_experiment) additionally compares the rule with an archived numerical finite-horizon parameter. Its complete trajectory costs, reference parameters and program are preserved. Its reference comparisons apply to those twelve scenarios. Run it with `python code/calibration_experiment.py --output reproduced_reference_comparison`.

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

[CITATION.cff](CITATION.cff) supplies metadata. Cite the associated study and version `v1.2.2`; record the repository commit for an immutable identifier.

Copyright 2026 Pedro M. M. de Castro. See [COPYRIGHT.md](COPYRIGHT.md). No open license is granted by this repository.
