# Image Analysis Report

## Figures (11 total)

### 1. `energy-budget-comparison.png` — _plot_

![energy-budget-comparison.png](https://i.postimg.cc/L5ztYZLS/energy-budget-comparison.png)

**Caption:** Energy budget components (smoothed)

**Description:** Subtype: composite multi-panel line_plot (5 subplots) comparing smoothed energy budget components across three experiments.

Overall layout/title: “Energy budget components (smoothed)”. Shared x-axis is model time in hours (0–200) for all panels. Each panel has its own y-axis label (CM1 units) and scientific-notation scale indicator.

Legend (upper-right of the full figure):
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

Panel details:
1) Top-left: ek
- y-axis label: “ek (CM1 units)”, scale 1e18; visible range ~0 to 2.5×10^18.
- All three series increase overall (nonlinear, with step-like accelerations).
- Orange (001) is highest throughout after early times: starts near ~0.1×10^18 and rises strongly, reaching ~2.0×10^18 by ~130 h and ~2.4–2.5×10^18 by ~170–190 h (slight plateau/undulations late).
- Blue (baseline) increases more moderately: ends around ~1.4×10^18 by ~190 h.
- Green (002) is lowest: ends around ~0.9×10^18 by ~190 h.

2) Top-right: ei
- y-axis label: “ei (CM1 units)”, scale 1e22; values clustered near ~4.07–4.10×10^22.
- Series are nearly flat with small oscillations.
- Green (002) highest near ~4.095–4.096×10^22; blue (baseline) near ~4.081–4.082×10^22; orange (001) lowest near ~4.067–4.069×10^22.

3) Middle-left: ep
- y-axis label: “ep (CM1 units)”, scale 1e22; visible range ~1.488 to 1.494×10^22.
- Nearly constant with tiny undulations.
- Green (002) highest (~1.493–1.494×10^22), blue intermediate (~1.490–1.491×10^22), orange lowest (~1.4877–1.4883×10^22).

4) Middle-right: le
- y-axis label: “le (CM1 units)”, scale 1e18; visible range ~−2.0×10^18 to 0.
- All series quickly drop below 0 early and then oscillate strongly (non-monotonic).
- Orange (001) tends to be most negative, with repeated deep troughs; reaches roughly ~−1.9 to −2.0×10^18 near ~175–185 h.
- Blue (baseline) is intermediate, often between ~−0.5 and ~−1.6×10^18, with several sharp dips late.
- Green (002) is generally least negative (closer to 0), often ~−0.3 to ~−1.1×10^18, but still oscillatory.

5) Bottom-left: et
- y-axis label: “et (CM1 units)”, scale 1e22; values near ~5.555–5.590×10^22.
- Nearly flat with small waviness.
- Green (002) highest (~5.588–5.589×10^22), blue (~5.571–5.573×10^22), orange lowest (~5.555–5.557×10^22).

No sixth panel is shown; the bottom-right slot is empty in the layout.

**Inference:** Across experiments, total/internal/potential energy (et/ei/ep) show small, largely time-invariant offsets, while kinetic energy (ek) diverges strongly (001 highest, 002 lowest). This pattern is more consistent with a primarily dynamical/momentum-structure pathway affecting storm intensity (changes manifesting as large kinetic-energy differences) than with a dominant thermodynamic-energy-input change that would visibly reshape total/internal energy time evolution.

However, the figure does not display surface enthalpy flux components directly, so it cannot by itself isolate momentum vs thermodynamic mediation; it mainly indicates that the experiments’ main energetic separation appears in kinetic energy and in the oscillatory “le” term.

**X-axis:** Model time (hours), 0–200

**Y-axis:** Varies by subplot (CM1 units): ek ~0–2.5×10^18; ei ~4.067–4.096×10^22; ep ~1.488–1.494×10^22; le ~−2.0–0×10^18; et ~5.555–5.590×10^22

**Notes:** Experiment labels reference “RQ3_H31” (not RQ2), so mapping from these curves to the stated drag/flux pathway-separation design is not explicit in the figure.

**Legend:**
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

### 2. `intensity-anomalies.png` — _plot_

