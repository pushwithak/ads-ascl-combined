# Boundary-Layer Momentum Structure, Not Surface Enthalpy Input, Explains Drag-Dependent Intensification Timing in Axisymmetric CM1 Hurricanes

**Authors:** AI-Augmented Scientific Pipeline (AKD)  
**Date:** 2026-06-15  
**Keywords:** surface drag, boundary layer, tropical cyclone intensification, CM1, air–sea fluxes

> *This manuscript was generated with AI assistance and requires researcher validation before publication.*

## Abstract
Hypothesis 2.1 posits that reduced high-wind drag modifies tropical cyclone (TC) intensity primarily through boundary-layer (BL) momentum/structural changes rather than by directly altering surface enthalpy input, with structural responses emerging before thermodynamic drivers. This hypothesis was evaluated using idealized axisymmetric CM1 hurricane experiments that sweep constant surface drag (Cd) across four cases (baseline, low-Cd, mid-Cd, and high-Cd) while retaining interactive surface fluxes. Across the Cd sweep, mature intensity converged to essentially the same ceiling (peak maximum wind ~105–110 m s⁻¹ and minimum surface pressure ~900 hPa by ~190 h), but intensification timing differed dramatically: the low-Cd case lagged the baseline by ~21 h at 33 m s⁻¹, ~29 h at 50 m s⁻¹, and ~53 h at 70 m s⁻¹, whereas the high-Cd case reached early thresholds tens of hours sooner and exhibited early wind anomalies up to ~+30 m s⁻¹. Surface enthalpy/moisture-flux proxies were nearly coincident across all Cd levels, with flux anomalies only ~2–3% of cumulative enthalpy exchange. In contrast, BL/structural metrics (low-level vorticity spin-up and RMW contraction) exhibited coherent, signed anomalies aligned with intensity timing differences. Overall, the results **partially support** Hypothesis 2.1: momentum/structure mediation is strongly supported, while the claimed sequencing and thermodynamic-pathway isolation cannot be rigorously established without the imposed-flux experiments.

## 1. Introduction
Surface drag is central to tropical-cyclone intensity theory because it links air–sea momentum exchange to the near-surface wind field that both dissipates kinetic energy and regulates boundary-layer inflow. In classical thermodynamic perspectives, intensity is constrained by the surface enthalpy flux that sustains the storm’s energy cycle and by the efficiency of converting enthalpy input into mechanical work (e.g., Emanuel, 1986, 1995). However, drag can also alter the storm’s internal dynamics by reshaping BL convergence, the radial distribution of angular momentum, and the structure of the eyewall and radius of maximum wind (RMW), potentially changing intensification pathways even when thermodynamic forcing is similar.

A persistent ambiguity in the literature is whether drag perturbations should be interpreted mainly as changes in surface energy input (through wind-speed-dependent fluxes) or as changes in BL momentum closure and storm structure (e.g., Smith, 2009; Montgomery et al., 2010; Kim et al., 2022). This distinction matters operationally because many “reduced high-wind drag” parameterizations are introduced to represent wave-state effects at extreme winds, yet their simulated intensity impacts may emerge through either a thermodynamic pathway (modified enthalpy flux) or a momentum/structural pathway (modified inflow, eyewall contraction, and spin-up).

The present study targets this separation explicitly. The hypothesis tested is stated verbatim from the Stage-1 formulation: **“Hypothesis 2.1: Reduced high-wind drag modifies tropical cyclone intensity primarily through altered boundary-layer momentum structure (convergence/divergence patterns, RMW shifts, BL jet properties) rather than through direct changes in surface enthalpy flux, such that controlled Cd perturbations produce measurable structural responses before thermodynamic intensity signals emerge.”**

Using an idealized axisymmetric CM1 hurricane configuration and a sweep of constant drag coefficients, this paper asks whether intensity differences across Cd are better explained by BL/structural adjustments than by changes in surface enthalpy input. Section 2 summarizes the experiment design and the mapping between planned and analyzed experiments. Section 3 presents the intensity response, the structural/momentum response, and the surface-flux/energetic corroboration. Section 4 provides an explicit verdict on Hypothesis 2.1, including key quantitative contrasts and limitations.

## 2. Experimental Design

