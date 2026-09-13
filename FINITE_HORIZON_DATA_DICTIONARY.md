# Data dictionary

Supplement to **Finite-horizon phase transitions in optimal exponential memory for Euclidean connections**, by Pedro M. M. de Castro, submitted to *Mathematical Methods of Operations Research*.

Centro de Informática, Universidade Federal de Pernambuco, Recife, Brazil. Correspondence: [pmmc@cin.ufpe.br](mailto:pmmc@cin.ufpe.br).

This dictionary describes the files included in Online Resource 1. The [README](README.md) explains how to reproduce the numerical results. Data and rendering programs for the other named figures are available in [repository version v1.2.2](https://github.com/tashimir/optimal-exponential-memory-edge-power-data/tree/v1.2.2).

## Model and units

The input ball has radius one. The memory parameter is gamma and the update fraction is delta = 1 - gamma. Each trajectory has N insertions and starts at x_0 = p_0. The retained-edge factor is h_alpha(gamma) = gamma^alpha + (1-gamma)^alpha. A trajectory cost includes both retained edges at every insertion.

The dimension is d, the power is alpha, epsilon = alpha - 1, and log denotes the natural logarithm. The initialization constant H, stationary scale delta_N, critical scale Delta_N and threshold lambda_star have the definitions in the manuscript. The scaled power is r = (alpha-1) log(N)/lambda_star(d).

The stationary-scale prescription uses delta_N = q_(d,alpha)^(1/(alpha-1)) above power one and delta_N = 0 at power one. This is an analytical scale; exact stationary optimality is not assumed. The finite rule solves the strictly convex scalar balance in the manuscript. The separate numerical reference uses an archived finite-horizon parameter.

Means and variances refer to complete-trajectory costs. Percentage savings, their standard errors and confidence limits are measured in percentage points. A positive saving means that the finite rule costs less than the stationary-scale prescription. Negative estimates are retained. All confidence intervals described here are pointwise normal delta-method intervals.

## File inventory

| Location | Contents |
|---|---|
| `data/analytical_benchmarks/dimension_constants.csv` | Eight dimensions and their initialization constants and critical prefactors. |
| `data/analytical_benchmarks/exact_1d_finite.csv` | Five horizons for the exact one-dimensional objective at power one. |
| `data/analytical_benchmarks/critical_scalar_model.csv` | Twelve scalar-model calculations along three paths approaching the threshold. |
| `data/analytical_benchmarks/check_results.json` | Symbolic identities and the same three benchmark tables. |
| `data/analytical_benchmarks/finite_cost_monte_carlo.json` | Independent cost estimates at three fixed parameters. |
| `data/calibration_experiment/calibration_results.csv` | Twelve scenarios comparing the finite rule, stationary scale and available numerical reference. |
| `data/calibration_experiment/calibration_trajectory_costs.npz` | Complete trajectory-cost arrays and their policy identifiers. |
| `data/calibration_experiment/calibration_experiment_design.json` | Input distribution, parameters, sample size, seed and interval definitions. |
| `data/measured_calibration_gains/scenarios.csv` | The 259 expanded scenarios and the fixed policy parameters. |
| `data/measured_calibration_gains/expanded_calibration_results.csv` | Full-sample paired statistics for all 259 scenarios. |
| `data/measured_calibration_gains/expanded_calibration_block_moments.csv` | 66,304 rows of moments from nonoverlapping trajectory blocks. |
| `data/measured_calibration_gains/policies_N*.tsv` | Seven headerless parameter tables, each with 74 rows and two columns, alpha then delta. |
| `data/measured_calibration_gains/expanded_calibration_design.json` | Expanded grids, random-stream specification and statistical definitions. |
| `data/measured_calibration_gains/observed_zero_crossing_brackets.json` | Adjacent sampled powers with opposite estimated signs, together with their pointwise intervals. |
| `code/calibration_reference_parameters.csv` | Eight archived numerical reference parameters with their public source paths and version. |
| `code/monte_carlo_cases.csv` | The three fixed cases used by the separate Monte Carlo comparison. |

## Parameters and identifiers

| Field | Meaning |
|---|---|
| `N` | Number of insertions. |
| `d` | Ambient dimension. The paired experiments use d = 2. |
| `alpha` | Edge-power exponent. |
| `epsilon` | Excess power alpha - 1. |
| `gamma` | Exponential-memory parameter. |
| `delta` | Update fraction 1 - gamma for the indicated exact or numerical parameter. |
| `H` | Initialization constant H_(d,alpha). The dimension table evaluates it at alpha = 1. |
| `lambda_star` | Transition threshold 2 log(4(d+2)/(3d+7)). |
| `r` | Scaled power (alpha-1) log(N)/lambda_star(d). |
| `family` | `scaled_r` for a joint-window scenario or `fixed_alpha` for a fixed-power scenario. |
| `case` | The selected r or alpha value, according to `family`. |
| `case_index` | Zero-based scenario index within a horizon. |
| `delta_finite` | Update fraction selected by the finite scalar balance. |
| `delta_stationary_scale` | Analytical stationary-scale update fraction. |
| `delta_reference` | Archived numerical finite-horizon update fraction. Empty when unavailable. |
| `finite_column`, `stationary_column` | Zero-based policy positions in the C++ trajectory output and corresponding parameter table. |
| `N_delta_finite`, `N_delta_stationary_scale` | N multiplied by the indicated update fraction. |
| `trajectories` | Number of independent complete trajectories used in the row. |
| `start` | Zero-based starting trajectory index of a block. |
| `count` | Number of trajectories in that block. |
| `seed` | Pseudorandom initialization value for the specified experiment. |
| `source_file`, `source_version` | Dataset path within the cited public repository and its version tag. |
| `stored_objective`, `stored_reference_cost` | Archived numerical finite-horizon cost at the supplied reference parameter. |

The `policies_N*.tsv` files have no header. Their first and second columns are alpha and delta. The row order is the policy order used by `disk_calibration.cpp`; `finite_column` and `stationary_column` identify each scenario's pair. There are 37 scenarios and 74 policy columns at each of seven horizons.

## Analytical benchmarks

In `dimension_constants.csv`, `reported_H` is the rounded initialization constant printed in the article, and `within_rounding` indicates agreement to that precision. `critical_prefactor` is sqrt(H_(d,1)/(c_(d,1) q_(d,1) lambda_star(d))), with c_(d,1) = d/(d+1) and q_(d,1) = (3d+7)/(4(d+2)).

In `exact_1d_finite.csv`, `delta` is the numerically evaluated minimizer of the exact d = 1, alpha = 1 formula. `sqrtN_delta` is sqrt(N) delta. `six_scaled_excess` is 6[F_(1,1,N)(1-delta)-N/2]/sqrt(N). `absolute_slope` is the absolute derivative with respect to delta at that parameter. `curvature_positive` records positivity of the second derivative. These are numerical evaluations of the stated exact expression.

In `critical_scalar_model.csv`, `logN` is L = log(N). The `path` values `centered`, `below_weak` and `above_weak` mean epsilon = [lambda_star(2)+s]/L with s respectively 0, -1/sqrt(L) and +1/sqrt(L). `w` is the Lambert quantity w_N. `model_root_over_Delta` divides the root of the scalar balance by Delta_N. `w_over_sqrtL_div_lambda` divides w_N by sqrt(L)/lambda_star(2). The calculations use arbitrary-precision scalar arithmetic; the underlying initialization integral is evaluated numerically as specified in `analytical_benchmarks.py`.

The `symbolic` keys in `check_results.json` report equality checks for the squared coefficient norms and their first two derivative sequences, the leading fourth moment, chi_(d,1), the identity defining q_(d,alpha), and H_(1,1) = 1/6. The remaining keys reproduce the three benchmark tables above.

The separate `finite_cost_monte_carlo.json` compares three archived costs with fresh trajectory estimates. Each row provides `mean`, `standard_error`, `stored_objective`, and `standardized_difference` = (mean - stored_objective)/standard_error. These are cost comparisons at fixed parameters.

## Paired calibration experiment

The twelve scenarios combine N = 256, 1024, 4096 with r = 0, 0.5, 1, 2. Parameters are fixed before simulation. Each horizon uses 32,768 independent input sequences shared by all its policies. Horizon streams are independent. The archived numerical reference is available for N = 1024 and 4096; its fields are empty for N = 256.

Write A_i, B_i and R_i for the finite-rule, stationary-scale and reference costs on trajectory i. The fields `mean_finite`, `mean_stationary_scale` and `mean_reference` are their sample means. `saving_estimate_pct` equals 100[1-mean(A)/mean(B)]. `reference_excess_estimate_pct` equals 100[mean(A)/mean(R)-1].

For paired costs X_i and Y_i and m independent trajectories, the estimated standard error of mean(X)/mean(Y) is sd[X_i-(mean(X)/mean(Y))Y_i]/[sqrt(m) mean(Y)], with sample standard deviation. The fields `saving_standard_error_pct` and `reference_excess_standard_error_pct` multiply this ratio standard error by 100. The corresponding `lower95_pct` and `upper95_pct` fields use the estimate minus and plus 1.96 standard errors.

In `calibration_trajectory_costs.npz`, every `costs_N...` array has shape (policies, trajectories). `policy_r_N...` and `policy_name_N...` identify its rows. There are 8 policies at N = 256 and 12 at each of the other two horizons. These arrays contain all complete-trajectory costs for this twelve-scenario experiment.

## Expanded experiment and moment reconstruction

The expanded design has 31 joint-window r values and six fixed alpha values at seven horizons, for 259 scenarios in total. It uses 32,768 independent trajectories per horizon and 229,376 distinct input sequences overall. All 74 policies within a horizon share the same inputs. The full expanded trajectory arrays are retained by the author; the supplied moments reconstruct every reported estimate and interval, and the programs regenerate the trajectories.

Write A for finite-rule cost, B for stationary-scale cost and D = A - B. The expanded results use the following fields.

| Field | Meaning |
|---|---|
| `mean_finite`, `mean_stationary_scale` | Sample means of A and B. |
| `mean_difference` | Sample mean of D. |
| `variance_difference`, `variance_stationary_scale` | Unbiased sample variances of D and B. |
| `covariance_difference_stationary_scale` | Unbiased sample covariance of D and B. |
| `saving_estimate_pct` | -100 mean(D)/mean(B). |
| `saving_standard_error_pct` | 100 sd[D-(mean(D)/mean(B))B]/[sqrt(m) mean(B)]. |
| `saving_lower95_pct`, `saving_upper95_pct` | Estimate minus and plus 1.96 standard errors. |
| `saved_cost_per_input` | -mean(D)/N. |

Each scenario is divided into 256 nonoverlapping blocks of 128 trajectories, giving 66,304 moment rows. In the block file, `trajectories` and `count` both refer to the block size. Pooling variances and covariance requires within-block and between-block contributions. `code/calibration_statistics.py` implements that calculation and checks the reconstructed estimates against the full-sample table. Averages of block ratios do not reproduce the full-sample ratio.

The design JSON specifies the C++17 `std::mt19937_64` generator, the conversion to uniform values and the seed mapping for each horizon and trajectory. It also records the fixed grids and numerical settings. The `seed_vector_sha256` value identifies the vector of distinct trajectory seeds. It is a reproducibility checksum.

## Reading the measured-gain figure

The named figure `measured_calibration_gains` uses the same linear saving scale in Fig. 5(a) and Fig. 5(b). Fig. 5(a) displays the 189 joint-window cases with r <= 2 and magnifies intersections of the plotted segments near r = 0.5. All 217 joint-window cases, including the 28 with r > 2, remain in the source data. Fig. 5(b) shows the 42 fixed-power cases. Segments connect sampled estimates and introduce no additional observations.

Fig. 5(c) displays all 91 negative estimates as positive percentage cost increases on a logarithmic axis, including those with r > 2. Its interval endpoints are `-saving_upper95_pct` and `-saving_lower95_pct`. Circles denote joint-window cases and triangles denote fixed-power cases. The highlighted curve selects the largest observed point estimate of cost increase among the 37 scenarios at each horizon. This selection has no simultaneous confidence interpretation.

The zero-crossing JSON gives `r_left` and `r_right`, the adjacent sampled values of opposite estimated sign, with their respective `saving_pct`, `lower95_pct` and `upper95_pct` fields prefixed by `left_` or `right_`. These empirical brackets locate observed sign changes on the sampled grid. They do not certify a continuous zero boundary. Fixed-power comparisons provide finite-sample sensitivity evidence within the tested model.