![intensity-anomalies.png](https://i.postimg.cc/MHy7MjVH/intensity-anomalies.png)

**Caption:** Δ Maximum wind speed (exp − baseline)

Δ Minimum surface pressure (exp − baseline)

**Description:** Subtype: composite multi-panel line_plot (2 stacked panels) showing intensity anomalies (experiment minus baseline) versus time.

Overall titles:
- Top: “Δ Maximum wind speed (exp − baseline)”
- Bottom: “Δ Minimum surface pressure (exp − baseline)”

x-axis (both panels): Model time (hours), 0–200.

Top panel (Δwspmax):
- y-axis label: “Δwspmax (m/s)”; visible range about −50 to +40; horizontal black zero line.
- Blue (EXP_RQ3_H31_001): starts near 0, becomes positive by ~10 h. Rises to a broad maximum around +35 to +38 m/s near ~55–65 h. Then drops sharply, briefly negative (around −5 to −10 m/s) near ~75–80 h. After ~85 h remains mostly positive (~+3 to +12 m/s) with a secondary peak ~+15–17 m/s near ~140–150 h, then trends toward ~0 by ~185–200 h.
- Orange (EXP_RQ3_H31_002): quickly becomes negative and stays negative most of the run. Reaches about −45 to −50 m/s near ~75–105 h (deep minimum around ~95–105 h). Recovers somewhat to ~−20 to −25 m/s around ~135–150 h, then dips again to roughly ~−45 m/s near ~170–175 h, ending around ~−10 to −15 m/s by ~195–200 h.

Bottom panel (Δpstcmin):
- y-axis label: “Δpstcmin (hPa)”; visible range about −35 to +55; horizontal black zero line.
- Blue (EXP_RQ3_H31_001): predominantly negative (lower minimum pressure than baseline). Drops to ~−30 to −35 hPa near ~50–65 h. Then rebounds toward ~−5 to −15 hPa around ~80–110 h, with another more negative episode (~−25 to −30 hPa) near ~140–155 h, ending around ~−5 to −10 hPa.
- Orange (EXP_RQ3_H31_002): predominantly positive (higher minimum pressure than baseline). Climbs steadily to ~+35 to +40 hPa by ~75–85 h, peaks around ~+50 to +55 hPa near ~100–110 h, then declines to ~+20 hPa near ~140–150 h. Rises again to ~+45 to +50 hPa near ~170–175 h, ending around ~+25 hPa.

Legend:
- EXP_RQ3_H31_001 — blue
- EXP_RQ3_H31_002 — orange

**Inference:** Relative to the baseline, experiment 001 produces a substantially stronger storm for an extended period (up to ~+35–38 m/s stronger peak winds and ~30+ hPa deeper minimum pressure around ~50–65 h), while experiment 002 produces a much weaker storm (up to ~−50 m/s and ~+50 hPa anomalies).

For the momentum-vs-thermodynamic mediation framing, these anomalies establish that the perturbations drive very large intensity differences. The figure alone does not identify whether the perturbation is drag, flux, or another control, so it cannot attribute causality. It does, however, provide a clear target interval (~40–110 h, plus a late-time weakening in 002) where boundary-layer structural diagnostics should be examined to test whether structural changes precede and plausibly mediate the intensity divergence.

**X-axis:** Model time (hours), 0–200

**Y-axis:** Top: Δwspmax (m/s), ~−50 to +40; Bottom: Δpstcmin (hPa), ~−35 to +55

**Notes:** Experiment naming (“RQ3_H31”) is inconsistent with the provided RQ2 context; the figure does not specify what physical parameter differs between 001 and 002.

**Legend:**
- EXP_RQ3_H31_001 — blue
- EXP_RQ3_H31_002 — orange

### 3. `intensity-comparison.png` — _plot_

![intensity-comparison.png](https://i.postimg.cc/3NgX4Dmd/intensity-comparison.png)

**Caption:** Maximum wind speed (smoothed)

Minimum surface pressure (smoothed)

**Description:** Subtype: composite multi-panel line_plot (2 stacked panels) comparing smoothed intensity metrics across three experiments.

Overall titles:
- Top: “Maximum wind speed (smoothed)”
- Bottom: “Minimum surface pressure (smoothed)”

Shared x-axis: Model time (hours), 0–200.

Legend (top panel):
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

Top panel (wspmax):
- y-axis label: “wspmax (m/s)”; visible range ~10 to ~110.
- All start near ~14–15 m/s.
- Orange (001) intensifies earliest and fastest: reaches ~25 m/s by ~20 h, ~60 m/s by ~50 h, peaks around ~75 m/s near ~65 h, dips slightly (~65 m/s) near ~75 h, then resumes strengthening to ~90 m/s by ~105 h and ~100–110 m/s by ~150–200 h. Ends around ~107–110 m/s.
- Blue (baseline) intensifies later than 001: remains ~20–30 m/s through ~50–60 h, then rises rapidly to ~60–70 m/s by ~75–85 h, then ~85–95 m/s by ~110–140 h. Shows a modest mid/late wobble (slight dip around ~140–150 h) before rising again to ~105–110 m/s by ~180–200 h.
- Green (002) is much weaker for most of the run: stays ~15–22 m/s through ~80 h, then strengthens to ~45 m/s by ~105 h and ~60–67 m/s by ~130–150 h. It weakens slightly (~55–60 m/s) around ~160–175 h, then re-intensifies sharply late to ~90–95 m/s by ~190–200 h.

Bottom panel (pstcmin):
- y-axis label: “pstcmin (hPa)”; visible range ~900 to ~1010 hPa.
- All start near ~1008–1010 hPa and decrease over time.
- Orange (001) drops earliest and deepest: ~975 hPa by ~50 h, ~950–955 hPa by ~65–75 h, then continues to ~920 hPa by ~120 h and ~895–900 hPa by ~190–200 h.
- Blue (baseline) drops more slowly: ~990 hPa by ~60 h, ~955 hPa by ~85–90 h, ~935–940 hPa by ~110–120 h, and ~900 hPa by ~190–200 h.
- Green (002) remains highest pressure (weakest) for most of the simulation: stays near ~1000 hPa through ~70–80 h, then declines to ~990 hPa around ~90–110 h, ~955–960 hPa by ~130–150 h, shows a modest rise/plateau (~960–965 hPa) around ~155–175 h, then drops late to ~925–930 hPa by ~190–200 h.

**Inference:** Experiment 001 yields earlier rapid intensification and a stronger storm (higher max winds and lower min pressure) than the baseline, while experiment 002 substantially delays and suppresses intensification for ~150+ hours, with late re-intensification.

In the context of testing whether drag changes act primarily through boundary-layer momentum structure, this figure provides timing: the 001–baseline divergence begins very early (~10–30 h) and becomes large by ~40–70 h, which is consistent with the idea that structural/momentum-field changes could precede mature intensity differences. The figure does not diagnose surface enthalpy flux, so it cannot directly separate momentum vs thermodynamic mediation; it must be combined with structure/flux diagnostics.

**X-axis:** Model time (hours), 0–200

**Y-axis:** Top: wspmax (m/s), ~10–110; Bottom: pstcmin (hPa), ~900–1010

**Notes:** None.

**Legend:**
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

### 4. `moisture-budget-comparison.png` — _plot_

![moisture-budget-comparison.png](https://i.postimg.cc/HnQwc7Xr/moisture-budget-comparison.png)

**Caption:** Moisture species masses (smoothed)

**Description:** Subtype: composite multi-panel line_plot (6 subplots; 3 rows × 2 columns) of smoothed total moisture-species masses over time for three experiments.

Overall title: “Moisture species masses (smoothed)”. Shared x-axis across panels: “Model time (hours)”, 0–200.

Legend (upper-right of the full figure):
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

Panels:
1) massqv (top-left)
- y-axis label: “massqv (CM1 units)”, scale 1e15.
- All decrease over time (gradual, slightly wavy).
- By ~190–200 h: orange (001) lowest (~1.01×10^15), blue baseline mid (~1.035×10^15), green (002) highest (~1.06×10^15).

2) massqc (top-right)
- y-axis label: “massqc (CM1 units)”, scale 1e11.
- Starts near 0 and generally increases with strong variability/spikes, especially after ~130 h.
- Orange (001) shows the largest late spikes (peaks roughly ~3.0–3.5×10^11 around ~170–185 h).
- Blue and green rise more moderately but still spike late; end values near ~2.5–2.8×10^11.

3) massqr (middle-left)
- y-axis label: “massqr (CM1 units)”, scale 1e11.
- Oscillatory with upward tendency; large late spikes.
- Orange (001) has the largest peaks (up to ~3.5×10^11 around ~165–175 h).
- Baseline (blue) reaches ~2.0–2.6×10^11 in late spikes.
- Green (002) remains comparatively lower (often ~0.5–1.2×10^11), with smaller peaks.

