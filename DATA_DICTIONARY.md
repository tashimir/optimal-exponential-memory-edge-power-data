# Data dictionary

The [README](README.md) maps each dataset to its article figure or table. The unit ball has radius one; lengths, costs and all scaling quantities are expressed in these normalized units. `log` denotes the natural logarithm. Relative losses are fractions, and figures/tables multiply them by 100 to display percentages. Flags are 1 for true and 0 for false unless a textual result is stored.

## Mathematical and numerical conventions

The retained-edge factor is h_alpha(gamma)=gamma^alpha+(1-gamma)^alpha. The uniform objective is Phi_(d,alpha)=h_alpha M_(d,alpha). The exact adversarial objective through power three is h_alpha [2/(1+gamma)]^alpha. The balanced policy minimizes the maximum of the two normalized losses.

The finite-horizon phase-transition dataset compares correction *scales*: C_tr=1/(N epsilon_N delta_N^2) and C_stat=delta_N/epsilon_N, with epsilon_N=alpha_N-1. The curve stored as `correction_balance` is log(C_tr/C_stat)/log(N). Coefficients multiplying these scales in the refined theorem are not included in that ratio.

The local-objective dataset uses `G_N`, `a_w` and `b_w` for the normalized objective, reciprocal-balance component and entropy component. Older notation mathcal P_N, A_N and B_N refers to the same stored arrays. Derivatives of the finite objective are evaluated by a degree-18 Chebyshev projection of the Chebyshev-Lobatto samples. The stored `C0`, `C1` and `C2` values are derivative-specific maximum errors on the sample grid, whereas the high-dimensional `C2_norm` takes the maximum over all three derivative orders on the continuous interval.

The high-dimensional dataset uses exact second- and fourth-moment formulas. Its dashed reference is (38656/2025)/d^2, anchored at d=2 on the alpha=4 differentiated remainder curve. These data contain no sampling error.

The earlier uniform-adversarial Monte Carlo diagnostics use 32 streams. The approximate 99% half-width uses factor 2.75. The retained-count allowance `effective_total` divides the count by 1.02; it is a diagnostic convention. A Monte Carlo case is accepted after at least two sample-size levels, diagnostic retained count greater than 100000, half-width at most .002 max(1,absolute normalized mean), and between-level change at most .001 max(1,absolute normalized mean). Pseudorandom initialization values are not distributed. Quadrature resolution differences and Monte Carlo intervals are separate evidence types.

## Column definitions

The following alphabetical dictionary covers the columns of the 42 original scientific CSV files. New experiment fields are defined in the calibration section below. `FILE_MANIFEST.csv` provides the exact file-level schemas and row counts. Parameters and validation JSON files retain the same meanings, with array-valued keys listing the tested grids and resolution settings.

