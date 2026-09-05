# Numerical data for optimal exponential memory

Numerical data for Pedro M. M. de Castro, *Optimal exponential memory for sequential Euclidean connections: edge-power costs and phase transitions* (2026), [arXiv:2608.27777v2](https://arxiv.org/abs/2608.27777v2).

## Figures and tables

The following map identifies the data by scientific topic and by figure or table in the article. Dataset paths are stable identifiers.

| Article object | Scientific topic | Data location |
|---|---|---|
| Figure 1 | Geometric construction | `data/figure1_geometry` |
| Figure 2 | Analytical joint-window diagram | No numerical dataset |
| Figure 3 | Uniform and adversarial relative loss | `data/figure2_tradeoff` |
| Figure 4 | Endpoint bifurcation | `data/figure3_endpoint_bifurcation` |
| Figure 5 | High-power adversarial bounds | `data/figure4_high_power` |
| Figure 6 | Finite-size phase transitions | `data/figure6_finite_size` |
| Figure 7 | Differentiated local objective | `data/figure7_local_objective` |
| Figure 8 | High-dimensional first correction | `data/figure8_high_dimension` |
| Table 1 | Robust policy comparison | `data/tables/t2_robustness_cost.csv` |
| Table 2 | Finite-size constants | `data/tables/t1_dimension_constants.csv` and `t1_sublinear_constants.csv` |

Additional files in `data/tables` and `data/validation` contain quadrature comparisons, interpolation tests, parameter records and independent Monte Carlo diagnostics. These numerical checks describe the precision and scope of the scientific calculations.

## Interpretation and independent use

`DATA_DICTIONARY.md` defines the stored columns, parameter conventions and plotted transformations. `FILE_MANIFEST.csv` records the byte size, SHA-256 digest, format, row count and columns of all 50 data files. `SHA256SUMS.txt` checks file integrity across the repository.

CSV files use a header row and comma delimiters. JSON files are UTF-8 encoded. Column names are case-sensitive: `delta_N` and `Delta_N` denote different analytical scales. Empty fields denote quantities that do not apply to the record. Relative losses are stored as fractions; multiply by 100 to obtain the percentages displayed in the article.

The dataset contains evaluated scientific quantities and numerical validation metadata. Exact second- and fourth-moment figures can be reconstructed directly from the article's formulas. Finite-size and nonquadratic stationary evaluations also require an implementation of the numerical method. The author's custom software is available from the author on reasonable request. Independent Monte Carlo checks include sample sizes and stream-level estimates; pseudorandom initialization values are not included.

## Citation

`CITATION.cff` supplies citation metadata. Cite the associated article and data version `v1.0.1-data`. Record the corresponding repository commit when an analysis requires an immutable data identifier.

## Rights

Copyright 2026 Pedro M. M. de Castro. See `COPYRIGHT.md`. No open license is granted by this repository.