4) massqi (middle-right)
- y-axis label: “massqi (CM1 units)”, scale 1e10.
- Oscillatory; increases from near 0 early.
- Orange (001) consistently highest with repeated peaks (~2–3×10^10; a maximum around ~3.0×10^10 near ~130–150 h).
- Baseline (blue) intermediate (~0.5–1.6×10^10).
- Green (002) generally lowest (~0.3–1.2×10^10).

5) massqs (bottom-left)
- y-axis label: “massqs (CM1 units)”, scale 1e11.
- Strong oscillations/episodes.
- Orange (001) tends to be largest with multiple peaks around ~2.0–2.7×10^11 (notably ~110–140 h).
- Baseline (blue) peaks around ~2.0–2.3×10^11.
- Green (002) peaks near ~1.8–2.0×10^11 earlier, then trends downward and ends much lower (~0.4–0.6×10^11).

6) massqg (bottom-right)
- y-axis label: “massqg (CM1 units)”, scale 1e11.
- Highly spiky.
- Orange (001) has the largest spikes (up to ~2.5–2.7×10^11 around ~150–170 h).
- Baseline (blue) typically ~0.5–1.2×10^11 with smaller spikes.
- Green (002) generally lowest, ending near ~0.5–0.7×10^11.

**Inference:** The stronger-intensity experiment (001, per the intensity figures) also exhibits systematically larger condensed/precipitating hydrometeor masses (qc/qr/qi/qs/qg) and greater variability/spikiness, while the weaker experiment (002) tends to have reduced hydrometeor masses and retains higher vapor mass (qv). This aligns with a more vigorous storm producing more condensate/precipitation and depleting vapor.

For the momentum-vs-thermodynamic mediation question, these differences indicate that microphysical/moisture fields strongly covary with intensity, but they do not identify whether the primary driver is altered boundary-layer momentum structure or altered surface enthalpy flux. They are consistent with intensity changes being accompanied by broader thermodynamic/hydrometeor adjustments (likely downstream effects).

**X-axis:** Model time (hours), 0–200

**Y-axis:** Varies by subplot (CM1 units): massqv ~1.01–1.09×10^15; massqc/massqr/massqs/massqg ~0–3.5×10^11; massqi ~0–3×10^10

**Notes:** None.

**Legend:**
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

### 5. `phase-timing-summary.png` — _plot_