| Column | Meaning |
|---|---|
| `C0` | Maximum absolute profile discrepancy on the stored z grid. |
| `C0_resolution_difference` | Maximum absolute profile difference between the 65-point and aligned 129-point evaluations. |
| `C1` | Maximum absolute first-derivative discrepancy on the stored z grid. |
| `C1_resolution_difference` | Maximum absolute first-derivative difference between the two profile resolutions. |
| `C2` | Maximum absolute second-derivative discrepancy on the stored z grid. |
| `C2_norm` | Maximum over derivative orders 0,1,2 of the supremum absolute remainder on gamma in [.5,.9], after subtracting the leading and first dimension terms. |
| `C2_resolution_difference` | Maximum absolute second-derivative difference between the two profile resolutions. |
| `Delta_N` | Lambert moving-window scale delta_N exp(w_N/2), as defined in the article. |
| `G_N` | Normalized finite objective G_N(z), as defined in the article. |
| `H` | Geometric accumulated initialization constant H_(d,alpha), evaluated at the row parameters. |
| `H_N` | Geometric accumulated initialization constant H_(d,alpha), evaluated at the row parameters. |
| `H_constant` | Geometric accumulated initialization constant H_(d,alpha), evaluated at the row parameters. |
| `H_d_1` | Geometric initialization constant H_(d,1). |
| `H_d_alpha` | Geometric accumulated initialization constant H_(d,alpha), evaluated at the row parameters. |
| `H_resolution_error` | Absolute difference between the two finest stored quadrature evaluations of H. |
| `N` | Number of insertions. |
| `a_w` | Reciprocal-balance component w_N(z+1/z-2)/(2(w_N+1)); it combines contributions after centering the objective. |
| `absolute_error` | Absolute difference between value and reference. |
| `accepted` | Numerical validation flag. Finite-size data require location_rel_change<.0025, value_rel_change<.001, first_order_ok and neighbor_ok; Monte Carlo records use the confidence and stability criteria described above. |
| `active_derivative_order` | Derivative order attaining C2_norm. |
| `active_m` | Integer block size attaining the largest witness certificate at the reported gamma. |
| `active_m_normalized` | active_m divided by log(alpha log(alpha))/log(2). |
| `adversarial_at_balanced` | Adversarial objective evaluated at gamma_balanced. |
| `adversarial_at_uniform` | Adversarial objective evaluated at gamma_uniform. |
| `adversarial_cost` | Worst-case retained-edge objective (gamma^alpha+(1-gamma)^alpha) [2/(1+gamma)]^alpha, in the exact power range. |
| `adversarial_loss_at_uniform` | adversarial_at_uniform/adversarial_minimum - 1. |
| `adversarial_minimum` | Minimum retained-edge objective for the exact adversarial criterion. |
| `adversarial_regret` | Adversarial relative loss adversarial_cost/adversarial_minimum - 1. |
| `alpha` | Positive edge-power exponent alpha; in the joint window alpha=1+lambda/log(N). |
| `alternation` | Per-point retained-edge lower bound from the periodic block witness with m=1. |
| `angular_order` | Number of angular quadrature nodes. |
| `artifact` | Scientific dataset or calculated-object identifier. |
| `auxiliary_vertex_label` | Label x_i of the auxiliary vertex. |
| `auxiliary_vertex_x` | First Cartesian coordinate of x_i. |
| `auxiliary_vertex_y` | Second Cartesian coordinate of x_i. |
| `b_w` | Entropy component (z log(z)-z+1)/(w_N+1), arising from the stationary power expansion. |
| `balanced_maximum_loss` | Maximum of the two criterion-relative losses at gamma_balanced. |
| `barrier` | Phi_(2,alpha)(1-delta_mid)-c_(2,alpha). |
| `barrier_ratio` | barrier/(alpha-14)^2; multiply by 1024 for the normalized barrier plot. |
| `base_m` | Base block-size cutoff in the witness computation. |
| `best_block` | Largest per-point lower certificate among the evaluated nonalternating block witnesses, m>=2. |
| `beta` | Single-size exponent -log(delta)/log(N), using the indicated optimizer. This differs from the size-pair exponent beta_quotient. |
| `beta_512` | Single-size exponent -log(delta)/log(N), using the indicated optimizer. This differs from the size-pair exponent beta_quotient. |
| `beta_quotient` | Size-pair exponent -log(delta_(4N)/delta_N)/log(4), using computed finite optimizer distances at their respective powers. |
| `branch_converged` | Indicator that the prescribed numerical enclosure-width criterion was reached. |
| `branch_relative_width` | (upper_enclosure-lower_enclosure)/upper_enclosure. |
| `cgal_version` | Version of the geometry library used in the numerical calculation. |
| `check` | Name of a numerical validation comparison. |
| `checked_midpoints` | Number of interpolation midpoint tests. |
| `collapse_ratio` | Computed finite optimizer distance divided by theory_scale. |
| `correction_balance` | -log(N delta_N^3)/log(N), with analytical stationary delta_N. This equals log(C_tr/C_stat)/log(N) for the scales C_tr=1/(N epsilon delta_N^2), C_stat=delta_N/epsilon; coefficient factors are omitted. |
| `cost_correction_constant` | Sublinear cost coefficient (alpha+1) c^(1/(alpha+1)) [H/(2 alpha)]^(alpha/(alpha+1)). |
| `critical_prefactor` | sqrt(H_(d,1)/(c_(d,1) q_(d,1) lambda_star)), the coefficient of sqrt(log(N)/(N log(log(N)))) in the exactly critical optimizer distance. Here c_(d,1)=d/(d+1) and q_(d,1)=(3d+7)/(4(d+2)). |
| `curvature` | Second derivative of the endpoint objective at the computed interior branch point. |
| `curvature_step_error` | Absolute curvature discrepancy between the two finite-difference step sizes used. |
| `d` | Ambient dimension d of the unit Euclidean ball. |
| `dataset` | Scientific dataset or calculated-object identifier. |
| `delta` | Distance 1-gamma from the endpoint. |
| `delta_128` | Computed finite optimizer distance 1-gamma at the radial quadrature order indicated by the suffix. |
| `delta_256` | Computed finite optimizer distance 1-gamma at the radial quadrature order indicated by the suffix. |
| `delta_512` | Computed finite optimizer distance 1-gamma at the radial quadrature order indicated by the suffix. |
| `delta_N` | Analytical stationary scale q_(d,alpha)^(1/(alpha-1)); in d=2, q_(2,alpha)=(14-alpha)/16. It is distinct from a computed finite optimizer distance. |
| `delta_lower` | Lower numerical bracket endpoint for the interior endpoint-branch distance. |
| `delta_mid` | Representative branch distance within the numerical bracket. |
| `delta_ratio` | delta_mid/(alpha-14); multiply by 56 for the normalized branch plot. |
| `delta_upper` | Upper numerical bracket endpoint for the interior endpoint-branch distance. |
| `derivative_logdelta` | Centered objective derivative with respect to log(delta), using step .002. |
| `derivative_scaled` | Absolute derivative_logdelta divided by max(1,absolute objective). |
| `dimension` | Ambient dimension d of the unit Euclidean ball. |
| `doubling_rounds` | Number of successive sample-size levels considered in Monte Carlo validation. |
| `edge_type` | Spine or leaf edge in the labelled network. |
| `effective_total` | Diagnostic retained count streams*retained_per_stream/1.02, using a fixed allowance for dependence. An independently estimated effective sample size is unavailable. |
| `envelope` | Maximum of alternation and best_block. At alpha=256 throughout the displayed interval, best_block dominates. |
| `epsilon_upper` | Separation parameter used to construct theorem_upper. |
| `evaluation_resolution` | Profile grid identifier: display (129 points) or independent numerical verification (65 points). |
| `evaluations` | Number of numerical objective evaluations used for a computed optimizer. |
| `first_order_ok` | Indicator derivative_scaled<2e-5. |
| `gamma` | Fixed exponential-memory parameter gamma. |
| `gamma_adversarial` | Exact worst-case optimizer 1/(1+2^(-1/(alpha-1))). |
| `gamma_at_maximum` | Location attaining the reported differentiated remainder norm. |
| `gamma_balanced` | Parameter minimizing the maximum of the uniform and adversarial relative losses. |
| `gamma_interval_width` | Final numerical optimizer bracketing width in gamma. |
| `gamma_lower_envelope` | Numerically selected minimizing gamma for the block-witness lower envelope. |
| `gamma_min` | Numerically selected minimizing gamma for the block-witness lower envelope. |
| `gamma_uniform` | Memory parameter minimizing the uniform stationary objective. |
| `half_width_99` | Reported approximate 99% confidence half-width: 2.75 times sample standard deviation of stream means divided by sqrt(number of streams). |
| `high_value` | Evaluations at the indicated quadrature resolutions. |
| `initial_gamma_count` | Number of gamma nodes before interpolation refinement. |
| `insertion_length` | Euclidean distance between p_i and x_(i-1). |
| `is_envelope_minimum` | Indicator for the smallest envelope value on the stored gamma grid; this is distinct from continuous interval optimization. |
| `key` | Name of a numerical method parameter; its setting is in value. |
| `lambda` | Joint-window parameter (alpha-1) log(N). |
| `lambda_ratio` | Scaled window parameter r=lambda/lambda_star. |
| `lambda_star` | Leading transition threshold 2 log(4(d+2)/(3d+7)). |
| `leaf_length` | Length gamma times insertion_length. |
| `leaf_ratio` | leaf_length/insertion_length, equal to gamma. |
| `length` | Euclidean edge length. |
| `location_constant` | Sublinear location coefficient [H/(2 alpha c)]^(1/(alpha+1)), with c=d/(d+alpha). |
| `location_rel_change` | Absolute finest-minus-medium optimizer-distance difference divided by the finest optimizer distance. |
| `log2N` | Base-two logarithm of N. |
| `log2N_left` | Base-two logarithm of the smaller N in a size pair. |
| `log2N_right` | Base-two logarithm of the larger 4N in a size pair. |
| `log_normalized_distance` | Natural logarithm of collapse_ratio. |
| `low_value` | Evaluations at the indicated quadrature resolutions. |
| `lower_bound` | Lower enclosure for the minimum over gamma of the block-witness lower certificate. |
| `lower_enclosure` | Lower enclosure for the minimum over gamma of the block-witness lower certificate. |
| `lower_numerical_upper` | Upper enclosure for the minimum of the lower-certificate family. The unrestricted adversarial optimum has the separate upper bound theorem_upper. |
| `maximum_relative_interpolation_error` | Largest relative discrepancy between interpolation and direct midpoint evaluation. |
| `mean_cost` | Mean retained-edge cost per sample within a Monte Carlo stream. |
| `medium_value` | Evaluations at the indicated quadrature resolutions. |
| `neighbor_left` | Objective change on replacing log(delta) by log(delta)-.02. |
| `neighbor_ok` | Indicator both neighbor changes are at least -1e-8 max(1,objective). |
| `neighbor_right` | Objective change on replacing log(delta) by log(delta)+.02. |
| `normalized_cost` | Monte Carlo mean_cost divided by the deterministic uniform minimum; aggregate files report the mean over streams. |
| `normalized_lower` | lower_bound times log(alpha)/(2 log(2)). |
| `normalized_upper` | theorem_upper times log(alpha)/(2 log(2)). |
| `objective` | Finite retained-edge expectation F_(d,alpha,N)(gamma); a numerical suffix specifies radial quadrature order. |
| `objective_256` | Finite retained-edge expectation F_(d,alpha,N)(gamma); a numerical suffix specifies radial quadrature order. |
| `objective_512` | Finite retained-edge expectation F_(d,alpha,N)(gamma); a numerical suffix specifies radial quadrature order. |
| `objective_minus_endpoint` | Phi_(2,alpha)(1-delta)-c_(2,alpha). |
| `order` | Quadrature or series order, interpreted with the representation or check column. |
| `p_x` | First Cartesian coordinate of input point p_i. |
| `p_y` | Second Cartesian coordinate of input point p_i. |
| `panel` | Geometric construction identifier (path, caterpillar or star). |
| `pareto_segment` | Indicator that gamma lies between the two criterion-specific optima. |
| `passed` | Outcome of the named numerical validation check. |
| `point_index` | Processing index i of input point p_i. |
| `point_label` | Label p_i of the input vertex. |
| `point_x` | First Cartesian coordinate of input point p_i. |
| `point_y` | Second Cartesian coordinate of input point p_i. |
| `policy` | Criterion-specific policy identifier: uniform, balanced or adversarial. |
| `profile_sum` | A_N(z)+B_N(z), equivalently a_w+b_w. |
| `quantity` | Mathematical quantity being compared in a convergence record. |
| `radial_order` | Number of radial quadrature nodes. |
| `reference` | Analytical or independently evaluated comparison value. |
| `refinement_rounds` | Number of adaptive gamma-grid interpolation refinement rounds. |
| `regret` | normalized_cost-1 in independent Monte Carlo validation. |
| `relative_band_width` | (theorem_upper-lower_bound)/theorem_upper. |
| `relative_medium_high` | Absolute difference between medium_value and high_value divided by the absolute high-resolution value, with a numerical floor near zero. |
| `representation` | Integral or analytical representation used to evaluate a constant. |
| `resolution` | Quadrature-resolution identifier; low, medium and high settings are listed in the parameter records. |
| `retained_per_stream` | Number of retained observations in each Monte Carlo stream. |
| `retained_samples` | Number of retained observations in each Monte Carlo stream. |
| `row_error` | Maximum absolute deviation from one of a numerical Markov-operator row sum. |
| `scale_type` | Regime selecting the reference scale: subcritical, critical or supercritical. |
| `scaled_difference` | d times [M_(d,alpha)(gamma)-sigma(gamma)^alpha], where sigma^2=2/(1+gamma). |
| `second_crossover` | Correction-scale crossover 3 lambda_star/2. |
| `series_order` | Order of the truncated endpoint expansion used in numerical evaluation. |
| `shard_count` | Total number of data partitions in the same family. |
| `shard_index` | Zero-based index of a data partition. |
| `spine_length` | Length (1-gamma) times insertion_length. |
| `spine_ratio` | spine_length/insertion_length, equal to 1-gamma. |
| `stability_change` | Absolute change in the mean normalized Monte Carlo cost from the preceding sample-size level. |
| `state_bins` | Number of state discretization bins. |
| `stationary_iterations` | Number of distribution-iteration steps in the stationary numerical evaluation. |
| `stationary_residual` | L1 difference between consecutive state-probability vectors at termination. |
| `stationary_scale` | Analytical stationary scale q_(d,alpha)^(1/(alpha-1)); in d=2, q_(2,alpha)=(14-alpha)/16. It is distinct from a computed finite optimizer distance. |
| `status` | Outcome of the named numerical validation check. |
| `step` | Insertion index i. |
| `steps` | Number of time steps represented in the finite evaluation. |
| `stream` | Independent pseudorandom stream identifier. |
| `streams` | Number of independent Monte Carlo streams. |
| `subdivisions` | Number of interval subdivisions in the envelope enclosure calculation. |
| `theorem_upper` | Proved separation-based upper bound for the unrestricted adversarial optimum. |
| `theory_scale` | Regime-specific reference S_N(r): subcritical boundary scale, critical Lambert scale, or supercritical stationary scale. |
| `thinning` | Number of simulation updates between retained observations. |
| `threshold` | Prescribed tolerance for the numerical comparison. |
| `truncation_factor` | Multiplier applied to base_m for a truncation comparison. |
| `truncation_m` | Largest block size evaluated in the witness computation. |
| `uniform_at_adversarial` | Uniform objective evaluated at gamma_adversarial. |
| `uniform_at_balanced` | Uniform objective evaluated at gamma_balanced. |
| `uniform_cost` | Stationary retained-edge objective Phi_(d,alpha)(gamma); exact quadratic evaluation is used when alpha=2. |
| `uniform_cost_numeric` | Numerical stationary objective before replacement by the exact quadratic formula where applicable. |
| `uniform_cost_used` | Stationary retained-edge objective Phi_(d,alpha)(gamma); exact quadratic evaluation is used when alpha=2. |
| `uniform_loss_at_adversarial` | uniform_at_adversarial/uniform_minimum - 1. |
| `uniform_minimum` | Minimum stationary retained-edge objective for the uniform input model. |
| `uniform_regret` | Uniform relative loss uniform_cost/uniform_minimum - 1. |
| `upper_enclosure` | Upper enclosure for the minimum of the lower-certificate family. The unrestricted adversarial optimum has the separate upper bound theorem_upper. |
| `value` | Numerical value of the named check, or value of a named parameter in key/value files. |
| `value_rel_change` | Absolute finest-minus-medium objective difference divided by the absolute finest objective. |
| `w_N` | Principal Lambert-W quantity specifying Delta_N in the joint critical window. |
| `x0` | First Cartesian coordinate of the starting endpoint of an edge. |
| `x1` | First Cartesian coordinate of the ending endpoint of an edge. |
| `x_current_x` | First Cartesian coordinate of x_i. |
| `x_current_y` | Second Cartesian coordinate of x_i. |
| `x_previous_x` | First Cartesian coordinate of x_(i-1). |
| `x_previous_y` | Second Cartesian coordinate of x_(i-1). |
| `y0` | Second Cartesian coordinate of the starting endpoint of an edge. |
| `y1` | Second Cartesian coordinate of the ending endpoint of an edge. |
| `z` | Multiplicative displacement from Delta_N: the tested endpoint distance is Delta_N z. |
| `z_order` | Number of Chebyshev-Lobatto points in the z grid. |
| `zero_length` | Indicator that an edge has zero geometric length. |


## Paired calibration experiment

`data/calibration_experiment` contains the complete twelve-scenario experiment. `N`, `r`, `alpha`, `H`, and the `delta_*` columns identify fixed policies. `delta_stationary_scale` is the analytical stationary scale, including zero at power one; it is not the exact stationary minimizer. `delta_reference` is a stored numerical finite-horizon parameter from the highest archived resolution. No such reference is available for N=256.

`mean_finite`, `mean_stationary_scale`, and `mean_reference` are sample means of complete-trajectory costs. `saving_estimate_pct` equals 100(1-mean_finite/mean_stationary_scale). `reference_excess_estimate_pct` equals 100(mean_finite/mean_reference-1). The corresponding `standard_error_pct`, `lower95_pct`, and `upper95_pct` fields give paired delta-method uncertainty. Pointwise 95% normal intervals use the estimate plus or minus 1.96 standard errors. Empty reference fields are unavailable quantities.

For trajectory costs A_i and B_i, the standard error of their mean ratio is sd(A_i-(mean(A)/mean(B))B_i)/(sqrt(m)mean(B)). Trajectories are independent; all policies within a horizon share their inputs. The seed and complete design are supplied. Each array `costs_N...` in the NPZ file has shape (policies, trajectories), identified by the matching `policy_r_N...` and `policy_name_N...` arrays. Negative savings are retained.

The `data/analytical_benchmarks` files contain exact-objective, scalar-model and geometric-constant calculations. Their programs and seeds are supplied in `code`. Original numerical records retain their scientific identifiers and values; current descriptive paths are indexed by `LEGACY_PATH_MAP.csv`.

## Expanded calibration experiment

`data/measured_calibration_gains` contains 259 scenarios. `family` is `scaled_r` for the joint-window path or `fixed_alpha` for a fixed-power sensitivity scenario; `case` gives the corresponding value. `N`, `r`, `alpha`, `H`, `delta_finite` and `delta_stationary_scale` specify the design and fixed policies. `case_index`, `finite_column` and `stationary_column` are zero-based indices. Each `policies_N*.tsv` is a headerless two-column table of alpha and delta in kernel output order.

`expanded_calibration_results.csv` contains complete-trajectory statistics. Write A for finite-rule cost, B for stationary-scale cost and D=A-B. `mean_difference` is mean(D); `variance_difference` and `variance_stationary_scale` are unbiased sample variances of D and B; `covariance_difference_stationary_scale` is their unbiased sample covariance. The saving estimate is -100 mean(D)/mean(B). Its paired standard error is 100 sd(D-(mean(D)/mean(B))B)/(sqrt(m)mean(B)). The `saving_lower95_pct` and `saving_upper95_pct` columns use estimate +/-1.96 standard errors. Units for estimates, standard errors and limits are percentage points. `saved_cost_per_input` is -mean(D)/N; `N_delta_*` gives N times the respective update fraction.

`expanded_calibration_block_moments.csv` contains the same moment definitions for each of 256 nonoverlapping blocks of 128 trajectories per scenario, totaling 66,304 rows. `start` is the zero-based trajectory index and `count` is the block size. `trajectories` repeats that block count. Pooling requires both within-block and between-block contributions to variances and covariance. Averaging block ratios or block standard errors does not reconstruct the full-sample statistic; `code/calibration_statistics.py` implements the pooled calculation.

Every scenario at a given horizon uses the same 32,768 input sequences. There are 229,376 distinct input sequences over the seven horizons, with the seed mapping and generator stated in the design JSON. The normal delta-method intervals are pointwise. The zero-gain bracket JSON records adjacent sampled r values of opposite estimated sign and their intervals. It gives no simultaneous confidence interval or certified threshold for a continuous zero boundary.

The named figure `measured_calibration_gains` shows the same saving estimates on common linear axes in panels (a,b). Panel (c) contains the 91 negative cases, displaying `-saving_estimate_pct` as a positive percentage cost increase. The interval endpoints there are `-saving_upper95_pct` and `-saving_lower95_pct`. Circles denote `scaled_r` and triangles `fixed_alpha`. The highlighted curve takes the largest point estimate of the increase among the 37 scenarios at each horizon, and has no simultaneous confidence interpretation. All 259 source records are retained.