### 2.1 Model Configuration
All simulations are based on the repository’s idealized **axisymmetric hurricane** CM1 configuration (`run/config_files/hurricane_axisymmetric/namelist.input`) with the co-located thermodynamic environment (`isnd=7` with `input_sounding`). Surface flux diagnostics were enabled in the template (per the Stage-3 requirement that `output_sfcflx=1` be available). Results presented here use 6-h running means and cover approximately 0–190 h of model time.

### 2.2 Baseline
The baseline experiment is the unmodified axisymmetric hurricane template, serving as the reference evolution of maximum wind speed and minimum surface pressure and as the baseline for anomaly calculations in intensity, structure, and flux diagnostics.

### 2.3 Perturbation Experiments
The Stage-3/Stage-4 workflow specification implemented five experiments: (i) baseline; (ii) reduced drag via constant Cd proxy (`cnstcd=0.0005`); (iii) reduced drag with imposed constant SH/LH fluxes (`set_flx=1` with baseline flux constants); (iv) reduced SH/LH fluxes with imposed flux (`set_flx=1` with reduced constants) and baseline drag; and (v) a capability probe varying `cecd`.

However, the Stage-5 analysis product used as ground truth for the results contains a different set: **four experiments that form a Cd sweep with interactive fluxes**—`exp_RQ2_H21_baseline`, `exp_RQ2_H21_low_Cd`, `exp_RQ2_H21_mid_Cd`, and `exp_RQ2_H21_high_Cd`. No figures are provided for the imposed-flux pathway-isolation experiments or the `cecd` probe.

### 2.4 Experiment–Figure Mapping
Because the Stage-5 figures embed experiment identity directly in their legends, the mapping between analyzed figure curves and the Stage-5 experiment names is unambiguous. The mapping to the Stage-3/Stage-4 planned IDs is only partially defensible.

The following mapping is used in this manuscript.

The Stage-5 **baseline** (`exp_RQ2_H21_baseline`) is treated as equivalent to the planned baseline **`EXP_RQ2_baseline`**, because both correspond to the unmodified axisymmetric hurricane template.

The Stage-5 **low-Cd** case (`exp_RQ2_H21_low_Cd`) is interpreted as a constant-drag reduction experiment comparable in intent to **`EXP_RQ2_001`** (which explicitly sets `cnstcd=0.0005`). This mapping is plausible because both represent reduced drag via a constant-Cd proxy, and the Stage-5 synthesis describes it as “reduced high-wind drag.” Nevertheless, the Stage-5 analysis does not provide the exact `cnstcd` values for the mid/high cases, and it does not indicate that imposed-flux constraints (`set_flx=1`) were applied.

The Stage-5 **mid-Cd** and **high-Cd** cases (`exp_RQ2_H21_mid_Cd` and `exp_RQ2_H21_high_Cd`) do not correspond to any experiment IDs described in the Stage-3/Stage-4 matrix. They are therefore treated as additional Cd sensitivity experiments outside the planned five-experiment set.

Critically, because Stage-5 contains only **interactive-flux** simulations, the strongest causal isolation test proposed in the design—repeating the drag perturbation with **constant imposed SH/LH fluxes**—cannot be evaluated here. The paper therefore tests Hypothesis 2.1 using (i) flux invariance across interactive runs, and (ii) consistency of BL/structural signatures with intensity changes, rather than using a true imposed-flux counterfactual.

## 3. Results

### 3.1 Intensity and Pressure Response (primary test)
Hypothesis 2.1 predicts that changing Cd should produce a robust intensity response that is more readily explained by BL/structural changes than by direct changes in surface enthalpy input. Under a momentum-mediation framing, the largest effects may appear as changes in intensification rate and timing (e.g., delayed or accelerated threshold crossing) and need not imply a large change in the final intensity ceiling.

The Cd sweep shows that **mature intensity is nearly insensitive to Cd**, but the **path to maturity is highly sensitive**.

![intensity_timeseries.png](figures_out/figures/intensity_timeseries.png)

**Figure 1:** Time series of maximum wind speed (m s⁻¹) and minimum surface pressure (hPa) for baseline, low-Cd, mid-Cd, and high-Cd experiments.

Across all Cd levels, storms begin near ~14 m s⁻¹ and ~1008 hPa and converge by ~190 h to peak winds of ~105–110 m s⁻¹ and minimum pressures near ~900 hPa (Fig. 1). In contrast, early intensification differs strongly. The **high-Cd** storm intensifies earliest, reaching ~80 m s⁻¹ by ~75 h, whereas the **low-Cd** storm lags substantially through roughly the first ~130 h before catching up.

The anomaly view highlights the magnitude and reversibility of these timing differences.

![intensity_anomalies.png](figures_out/figures/intensity_anomalies.png)

**Figure 2:** Intensity anomalies relative to baseline (Δwspmax, Δpsfcmin).

Relative to baseline, the high-Cd experiment exhibits early positive wind anomalies up to ~+30 m s⁻¹ (near ~55–65 h) and deeper pressure anomalies of ~−30 hPa (near ~65 h), followed by a later negative phase (~−20 m s⁻¹ near ~110–130 h) as the other storms catch up (Fig. 2). The low-Cd experiment is the mirror image, with early negative wind anomalies reaching ~−38 m s⁻¹ (near ~80 h) and positive pressure anomalies ~+38 hPa (near ~85 h), recovering toward zero late in the simulation. By ~170–190 h, anomalies collapse toward ~0, reinforcing that Cd primarily modulates **intensification timing**, not final intensity.

Timing diagnostics confirm a nearly monotonic ordering of early intensification thresholds with Cd.

![phase_timing_comparison.png](figures_out/figures/phase_timing_comparison.png)

**Figure 3:** Timing of RI onset and time-to-threshold (33/50/70 m s⁻¹), as well as peak-wind and minimum-pressure timing.

The high-Cd storm reaches key intensity thresholds substantially earlier than the baseline, while the low-Cd storm is delayed by tens of hours (Fig. 3). Quantitatively, the baseline reaches 33 m s⁻¹ at ~58 h, 50 m s⁻¹ at ~67 h, and 70 m s⁻¹ at ~80 h, while the low-Cd storm reaches those thresholds at ~79 h, ~96 h, and ~133 h, respectively. Thus, relative to baseline, the low-Cd case is delayed by ~21 h (33 m s⁻¹), ~29 h (50 m s⁻¹), and ~53 h (70 m s⁻¹). Peak intensity timing and minimum-pressure timing are later and closer together across experiments (~153–191 h), consistent with convergence to a common mature intensity.

These results establish the core phenomenology that Hypothesis 2.1 must explain: Cd perturbations generate large, transient intensity differences dominated by timing and rate changes.

### 3.2 Mechanism: boundary-layer and structural mediation
Under Hypothesis 2.1, the drag perturbation should imprint first and most clearly on BL momentum structure (e.g., near-surface vorticity spin-up, RMW contraction, BL depth/jet proxies), and these structural changes should provide a plausible proximate explanation for the transient intensity anomalies.

The BL/structural time series indeed show a coherent ordering aligned with the intensity timing response.

![structure_timeseries.png](figures_out/figures/structure_timeseries.png)

**Figure 4:** Time series of structural metrics including RMW, a PBL-depth proxy, and azimuthal vorticity at multiple heights.

Across all cases, RMW contracts from ~75 km toward ~15–25 km as the storm intensifies (Fig. 4). More importantly for mediation, the timing of low-level vorticity spin-up exhibits the same ordering as intensity: **high-Cd spins up earliest**, baseline and mid-Cd are intermediate, and **low-Cd spins up latest**. The Stage-5 synthesis notes that the structural response “tracks—and appears to lead—the intensity response,” which is consistent with a momentum/structure pathway in which early BL spin-up and contraction precondition later rapid intensification.

Anomaly diagnostics clarify that the structural fields carry a signed perturbation signal coincident with (and potentially preceding) the intensity anomalies.

![structure_anomalies.png](figures_out/figures/structure_anomalies.png)

**Figure 5:** Structural anomalies relative to baseline for RMW, PBL-depth proxy, and vorticity at multiple heights.

The high-Cd experiment shows early positive low-level vorticity anomalies, while the low-Cd experiment shows early negative anomalies that recover later (Fig. 5). RMW anomalies are noisier than vorticity but are broadly consistent with earlier contraction under high-Cd and delayed contraction under low-Cd. This combination—earlier low-level rotation increase and earlier contraction accompanying earlier intensification—supports the interpretation that the drag perturbation manifests first as a **momentum/structure** change that then governs intensification timing.

While these results are consistent with Hypothesis 2.1, the available figures do not provide a formal lead–lag quantification (e.g., cross-correlation or event-based sequencing) sufficient to prove that structural signals systematically precede intensity changes in time; they demonstrate robust co-evolution and consistent ordering across experiments.

### 3.3 Supporting evidence: surface flux invariance and energetic/convective consistency
Hypothesis 2.1 further predicts that surface enthalpy input should not be the primary differentiator across Cd cases. In the strongest form of the hypothesis, intensity should change even when fluxes are held fixed; those imposed-flux experiments are not present in the figure set. Nevertheless, the interactive-flux Cd sweep provides a critical diagnostic: whether surface enthalpy and moisture flux proxies differ enough—and with the appropriate sign and timing—to plausibly drive the observed ~30–40 m s⁻¹ transient intensity differences.

The cumulative surface enthalpy and moisture exchange proxies are nearly invariant across Cd cases.

![surface_flux_timeseries.png](figures_out/figures/surface_flux_timeseries.png)

**Figure 6:** Cumulative surface flux proxies (`esfc` enthalpy; `qsfc` moisture) for all experiments.

Despite the large intensity and timing separation in Figs. 1–3, the `esfc` and `qsfc` curves are nearly coincident throughout the simulation (Fig. 6), with only a slight late reduction in moisture exchange for low-Cd. This near-invariance is difficult to reconcile with a thermodynamic interpretation in which altered surface energy input is the primary driver of the early intensity anomalies.

Flux anomalies relative to baseline further indicate that flux differences are small in fractional terms and appear consistent with being a consequence of circulation differences rather than a cause.

![surface_flux_anomalies.png](figures_out/figures/surface_flux_anomalies.png)

**Figure 7:** Surface-flux anomalies relative to baseline (Δ`esfc`, Δ`qsfc`).

The peak Δ`esfc` is only ~±1×10¹⁸, which corresponds to roughly ~2–3% of the total cumulative enthalpy proxy (~3.8×10¹⁹) (Fig. 7). Moisture-flux anomalies reach ~−8×10⁹ in the low-Cd case (reported as ~9% of total in the Stage-5 synthesis). Notably, the reduced-drag (low-Cd) run tends to have *lower* moisture flux, consistent with weaker winds reducing exchange, i.e., flux anomalies have the sign expected for a feedback *from* intensity rather than a forcing *of* intensity. Given early wind anomalies up to ~±30–40 m s⁻¹ (Fig. 2) but only percent-level enthalpy-exchange differences (Fig. 7), the thermodynamic pathway is not supported as the primary mediator in this figure set.

Energetic and moist-convective diagnostics align with the intensity ordering, consistent with a dynamically mediated timing shift.

![energy_budget_timeseries.png](figures_out/figures/energy_budget_timeseries.png)

**Figure 8:** Time series of energy reservoirs, highlighting kinetic energy evolution across experiments.

Kinetic energy increases with intensification and follows the same ordering as intensity timing (high-Cd earliest, low-Cd delayed) (Fig. 8), while larger internal/potential reservoirs vary weakly. This points to a primary signature in the storm’s dynamical spin-up rather than in a substantially different thermodynamic energy supply.

Moisture conversion and rainfall accumulation similarly track the intensity response, suggesting convective vigor responds to (and reinforces) the evolving circulation structure.

![moisture_budget_timeseries.png](figures_out/figures/moisture_budget_timeseries.png)

**Figure 9:** Vapor mass evolution and accumulated rainfall across experiments.

The low-Cd case retains the most vapor and produces the least accumulated rainfall, while baseline/high-Cd produce more rainfall (Fig. 9). This pattern is consistent with convection being weaker when the storm is dynamically delayed, rather than indicating that suppressed convection via reduced surface enthalpy flux is the initiating mechanism.

Taken together, the combination of (i) strong intensity timing differences, (ii) strong and signed BL/structural anomalies, and (iii) near-invariance of surface enthalpy exchange strongly favors the momentum/structure pathway highlighted in Hypothesis 2.1.

## 4. Discussion
The results **partially support** Hypothesis 2.1. Drag perturbations produced large, transient intensity differences that are best explained by changes in BL momentum structure rather than by changes in surface enthalpy input. Quantitatively, the low-Cd experiment lagged the baseline by ~21 h (33 m s⁻¹), ~29 h (50 m s⁻¹), and ~53 h (70 m s⁻¹), with early intensity anomalies reaching ~−38 m s⁻¹ and ~+38 hPa relative to baseline, while mature intensity converged to ~105–110 m s⁻¹ and ~900 hPa across all cases. Over the same period, surface enthalpy-flux proxy differences were only ~2–3% of cumulative totals, and moisture-flux anomalies were small and consistent with being a response to weaker winds rather than a driver. This evidentiary pattern supports the “momentum/structure mediation” component of the hypothesis.

A physically consistent mechanism chain is suggested by the diagnostics: Cd changes alter near-surface stress and hence BL inflow and the radial distribution of angular momentum, which then modulates the timing of RMW contraction and low-level vorticity spin-up (Figs. 4–5). Earlier vorticity amplification and contraction in high-Cd cases coincide with earlier rapid intensification, while delayed low-level spin-up in low-Cd cases coincides with delayed threshold crossing and reduced rainfall production (Figs. 3, 5, 9). The surface-flux proxies remain nearly coincident across Cd (Fig. 6), implying that the primary pathway is not a direct thermodynamic forcing via substantially changed surface enthalpy input. In this configuration, surface fluxes appear more consistent with a secondary feedback that follows the evolving circulation rather than initiating it.

Several caveats limit the strength of inference regarding the full, causal wording of Hypothesis 2.1. First, the analyzed figure set is a Cd-level sweep with interactive fluxes; it does not include the planned imposed-flux experiments (`set_flx=1`) designed to isolate the thermodynamic pathway. Consequently, “thermodynamic mediation” is assessed indirectly via flux invariance rather than by a controlled counterfactual. Second, the “reduced high-wind drag” concept is represented here by a **constant-Cd proxy** (and in the analyzed set, by unspecified Cd levels), not by a confirmed wind-speed-dependent high-wind drag reduction scheme; this affects how directly the results translate to real high-wind drag rolloff physics. Third, while structural metrics show consistent ordering and strong anomalies, the claim that structural changes occur **before** intensity signals is not formally established with lead–lag statistics in the current diagnostics.

In the context of TC theory, these results are broadly consistent with a view in which the BL acts as an active controller of spin-up and intensification timing, with drag shaping convergence and the localization of angular momentum that supports eyewall contraction and vorticity amplification (e.g., Smith, 2009; Montgomery et al., 2010). At the same time, the near-invariance of surface enthalpy exchange proxies across large intensity timing differences complicates purely thermodynamic explanations in which drag effects are mediated mainly by modified surface heat input (Emanuel, 1986, 1995). The present axisymmetric experiments therefore support a structurally mediated interpretation of drag sensitivity, at least for the transient evolution toward a common mature intensity in this configuration.

## 5. Conclusion
Axisymmetric CM1 experiments spanning baseline, low-, mid-, and high-drag configurations show that varying Cd produces large transient differences in intensification timing but little difference in final intensity. The low-Cd case reached 70 m s⁻¹ at ~133 h compared to ~80 h in the baseline (a delay of ~53 h), with early anomalies as large as ~−38 m s⁻¹ and ~+38 hPa, yet all experiments converged by ~190 h to ~105–110 m s⁻¹ and ~900 hPa.

Diagnostics most directly relevant to Hypothesis 2.1 indicate that BL/structural adjustments are the dominant mediator of these timing differences. Low-level vorticity spin-up and contraction metrics show clear, signed anomalies aligned with intensity timing, while surface enthalpy and moisture flux proxies are nearly invariant across Cd levels and differ only at the few-percent level, with signs consistent with being feedbacks to wind differences. Thus, the evidence supports momentum/structure mediation and renders a surface-enthalpy-forcing interpretation unlikely for the observed transient intensity contrasts.

Future work should (i) rerun or recover the planned imposed-flux experiments to provide a direct thermodynamic-pathway isolation test, (ii) report exact Cd values for all sweep members and confirm whether any high-wind, wind-speed-dependent drag modification is available, and (iii) quantify sequencing with lead–lag analyses (e.g., event detection for RMW contraction and low-level vorticity growth rates relative to intensity-change rates). These steps would convert the present partial support of Hypothesis 2.1 into a more decisive causal attribution.

## Acknowledgments
This manuscript was generated by an AI-assisted analysis pipeline using CM1 experiment outputs and a Stage-5 figure-based synthesis. Researcher validation is required for publication-quality confirmation of configuration details (e.g., exact Cd values for the mid/high cases) and for follow-on controlled experiments (imposed-flux and exchange-coefficient option tests).