![phase-timing-summary.png](https://i.postimg.cc/rsS10txz/phase-timing-summary.png)

**Caption:** Phase timing metrics (hours; NR = not reached)

Peak intensity (m/s) and timing (hours)

**Description:** Subtype: composite (2 stacked bar_chart panels) summarizing timing metrics and peak intensity/timing for three experiments.

Top panel title: “Phase timing metrics (hours; NR = not reached)”
- y-axis: “Time (hours)”, range ~0 to ~120.
- Categories on x-axis (rotated labels): EXP_RQ3_H31_baseline, EXP_RQ3_H31_001, EXP_RQ3_H31_002.
- Legend entries:
  - ri_onset_h — blue
  - t33_h — orange
  - t50_h — green
- Approximate bar values:
  - EXP_RQ3_H31_baseline: ri_onset_h ~59–60 h; t33_h ~57–58 h; t50_h ~67 h.
  - EXP_RQ3_H31_001: ri_onset_h ~5–7 h; t33_h ~35 h; t50_h ~44–45 h.
  - EXP_RQ3_H31_002: ri_onset_h ~60–61 h; t33_h ~100 h; t50_h ~115 h.

Bottom panel title: “Peak intensity (m/s) and timing (hours)”
- y-axis label: “Value”, range ~0 to ~200 (note: mixes units).
- Same three experiment categories.
- Legend entries:
  - peak_wspmax_ms — blue
  - peak_time_h — orange
- Approximate bar values:
  - EXP_RQ3_H31_baseline: peak_wspmax_ms ~105 m/s; peak_time_h ~190 h.
  - EXP_RQ3_H31_001: peak_wspmax_ms ~108 m/s; peak_time_h ~185–188 h.
  - EXP_RQ3_H31_002: peak_wspmax_ms ~92–95 m/s; peak_time_h ~190–192 h.

**Inference:** Experiment 001 reaches “RI onset” and intensity thresholds much earlier than baseline (ri_onset ~6 h vs ~60 h; t33/t50 also earlier), while experiment 002 delays threshold attainment substantially (t33 ~100 h; t50 ~115 h) and achieves a lower peak wind speed.

For Hypothesis 2.1 (structural/momentum changes preceding thermodynamic intensity signals), the timing separation suggests that the controlling perturbation in 001 impacts storm evolution almost immediately, consistent with a fast-acting dynamical pathway (e.g., boundary-layer momentum/structure) rather than a slow cumulative thermodynamic pathway—though the figure does not directly show the sequencing of boundary-layer structure relative to these timing metrics. The summary motivates checking early-time (first ~0–20 h) boundary-layer structural diagnostics in 001.

**X-axis:** Experiment category (EXP_RQ3_H31_baseline / _001 / _002)

**Y-axis:** Top: Time (hours), ~0–120; Bottom: Value (mixed units: m/s and hours), ~0–200

**Notes:** Bottom panel y-axis mixes two different physical units (m/s and hours) on the same numeric axis, which can be visually misleading.

**Legend:**
- ri_onset_h — blue bars
- t33_h — orange bars
- t50_h — green bars
- peak_wspmax_ms — blue bars (bottom panel)
- peak_time_h — orange bars (bottom panel)

### 6. `rain-train-comparison.png` — _plot_

![rain-train-comparison.png](https://i.postimg.cc/BbxTL1HT/rain-train-comparison.png)

**Caption:** Accumulated rainfall (train)

**Description:** Subtype: line_plot of accumulated rainfall metric (“train”) versus time for three experiments.

Title: “Accumulated rainfall (train)”.

x-axis: “Model time (hours)”, 0–200.

y-axis: “train (CM1 units)”, scale 1e13; visible range ~0 to ~9×10^13.

Legend:
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

Trends:
- All series are monotonically increasing from near 0, with slope changes (steeper accumulation periods) but no decreases.
- Orange (001) accumulates the most throughout after early times: by ~100 h it is ~3.5×10^13, by ~150 h ~6.0×10^13, ending near ~8.8–9.0×10^13 at ~190–200 h.
- Blue (baseline) is intermediate: ~2.5×10^13 at ~100 h, ~4.6×10^13 at ~150 h, ending ~6.8–7.0×10^13.
- Green (002) is lowest: ~1.8×10^13 at ~100 h, ~3.2×10^13 at ~150 h, ending ~4.3–4.5×10^13.

**Inference:** The experiment with strongest storm intensity (001 in the intensity figures) also produces the largest accumulated rainfall, while the weaker experiment (002) produces the least. This is consistent with storm intensity changes being associated with a substantially altered hydrological output.

This figure does not distinguish whether rainfall differences arise from momentum/structure changes or thermodynamic surface-input changes; it mainly confirms that the perturbations materially change integrated precipitation, making rainfall a useful downstream metric to compare against boundary-layer structural diagnostics.

**X-axis:** Model time (hours), 0–200

**Y-axis:** train (CM1 units), ~0–9×10^13

**Notes:** None.

**Legend:**
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

### 7. `stability-cape-cin-anomalies.png` — _plot_

![stability-cape-cin-anomalies.png](https://i.postimg.cc/brQxD2k9/stability-cape-cin-anomalies.png)

**Caption:** CAPE anomaly (exp − baseline)

CIN anomaly (exp − baseline)

**Description:** Subtype: composite multi-panel line_plot (2 stacked panels) showing CAPE and CIN anomalies (experiment minus baseline) for two experiments.

Top title: “CAPE anomaly (exp − baseline)”
- x-axis: Model time (hours), 0–200.
- y-axis: “ΔCAPE (J/kg)”, visible range about −1200 to +1200; horizontal zero line.
- Blue (EXP_RQ3_H31_001): mostly positive. Starts ~+650–700 J/kg, declines to near 0 and briefly negative (~−100 to −200) around ~35–40 h, then jumps to ~+900–1000 near ~45–55 h. Peaks ~+1050 around ~70–80 h. Thereafter stays broadly +600 to +900 with oscillations; another peak near ~+1100 around ~165–170 h; ends ~+650–700.
- Orange (EXP_RQ3_H31_002): mostly negative. Begins ~−650 to −700, rises toward near-zero but still negative (~−100) around ~45–50 h, drops back to ~−600 to −700 around ~55–65 h, rises again toward ~−50 to −150 near ~70–75 h, then plunges to a strong minimum around ~−1100 near ~90–95 h. After ~100 h it remains around ~−500 to −750 with a brief weakening of negativity (~−300) near ~160–165 h; ends ~−600 to −650.

Bottom title: “CIN anomaly (exp − baseline)”
- x-axis: Model time (hours), 0–200.
- y-axis: “ΔCIN (J/kg)”, visible range about −0.075 to +0.09; horizontal zero line.
- Blue (EXP_RQ3_H31_001): starts near ~−0.075 at 0 h, rapidly approaches 0 by ~5 h, then stays very close to 0 with tiny positive excursions (~0.001–0.005) through ~70 h; essentially 0 thereafter.
- Orange (EXP_RQ3_H31_002): starts near ~+0.085 at 0 h, rapidly approaches 0 by ~5 h, then remains essentially 0 for the rest of the run (minor wiggles). 

Legends:
- Top panel legend (upper-left): EXP_RQ3_H31_001 (blue), EXP_RQ3_H31_002 (orange)
- Bottom panel legend (upper-right): same entries.

**Inference:** Experiment 001 has substantially higher CAPE than baseline for most of the simulation (positive ΔCAPE), while experiment 002 has lower CAPE (negative ΔCAPE), with ΔCIN differences collapsing to near zero after the first few hours.

This suggests that the perturbations strongly modulate convective instability (CAPE) in a manner consistent with the intensity differences (001 stronger, 002 weaker), but inhibition (CIN) is not a persistent differentiator after spin-up. For the momentum-vs-thermodynamic mediation hypothesis, persistent CAPE changes could reflect altered thermodynamic sourcing/mixing or storm structure; without corresponding surface enthalpy flux or boundary-layer convergence diagnostics, the figure alone cannot establish whether CAPE changes are cause or consequence of structural/momentum changes.

**X-axis:** Model time (hours), 0–200

**Y-axis:** Top: ΔCAPE (J/kg), ~−1200 to +1200; Bottom: ΔCIN (J/kg), ~−0.075 to +0.09

**Notes:** The ΔCIN axis is extremely small compared to typical CIN magnitudes; after ~5 h both series sit essentially at 0, so interpretability of CIN differences is limited by scale/resolution.

**Legend:**
- EXP_RQ3_H31_001 — blue
- EXP_RQ3_H31_002 — orange

### 8. `stability-cape-cin-comparison.png` — _plot_

![stability-cape-cin-comparison.png](https://i.postimg.cc/3NgX4DmC/stability-cape-cin-comparison.png)

**Caption:** Domain-maximum CAPE

Domain-minimum CIN (most negative = strongest inhibition)

**Description:** Subtype: composite multi-panel line_plot (2 stacked panels) comparing domain-extreme CAPE and CIN across three experiments.

Top panel title: “Domain-maximum CAPE”
- x-axis: Model time (hours), 0–200.
- y-axis: “CAPE (domain max) (J/kg)”, visible range ~2400 to ~5000.
- Orange (EXP_RQ3_H31_001) highest throughout: starts ~3800, spikes to ~4600–4700 by ~10 h, dips to ~3800–3900 around ~40–45 h, then climbs and remains ~4600–4900 from ~90 h onward, peaking near ~4950 around ~150–160 h; ends ~4700–4800.
- Blue (baseline) intermediate: starts ~3100, rises to ~4000 near ~10 h, fluctuates (notably a dip to ~3500 around ~50 h and a deeper dip to ~3200 around ~70–80 h), then returns to ~3900–4100 after ~110 h; ends near ~4050.
- Green (EXP_RQ3_H31_002) lowest: starts ~2450, rises to ~3400 by ~10 h, then oscillates ~3000–3500, with dips near ~2950–3050 around ~55–65 h and ~90–100 h; ends near ~3400–3450.

Bottom panel title: “Domain-minimum CIN (most negative = strongest inhibition)”
- x-axis: Model time (hours), 0–200.
- y-axis: “CIN (domain min) (J/kg)”, visible range 0 to ~5.
- All three experiments start near ~4.7–4.9 at 0 h, drop sharply to ~0 by ~5–8 h, and then remain at 0 for essentially the entire remainder of the simulation; lines overlap.

Legend (both panels):
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

**Inference:** Domain-maximum CAPE differs substantially among experiments (001 >> baseline >> 002) throughout most of the run, consistent with a systematic change in the thermodynamic environment or storm-induced thermodynamic extremes. In contrast, the plotted “domain-minimum CIN” collapses to ~0 very early and ceases to discriminate experiments.

For RQ2/Hypothesis 2.1, the strong and persistent CAPE separation could be interpreted as a thermodynamic pathway signal, but because it is a domain-maximum metric it may also respond to structural/dynamical changes (e.g., storm organization affecting localized buoyancy extremes). The absence of sustained CIN separation suggests inhibition is not the controlling thermodynamic limiter here (at least as represented by this plotted metric).

**X-axis:** Model time (hours), 0–200

**Y-axis:** Top: CAPE (domain max) (J/kg), ~2400–5000; Bottom: CIN (domain min) (J/kg), ~0–5

**Notes:** Despite the label “most negative = strongest inhibition,” the CIN axis is plotted as nonnegative and rapidly becomes identically ~0 for all runs, suggesting either (a) CIN is plotted with sign flipped/absolute value, (b) a floor/clipping at 0, or (c) a diagnostic/aggregation issue.

**Legend:**
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

### 9. `structure-anomalies.png` — _plot_

![structure-anomalies.png](https://i.postimg.cc/2y4QbBhx/structure-anomalies.png)

**Caption:** Δrmw (exp − baseline)

Δhpblmax (exp − baseline)

Δzwmax (exp − baseline)

**Description:** Subtype: composite multi-panel line_plot (3 stacked panels) showing storm-structure metric anomalies (experiment minus baseline) for two experiments.

Shared x-axis: “Model time (hours)”, 0–200.

Top panel title: “Δrmw (exp − baseline)”
- y-axis label: “Δrmw (km)”, visible range about −25 to +70; horizontal zero line.
- Blue (EXP_RQ3_H31_001): early positive anomaly grows to ~+30 to +35 km around ~15–25 h. Drops toward 0 around ~35–45 h, then becomes slightly negative (~−10 to −15 km) near ~55–70 h. After ~80 h stays modestly positive (~+3 to +10 km) through ~180 h, ending around a few km positive.
- Orange (EXP_RQ3_H31_002): larger early expansion: rises to ~+60 to +70 km around ~20–25 h, then falls sharply to negative values (~−15 to −25 km) around ~40–55 h. Recovers toward 0 by ~90–110 h, stays slightly negative (~−5 to −10) through ~150–165 h, then spikes positive (~+15–20 km) around ~170–175 h, ending near ~0 to +5.

Middle panel title: “Δhpblmax (exp − baseline)”
- y-axis label: “Δhpblmax (km)”, visible range about −1.3 to +1.0; horizontal zero line.
- Blue (001): increases from ~0 to ~+0.2 early, then rises to a broad maximum ~+0.9 to +1.0 km around ~50–65 h. Drops rapidly toward 0 around ~75 h, then remains positive ~+0.2 to +0.4 for much of ~85–160 h, with a secondary bump near ~+0.8 around ~145–150 h; ends around ~+0.2.
- Orange (002): predominantly negative. Drifts from ~0 to ~−0.3 by ~30–40 h, then falls further to ~−1.1 to −1.3 km around ~80–95 h. Recovers to ~−0.5 to −0.6 by ~130–145 h, dips again to ~−1.1 around ~155–165 h, ending near ~−0.5.

Bottom panel title: “Δzwmax (exp − baseline)”
- y-axis label: “Δzwmax (km AGL)”, visible range about −8 to +8; horizontal zero line.
- Blue (001): very noisy early with swings from about −7 km (near ~10–15 h) to +7 km (near ~25–30 h). After ~60–80 h variability damps and stays near 0 (roughly between −1 and +2), trending slightly negative (about −1 to −2) by ~180–200 h.
- Orange (002): also highly variable, with many positive excursions. Reaches ~+6 to +8 km around ~60–85 h. Later remains around 0 to +3 km with intermittent small negatives; ends near ~0 to +1.

Legends (each panel, upper-right):
- EXP_RQ3_H31_001 — blue
- EXP_RQ3_H31_002 — orange

**Inference:** Both experiments show substantial early structural departures from baseline (especially Δrmw within ~10–30 h and Δhpblmax by ~30–70 h). Notably, experiment 001 (the stronger-intensity case in the intensity plots) corresponds to a higher boundary-layer height maximum (positive Δhpblmax up to ~+1 km) and early RMW expansion relative to baseline, while experiment 002 (weaker-intensity case) shows reduced boundary-layer height (negative Δhpblmax down to ~−1.2 km) and large early RMW changes.

This timing—structural anomalies appearing early, before/while the largest intensity differences emerge—supports the plausibility of Hypothesis 2.1’s “structural response precedes intensity signal” concept. The figure still does not distinguish whether the structural changes are driven by momentum (drag) changes versus thermodynamic flux changes, because the perturbation identity is not encoded here.

**X-axis:** Model time (hours), 0–200

**Y-axis:** Top: Δrmw (km), ~−25 to +70; Middle: Δhpblmax (km), ~−1.3 to +1.0; Bottom: Δzwmax (km AGL), ~−8 to +8

**Notes:** None.

**Legend:**
- EXP_RQ3_H31_001 — blue
- EXP_RQ3_H31_002 — orange

### 10. `structure-comparison.png` — _plot_

![structure-comparison.png](https://i.postimg.cc/KcLrsCVV/structure-comparison.png)

**Caption:** Storm structure metrics (smoothed)

**Description:** Subtype: composite multi-panel line_plot (3 stacked panels) comparing smoothed storm-structure metrics across three experiments.

Overall title: “Storm structure metrics (smoothed)”. Shared x-axis: “Model time (hours)”, 0–200.

Legend (upper-right of the full figure):
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

Panel 1 (top): rmw
- y-axis label: “rmw (km)”, visible range ~0 to ~80.
- All start near ~75 km.
- Baseline (blue): drops rapidly to near ~0 by ~18–20 h and stays near 0 until ~35–40 h, then increases to ~20–25 km by ~45–60 h. Thereafter fluctuates mostly ~15–22 km, with a gentle rise to ~22–24 km late (~150–200 h).
- Exp 001 (orange): drops from ~75 to ~20–30 km by ~20–30 h; then remains mostly ~15–25 km and slowly increases, reaching ~25–27 km by ~150–200 h.
- Exp 002 (green): highly variable early; after initial drop to ~25–30 km by ~15–20 h it spikes back upward (peaks ~60–70 km around ~25–30 h), then plunges to very small rmw (~0–5 km) around ~40–55 h. Later it stays around ~5–15 km through ~90–150 h, then shows a prominent late spike (~35–40 km around ~165–175 h) and ends near ~22–23 km.

Panel 2 (middle): hpblmax
- y-axis label: “hpblmax (km)”, visible range ~0.6 to ~3.3.
- All rise over time but differ in magnitude.
- Exp 001 (orange) is highest much of the run: rises from ~0.7 to ~2.0 km by ~50 h, ~2.7–3.0 km by ~110–150 h, peaking around ~3.2–3.3 km near ~170–185 h.
- Baseline (blue) is intermediate: rises from ~0.7 to ~1.2 km by ~50 h, ~2.4–2.6 km by ~110–140 h, and ~2.9–3.0 km late.
- Exp 002 (green) is lowest: stays ~0.8–1.0 km through ~80–90 h, then increases to ~1.5–2.0 km by ~120–150 h and ends near ~2.4–2.5 km.

Panel 3 (bottom): zwmax
- y-axis label: “zwmax (km AGL)”, visible range ~0 to ~15.
- All start near 0 and rise quickly to high values early, then settle.
- Baseline (blue): peaks around ~13–14 km near ~15–20 h, drops to ~4–7 km by ~25–40 h, then oscillates ~4–8 km for the remainder, ending ~7 km.
- Exp 001 (orange): peaks around ~12–13 km near ~30–40 h, then generally sits slightly lower than baseline late (~5–7 km), ending near ~5–6 km.
- Exp 002 (green): most variable, with several large mid-period peaks (up to ~14–15 km around ~65–75 h and additional peaks ~10–12 km around ~80–90 h). Late values are ~6–8 km, ending near ~7–8 km.

**Inference:** Structural metrics separate the experiments in ways that mirror the intensity differences: experiment 001 (stronger storm) tends to have a deeper boundary layer (higher hpblmax) and relatively larger/steadier rmw after early adjustment, while experiment 002 (weaker storm for most of the run) has a shallower boundary layer and more erratic rmw evolution (including periods of extremely small rmw and later spikes).

For Hypothesis 2.1, the key supportive element is that pronounced structural differences (rmw/hpblmax/zwmax behavior) emerge early and persist, providing a credible mechanism by which a momentum-related perturbation (e.g., altered drag) could mediate intensity outcomes. This figure alone cannot demonstrate that structural changes occur *before* thermodynamic intensity signals in a causal sequence, but it shows that structure is strongly modulated across experiments and therefore is a viable mediation pathway to test.

**X-axis:** Model time (hours), 0–200

**Y-axis:** Top: rmw (km), ~0–80; Middle: hpblmax (km), ~0.6–3.3; Bottom: zwmax (km AGL), ~0–15

**Notes:** None.

**Legend:**
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

### 11. `vorticity-levels-comparison.png` — _plot_

![vorticity-levels-comparison.png](https://i.postimg.cc/y69Xr25t/vorticity-levels-comparison.png)

**Caption:** Vorticity time series (levels)

**Description:** Subtype: composite multi-panel line_plot (six time series panels).

Overall layout: 3 rows × 2 columns of line plots titled “Vorticity time series (levels)”. Each panel shows vorticity (scaled by ×10^-3 s^-1) versus model time (hours), for three experiments.

Legend (top-right of the full figure):
- EXP_RQ3_H31_baseline — blue solid line
- EXP_RQ3_H31_001 — orange solid line
- EXP_RQ3_H31_002 — green solid line

Common x-axis: Model time (hours), spanning 0 to 200 (ticks shown at ~0, 50, 100, 150, 200). Curves begin near ~0 vorticity at t=0 in all panels.

Panel-by-panel description:

1) Top-left: “vortsfc” (surface vorticity)
- y-axis label: vortsfc (×10^-3 s^-1). Visible range approximately 0 to ~18.
- Blue (baseline): gradual rise to ~5 by ~40–45 h; sharp intensification to ~12–14 by ~70–80 h; peaks around ~16–17 near ~100–115 h; then fluctuates mostly ~13–16 through 200 h with intermittent dips (e.g., ~12–13 around ~130–150 h) and a late value near ~15.
- Orange (001): fastest early spin-up: rises to ~5 by ~30–35 h, then steeply to ~12 by ~45–50 h; peaks near ~16 around ~60 h; then drops to ~9–10 around ~75–80 h; recovers and oscillates ~11–15 through ~100–130 h; after ~130 h stays relatively steady ~11–13 to 200 h.
- Green (002): slowest early growth: remains ~0–2 until ~50–60 h; increases to ~5–7 by ~80–95 h; sharp jump to ~14–16 around ~105–125 h (briefly comparable to or exceeding blue); then declines markedly after ~140 h, reaching a minimum near ~6–7 around ~165–175 h; rebounds to ~13–15 by ~185–200 h.

2) Top-right: “vort1km”
- y-axis label: vort1km (×10^-3 s^-1). Visible range approximately 0 to ~15.
- Blue: rises to ~4–5 by ~35–45 h; brief plateau/dip ~4–5 around ~45–60 h; strong increase to ~11–13 by ~85–110 h; continues upward with fluctuations, reaching ~14–15 around ~170–185 h; ends near ~13–14 by 200 h.
- Orange: early rapid rise; reaches ~10–12 by ~55–70 h; oscillates ~9–13 from ~70 to ~140 h; then trends slightly downward/stable around ~10–12 to 200 h.
- Green: delayed rise; stays near ~0–2 until ~60–70 h; increases to ~6–8 by ~90–110 h; reaches ~10–11 by ~120–150 h; pronounced dip to ~6 around ~165–175 h; rebounds to ~12–13 by ~190–200 h.

3) Middle-left: “vort2km”
- y-axis label: vort2km (×10^-3 s^-1). Visible range approximately 0 to ~11.
- Blue: increases to ~4–5 by ~40–50 h; climbs to ~9–10 by ~75–90 h; peaks near ~10.5–11 around ~110–130 h; then oscillates ~9–10.5 through 200 h.
- Orange: fastest early growth; reaches ~9–10 by ~50–60 h; dips to ~7–8 around ~70–80 h; then oscillates ~8–10.5 through 200 h, with a late dip near ~8 around ~175–185 h before returning toward ~9–10 by 200 h.
- Green: delayed; remains ~0–1.5 until ~60–70 h; rises to ~6–7 by ~95–115 h; reaches ~9–10 by ~120–140 h; then declines to ~6 around ~160–170 h; recovers to ~9–10 by ~185–200 h.

4) Middle-right: “vort3km”
- y-axis label: vort3km (×10^-3 s^-1). Visible range approximately 0 to ~11.
- Blue: gradual increase to ~4–5 by ~60–70 h; sharp rise to ~9–10 by ~90–105 h; then decreases to ~7–8 around ~120–150 h; modest recovery to ~9–10 by ~190–200 h.
- Orange: early rise to ~9–10 by ~55–65 h; peaks near ~10–11 around ~95–105 h; then declines to ~6.5–8 by ~120–160 h; ends around ~7.5–8 by 200 h.
- Green: delayed; stays ~0–1 until ~60–70 h; rises steadily to ~6–7 by ~100–115 h; peaks/plateaus around ~10–11 from ~130–150 h (highest during that interval); then drops to ~5–6 around ~175–185 h; rebounds to ~10 by 200 h.

5) Bottom-left: “vort4km”
- y-axis label: vort4km (×10^-3 s^-1). Visible range approximately 0 to ~11.
- Blue: increases to ~3–4 by ~50 h; sharp rise to ~9–11 by ~80–95 h (peak near ~10–11); then declines to ~6–7 around ~120–150 h; slight recovery to ~7.5–8.5 by ~185–200 h.
- Orange: early jump to ~8.5–9.5 by ~50–55 h; then fluctuates broadly ~6–9 through ~60–120 h; gradually settles lower ~6–7 after ~130 h; ends near ~6.5–7 by 200 h.
- Green: delayed rise; remains ~0–1 until ~70 h; climbs to ~5–6 by ~95–105 h; peaks near ~10.5–11 around ~125–135 h; then drops to ~6–7 around ~150–180 h; ends near ~10 at 200 h.

6) Bottom-right: “vort5km”
- y-axis label: vort5km (×10^-3 s^-1). Visible range approximately 0 to ~12.5.
- Blue: rises to ~3–4 by ~55–65 h; sharp rise to ~9–10.5 by ~85–95 h (peak ~10–10.5); then declines to ~5.5–7 by ~120–150 h; slight recovery to ~7–8.5 by ~175–200 h.
- Orange: early rise; reaches ~8–9.5 by ~50–55 h; then oscillates ~5.5–8.5 through 200 h; ends near ~7.
- Green: delayed; stays ~0–1 until ~70–80 h; rises to ~4–6 by ~95–115 h; peaks near ~11.5–12 around ~130–140 h; declines to ~5–7 around ~155–180 h; then strong late increase, ending near the top of the axis (~12–12.5) at ~200 h.

Cross-panel patterns:
- EXP_RQ3_H31_001 (orange) generally shows the earliest intensification across levels (notably before ~60–70 h), but tends to level off or remain lower than blue/green later in the simulation.
- EXP_RQ3_H31_002 (green) shows delayed development (often until ~70–100 h) followed by pronounced mid/upper-level peaks around ~125–145 h and a notable dip around ~160–180 h across several levels, then late recovery (especially strong at 5 km).
- Baseline (blue) typically intensifies after orange but earlier than green, with comparatively sustained vorticity at later times, especially at 1 km and surface.

**Inference:** This figure compares how the vertical vorticity structure evolves over time across three experiments. The main implication is that the experiments differ strongly in *timing* and *vertical distribution* of spin-up: EXP_RQ3_H31_001 spins up earliest at all levels but does not maintain the highest late-time vorticity, whereas EXP_RQ3_H31_002 spins up later yet can achieve comparable or higher vorticity aloft (3–5 km) during ~125–145 h and again near the end (notably at 5 km). Baseline tends to be more steadily strong at low levels later (surface/1 km). 

Relative to a generic null hypothesis of “no structural differences among experiments,” the clear separations in onset time, peak timing, and level-dependent strength reject H0 and indicate that the perturbations substantially alter the storm’s dynamical core evolution. However, connecting these differences specifically to the RQ2 momentum-vs-thermodynamic mediation hypothesis is not possible from this figure alone because the experiment labels shown are RQ3_H31 and no drag/flux or boundary-layer/enthalpy-flux diagnostics are displayed here.

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Varies by panel: vortsfc/vort1km/vort2km/vort3km/vort4km/vort5km (×10^-3 s^-1); approximate ranges: vortsfc 0–18, vort1km 0–15, vort2km 0–11, vort3km 0–11, vort4km 0–11, vort5km 0–12.5

**Notes:** Experiment names in the legend reference “EXP_RQ3_H31_*”, which does not match the provided RQ2 experiment matrix naming; figure-to-experiment mapping may be inconsistent with the surrounding context.

**Legend:**
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid
