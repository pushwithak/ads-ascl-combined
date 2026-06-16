# Image Analysis Report

## Figures (11 total)

### 1. `energy-budget-comparison.png` — _plot_

![energy-budget-comparison.png](https://i.postimg.cc/L5ztYZLS/energy-budget-comparison.png)

**Caption:** Energy budget components (smoothed)

**Description:** Subtype: composite multi-panel line_plot (5 panels), smoothed time series for three experiments.

Overall layout: 2 columns × 3 rows with the bottom-right panel empty; panels labeled ek (top-left), ei (top-right), ep (middle-left), le (middle-right), et (bottom-left). All panels share x-axis model time.

Legend (top-right of figure): three colored lines
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid

Panel ek (top-left):
- y-axis scale indicator shows 1e18; ek increases over time for all runs.
- Baseline (blue): starts near ~0.1×10^18 at 0 h, rises fairly steadily with mild steps/plateaus; by ~200 h reaches ~1.35–1.4×10^18.
- 001 (orange): consistently highest after ~10–20 h; rises in a stepped fashion with noticeable accelerations around ~80–110 h and ~120–160 h; peaks around ~2.45×10^18 near ~170–180 h, ending slightly lower/flat near ~2.4×10^18.
- 002 (green): lowest; increases more slowly; ends near ~0.85–0.9×10^18 by ~200 h.

Panel ei (top-right):
- y-axis scale indicator 1e22; values are nearly flat with small oscillations.
- 002 (green) is highest throughout (~4.095×10^22, small wiggles).
- Baseline (blue) is intermediate (~4.081–4.082×10^22).
- 001 (orange) is lowest (~4.066–4.068×10^22).

Panel ep (middle-left):
- y-axis scale indicator 1e22; nearly constant with small variability.
- 002 (green) highest (~1.493–1.494×10^22) with gentle oscillations.
- Baseline (blue) intermediate (~1.490–1.491×10^22) slowly drifting slightly downward late.
- 001 (orange) lowest (~1.4877–1.4882×10^22) with slight downward drift.

Panel le (middle-right):
- y-axis scale indicator 1e18; values are negative (0 at top, down to about −2.0×10^18).
- All runs drop from near 0 early to negative values, then fluctuate with large oscillations.
- 001 (orange): generally most negative; early drop to about −1.1×10^18 by ~15–20 h; later repeated deep minima, reaching roughly −2.0×10^18 near ~165–175 h; ends around −1.2×10^18.
- Baseline (blue): intermediate negativity; fluctuates roughly between −0.4 and −1.6×10^18; late period includes several dips below −1.2×10^18; ends ~−1.5×10^18.
- 002 (green): often least negative; oscillatory with several near-0 excursions (e.g., around ~95–100 h); typically between ~−0.2 and ~−1.0×10^18; ends near ~−1.0×10^18.

Panel et (bottom-left):
- y-axis scale indicator 1e22; nearly constant.
- 002 (green) highest (~5.588–5.590×10^22).
- Baseline (blue) intermediate (~5.571–5.573×10^22).
- 001 (orange) lowest (~5.554–5.556×10^22).

Caption/title text visible: "Energy budget components (smoothed)"

**Inference:** The three experiments show large separation in kinetic energy (ek) and the le component, while ei/ep/et differ mainly by nearly constant offsets (002 highest, 001 lowest). This pattern suggests the primary experiment-to-experiment differences manifest in dynamically evolving energy components (ek and le) rather than in the nearly steady reservoirs (ei/ep/et). However, the figure alone does not identify what physical parameter differs between EXP_RQ3_H31_001 and _002, so it is not possible to attribute the changes specifically to momentum/drag vs thermodynamic/flux pathways; insufficient context to map these runs to the RQ2 design described.

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Multiple panels: ek (CM1 units) ~0 to 2.5e18; ei (CM1 units) ~4.07e22 to 4.096e22; ep (CM1 units) ~1.487e22 to 1.494e22; le (CM1 units) 0 to −2.0e18; et (CM1 units) ~5.55e22 to 5.59e22

**Legend:**
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid

### 2. `intensity-anomalies.png` — _plot_

![intensity-anomalies.png](https://i.postimg.cc/MHy7MjVH/intensity-anomalies.png)

**Caption:** Δ Maximum wind speed (exp − baseline)

**Description:** Subtype: composite multi-panel line_plot (2 panels), anomalies relative to baseline (exp − baseline).

Top panel title: "Δ Maximum wind speed (exp − baseline)"
- x-axis: Model time (hours), 0 to 200.
- y-axis: Δwspmax (m/s), plotted with a horizontal 0 line; range appears roughly from about −55 to +40 m/s.
- Series:
  - EXP_RQ3_H31_001 — blue: starts near 0; small positive (~+2 to +5 m/s) by ~10–20 h; rises strongly from ~30–60 h to a peak around +35 to +38 m/s near ~55–60 h; then drops rapidly, crossing 0 near ~75 h and reaching a minimum around ~−8 to −10 m/s near ~80 h; rebounds to modest positive (~+5 to +10 m/s) from ~90–140 h; a secondary hump peaks around ~+15 to +17 m/s near ~145 h; trends back toward ~0 by ~175–200 h.
  - EXP_RQ3_H31_002 — orange: near 0 early, then becomes negative by ~10–20 h (~−5 to −10 m/s); continues decreasing, reaching ~−20 m/s near ~60 h; deep minimum around ~−45 to −50 m/s near ~90–105 h; partial recovery to ~−20 to −30 m/s by ~130–150 h; another pronounced dip near ~−45 m/s around ~170 h; ends less negative near ~−12 to −15 m/s by ~195–200 h.

Bottom panel title: "Δ Minimum surface pressure (exp − baseline)"
- x-axis: Model time (hours), 0 to 200.
- y-axis: Δpstcmin (hPa), with horizontal 0 line; range roughly about −35 to +55 hPa.
- Series:
  - EXP_RQ3_H31_001 — blue: near 0 early with small negative (~−2 to −5 hPa); sharp drop starting ~40–50 h reaching minimum ~−30 to −34 hPa near ~55–65 h; rebounds toward ~−5 to −10 hPa by ~80–100 h; then remains negative (typically ~−10 to −20 hPa) through ~160 h with a deeper dip ~−25 to −28 hPa around ~145 h; trends back toward ~−5 to −8 hPa by ~180–200 h.
  - EXP_RQ3_H31_002 — orange: increases positive after early hours; ~+5 to +10 hPa by ~30–50 h; rises to ~+35 to +40 hPa by ~75–85 h; peaks around ~+50 to +52 hPa near ~100–110 h; decreases toward ~+20 to +25 hPa near ~145 h; rises again toward ~+45 to +50 hPa around ~175 h; ends around ~+25 hPa by ~200 h.

Legend visible in each panel lists the two anomaly curves (001 blue, 002 orange).

**Inference:** Relative to baseline, EXP_RQ3_H31_001 intensifies substantially during ~40–70 h (higher maximum winds by ~+35–40 m/s and lower minimum pressure by ~−30 hPa), while EXP_RQ3_H31_002 is persistently weaker (winds down to ~−50 m/s and pressures higher by up to ~+50 hPa). This indicates the perturbations driving 001 and 002 have large, opposite-sign impacts on storm intensity. Without knowing what physical changes define 001 versus 002 (drag, imposed flux, etc.), the figure supports that intensity differences are strong but does not by itself isolate momentum-structure vs thermodynamic mediation (insufficient context for causal pathway attribution).

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Top: Δwspmax (m/s), approx −55 to +40; Bottom: Δpstcmin (hPa), approx −35 to +55

**Legend:**
- EXP_RQ3_H31_001 — blue solid
- EXP_RQ3_H31_002 — orange solid

### 3. `intensity-comparison.png` — _plot_

![intensity-comparison.png](https://i.postimg.cc/3NgX4Dmd/intensity-comparison.png)

**Caption:** Maximum wind speed (smoothed)

**Description:** Subtype: composite multi-panel line_plot (2 panels), smoothed intensity metrics for three experiments.

Top panel title: "Maximum wind speed (smoothed)"
- x-axis: Model time (hours), 0 to 200.
- y-axis: wspmax (m/s), plotted from roughly ~10 to ~110 m/s.
- Series (legend at upper-left):
  - EXP_RQ3_H31_baseline — blue: starts ~14–15 m/s; gradual rise to ~25 m/s by ~40–50 h; rapid intensification ~55–85 h reaching ~70–75 m/s; continues increasing to ~85–90 m/s by ~100–130 h with a slight dip/plateau around ~140–150 h (~mid/high 80s); then increases again to ~105–108 m/s by ~185–195 h.
  - EXP_RQ3_H31_001 — orange: rises earlier and faster than baseline; reaches ~60 m/s by ~50 h and ~70–75 m/s near ~60–65 h; shows a temporary weakening dip to ~63–65 m/s around ~75–80 h; then resumes strengthening to ~90–100 m/s by ~110–140 h; ends slightly above baseline near ~108–110 m/s.
  - EXP_RQ3_H31_002 — green: much weaker for most of the simulation; stays ~15–25 m/s through ~70–80 h; strengthens later to ~60–67 m/s by ~130–150 h; then a weakening/plateau around ~160–175 h with values near ~55–62 m/s; late rapid increase after ~175 h reaching ~90–95 m/s by ~195–200 h.

Bottom panel title: "Minimum surface pressure (smoothed)"
- x-axis: Model time (hours), 0 to 200.
- y-axis: pstcmin (hPa), roughly ~900 to ~1010 hPa.
- Series (legend at upper-right):
  - Baseline (blue): starts ~1008–1010 hPa; slowly decreases to ~995–1000 hPa by ~50–60 h; sharper drop ~60–100 h to ~940 hPa; then gradual decline with pauses/plateaus ~110–160 h (~930–920 hPa); ends near ~900 hPa by ~195–200 h.
  - 001 (orange): deepens earlier; by ~50–60 h reaches ~960 hPa; around ~70 h near ~950–955 hPa (consistent with the wind-speed dip); then continues deepening to ~920 hPa by ~110–120 h; keeps falling to ~905–910 hPa by ~150–170 h; ends lowest near ~895 hPa.
  - 002 (green): remains high pressure longer; stays near ~1000–1005 hPa through ~70–80 h; gradually deepens to ~985–990 hPa by ~100 h; then drops to ~955–960 hPa by ~130–150 h; shows a slight rise/plateau around ~150–175 h (~958–962 hPa); then drops again late, ending near ~925–930 hPa.


**Inference:** EXP_RQ3_H31_001 produces earlier and slightly stronger intensification than baseline (higher winds earlier; lower central pressure earlier and lower final pressure), while EXP_RQ3_H31_002 delays and suppresses intensification for much of the run (higher pressures and lower winds until late). This supports that the experimental perturbations strongly affect both timing (onset) and magnitude of intensity. The plot itself does not specify whether the controlling perturbation is drag/momentum or surface flux/thermodynamics, so it cannot directly test the stated RQ2 pathway hypothesis without additional experiment metadata.

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Top: wspmax (m/s), approx 10 to 110; Bottom: pstcmin (hPa), approx 900 to 1010

**Legend:**
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid

### 4. `moisture-budget-comparison.png` — _plot_

![moisture-budget-comparison.png](https://i.postimg.cc/HnQwc7Xr/moisture-budget-comparison.png)

**Caption:** Moisture species masses (smoothed)

**Description:** Subtype: composite multi-panel line_plot (6 panels), smoothed time series of moisture species masses for three experiments.

Title: "Moisture species masses (smoothed)". Shared x-axis across panels: "Model time (hours)" from 0 to 200.
Legend (top-right of figure):
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid

Panel massqv (top-left):
- y-axis label: massqv (CM1 units) with scale 1e15.
- All runs decrease roughly monotonically.
- Baseline: ~1.09e15 at 0 h to ~1.035e15 at ~200 h.
- 001 (orange): steepest decline; ends near ~1.01e15.
- 002 (green): least decline; remains highest; ends around ~1.06e15.

Panel massqc (top-right):
- y-axis: massqc (CM1 units), scale 1e11.
- Increases with episodic spikes, especially after ~140 h.
- 001 shows the largest spikes, reaching ~3.3–3.5e11 near ~175–180 h.
- Baseline peaks around ~2.0e11 near ~160–170 h.
- 002 generally lower early/mid, rises late; ends near ~2.7e11.

Panel massqr (middle-left):
- y-axis scale 1e11.
- Oscillatory with strong late spikes.
- 001 has highest late spikes, up to ~3.3–3.5e11 around ~165–175 h.
- Baseline peaks around ~2.5–2.7e11 near ~150–190 h with multiple peaks.
- 002 is generally lower, mostly ≤~1.2–1.3e11, with smaller oscillations.

Panel massqi (middle-right):
- y-axis scale 1e10.
- 001 dominates with repeated pulses: peaks near ~3.1e10 around ~75–80 h and again near ~2.8–3.0e10 around ~165–170 h; remains elevated (~1.5–2.0e10) late.
- Baseline rises to ~1.2–1.6e10 with moderate pulses.
- 002 lowest, mostly ~0.5–1.1e10, with intermittent pulses.

Panel massqs (bottom-left):
- y-axis scale 1e11.
- 001 frequently highest with large pulses; peaks near ~2.6e11 around ~120 h.
- Baseline has substantial pulses too, peaking near ~2.2e11 around ~120–135 h.
- 002 shows pronounced oscillations early/mid (including spikes up to ~1.8–2.0e11), then trends downward late, ending near ~0.4–0.5e11.

Panel massqg (bottom-right):
- y-axis scale 1e11.
- 001 has largest episodic spikes: peaks near ~2.6e11 around ~160–170 h; multiple other peaks ~1.5–2.2e11.
- Baseline generally intermediate, ~0.4–1.2e11 late.
- 002 generally lowest; mostly <~0.8e11 and ends near ~0.55–0.6e11.


**Inference:** The experiments differ markedly in condensate partitioning: EXP_RQ3_H31_001 tends to have larger cloud water, rain, ice, snow, and graupel mass peaks (especially late), while EXP_RQ3_H31_002 tends to have reduced hydrometeor masses and retains more vapor (higher massqv). This is consistent with 001 producing a more vigorous/hydrometeor-rich storm and 002 a less vigorous one. However, without knowing whether these runs correspond to drag reductions or flux constraints, this figure cannot by itself separate momentum-mediated versus thermodynamic-mediated mechanisms (insufficient context for pathway attribution).

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Multiple panels: massqv (CM1 units) ~1.01e15 to 1.09e15; massqc (CM1 units) 0 to ~3.5e11; massqr (CM1 units) 0 to ~3.5e11; massqi (CM1 units) 0 to ~3.2e10; massqs (CM1 units) 0 to ~2.7e11; massqg (CM1 units) 0 to ~2.6e11

**Legend:**
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid

### 5. `phase-timing-summary.png` — _plot_

![phase-timing-summary.png](https://i.postimg.cc/rsS10txz/phase-timing-summary.png)

**Caption:** Phase timing metrics (hours; NR = not reached)

**Description:** Subtype: composite multi-panel bar_chart (2 panels), grouped bars by experiment.

Top panel title: "Phase timing metrics (hours; NR = not reached)"
- y-axis: "Time (hours)" from 0 to ~120.
- x-axis categories (rotated labels): EXP_RQ3_H31_baseline, EXP_RQ3_H31_001, EXP_RQ3_H31_002.
- Legend (upper-left):
  - ri_onset_h — blue bars
  - t33_h — orange bars
  - t50_h — green bars
- Approximate values:
  - Baseline: ri_onset_h ~58–60 h; t33_h ~57–58 h; t50_h ~66–68 h.
  - 001: ri_onset_h ~5–7 h; t33_h ~35–37 h; t50_h ~43–45 h.
  - 002: ri_onset_h ~60–62 h; t33_h ~100 h; t50_h ~112–115 h.

Bottom panel title: "Peak intensity (m/s) and timing (hours)"
- y-axis: "Value" from 0 to 200.
- Same x-axis categories as above.
- Legend (upper-left):
  - peak_wspmax_ms — blue bars
  - peak_time_h — orange bars
- Approximate values:
  - Baseline: peak_wspmax_ms ~105 m/s; peak_time_h ~190 h.
  - 001: peak_wspmax_ms ~108 m/s; peak_time_h ~185 h.
  - 002: peak_wspmax_ms ~92–95 m/s; peak_time_h ~190 h.

X-axis label at bottom: "Experiment".

**Inference:** EXP_RQ3_H31_001 reaches key intensity thresholds (ri_onset, t33, t50) much earlier than baseline, whereas EXP_RQ3_H31_002 reaches them much later; peak intensity is slightly higher for 001 and notably lower for 002, while peak timing is similar (~185–190 h) across runs. This supports that the perturbations primarily alter the rate/timing of intensification and attainable peak intensity. The figure does not indicate what physical changes define 001/002, so it cannot directly confirm whether boundary-layer momentum structure changes precede thermodynamic intensity signals (insufficient context for that sequencing claim).

**X-axis:** Experiment categories: EXP_RQ3_H31_baseline, EXP_RQ3_H31_001, EXP_RQ3_H31_002

**Y-axis:** Top: Time (hours), 0 to ~120; Bottom: Value (m/s for peak_wspmax_ms and hours for peak_time_h), 0 to 200

**Legend:**
- ri_onset_h — blue bars
- t33_h — orange bars
- t50_h — green bars
- peak_wspmax_ms — blue bars
- peak_time_h — orange bars

### 6. `rain-train-comparison.png` — _plot_

![rain-train-comparison.png](https://i.postimg.cc/BbxTL1HT/rain-train-comparison.png)

**Caption:** Accumulated rainfall (train)

**Description:** Subtype: line_plot (smoothed/accumulated curve appearance) of accumulated rainfall metric "train" for three experiments.

Title: "Accumulated rainfall (train)"
- x-axis: "Model time (hours)", 0 to 200.
- y-axis: "train (CM1 units)" with scale indicator 1e13; values from ~0 to ~9e13.
- Legend (upper-left):
  - EXP_RQ3_H31_baseline — blue
  - EXP_RQ3_H31_001 — orange
  - EXP_RQ3_H31_002 — green

Curves:
- All are monotonically increasing (accumulation), with varying slope (episodes of faster accumulation).
- 001 (orange): highest accumulation; begins increasing by ~5–10 h; steady rise with slope increases around ~60–80 h and again ~145–170 h; ends near ~8.8–9.0×10^13 by ~195–200 h.
- Baseline (blue): intermediate; ends near ~6.9–7.1×10^13 by ~195–200 h; noticeable slope increases around ~60–80 h and ~145–165 h.
- 002 (green): lowest; more gradual rise throughout; ends near ~4.3–4.5×10^13 by ~195–200 h.


**Inference:** Accumulated rainfall is substantially larger in EXP_RQ3_H31_001 than baseline and much smaller in EXP_RQ3_H31_002, consistent with 001 producing a more productive/convectively active system and 002 a suppressed one over the simulation period. As with intensity, this shows strong sensitivity to the experimental perturbation, but without run metadata it does not isolate whether the rainfall differences arise primarily from momentum/structure changes or from thermodynamic surface-flux changes.

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** train (CM1 units), ~0 to ~9e13 (scale shown as 1e13)

**Legend:**
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid

### 7. `stability-cape-cin-anomalies.png` — _plot_

![stability-cape-cin-anomalies.png](https://i.postimg.cc/brQxD2k9/stability-cape-cin-anomalies.png)

**Caption:** CAPE anomaly (exp − baseline)

**Description:** Subtype: composite multi-panel line_plot (2 panels), anomalies relative to baseline (exp − baseline).

Top panel title: "CAPE anomaly (exp − baseline)"
- x-axis: Model time (hours), 0 to 200.
- y-axis: ΔCAPE (J/kg), with horizontal 0 line; range approx −1100 to +1100 J/kg.
- Series:
  - EXP_RQ3_H31_001 — blue: starts around +650 to +700 J/kg; declines through ~10–35 h, briefly dipping slightly negative around ~35 h (about −100 to −200 J/kg); then sharp increase to ~+900–1000 J/kg near ~45–50 h; dips to ~+350–450 J/kg around ~60–65 h; rises again to around ~+1000–1050 J/kg near ~75–85 h; thereafter remains mostly positive ~+650 to +850 J/kg with a peak near ~+1050 J/kg around ~165 h; ends around ~+650–700 J/kg.
  - EXP_RQ3_H31_002 — orange: mostly negative; starts near ~−650 to −700 J/kg; rises toward less negative values around ~45–50 h (near ~−100 to −200 J/kg); drops back to ~−600 to −700 J/kg around ~55–65 h; rises again toward ~−50 to −150 J/kg near ~70–75 h; then plunges to the minimum near ~−1050 to −1100 J/kg around ~90–95 h; recovers to ~−550 to −700 J/kg for much of ~105–200 h with a brief less-negative bump (~−300 to −400 J/kg) around ~165 h; ends near ~−650 J/kg.

Bottom panel title: "CIN anomaly (exp − baseline)"
- x-axis: Model time (hours), 0 to 200.
- y-axis: ΔCIN (J/kg), with horizontal 0 line; very small range about −0.075 to +0.09 J/kg.
- Series:
  - 001 (blue): starts near ~−0.075 J/kg, rises quickly to ~0 by ~5–10 h; then remains extremely close to 0 with tiny positive deviations (a few thousandths) through ~200 h.
  - 002 (orange): starts near ~+0.09 J/kg, drops rapidly to ~0 by ~5–10 h; then remains essentially at 0 thereafter.

Legends: top-left for CAPE anomaly; top-right for CIN anomaly; both list EXP_RQ3_H31_001 (blue) and EXP_RQ3_H31_002 (orange).

**Inference:** EXP_RQ3_H31_001 has substantially higher CAPE than baseline for most times (often +600 to +1000 J/kg), while EXP_RQ3_H31_002 has substantially lower CAPE than baseline (often −500 to −800 J/kg, with a deep minimum near −1100 J/kg). CIN differences are negligible after the first ~10 hours. This indicates the experiments strongly modulate convective instability primarily through CAPE rather than persistent CIN changes. Whether these CAPE shifts are driven by altered surface fluxes (thermodynamic pathway) or by dynamic/structural changes affecting thermodynamic profiles cannot be determined from this figure alone.

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Top: ΔCAPE (J/kg), approx −1100 to +1100; Bottom: ΔCIN (J/kg), approx −0.075 to +0.09

**Notes:** ΔCIN values are orders of magnitude smaller than typical CIN in J/kg, suggesting either CIN is computed/normalized differently than standard, or the plotted variable is near-zero by construction; units/scale may warrant verification.

**Legend:**
- EXP_RQ3_H31_001 — blue solid
- EXP_RQ3_H31_002 — orange solid

### 8. `stability-cape-cin-comparison.png` — _plot_

![stability-cape-cin-comparison.png](https://i.postimg.cc/3NgX4DmC/stability-cape-cin-comparison.png)

**Caption:** Domain-maximum CAPE

**Description:** Subtype: composite multi-panel line_plot (2 panels), absolute domain-extreme stability metrics.

Top panel title: "Domain-maximum CAPE"
- x-axis: Model time (hours), 0 to 200.
- y-axis: "CAPE (domain max) (J/kg)" from ~2400 to ~5000 J/kg.
- Legend (lower-right):
  - EXP_RQ3_H31_baseline — blue
  - EXP_RQ3_H31_001 — orange
  - EXP_RQ3_H31_002 — green
- Series behavior:
  - 001 (orange): highest throughout; rises quickly from ~3800 at 0 h to ~4600–4700 by ~10 h; fluctuates 4300–4800 mid-run; increases late to near ~4900–5000 around ~150–160 h; slight dip around ~170 h; ends near ~4750–4800.
  - Baseline (blue): intermediate; rises from ~3100 to ~4000 by ~10 h; dips toward ~3500 around ~50 h; deeper dip near ~3200 around ~75 h; recovers to ~4000–4100 by ~120–160 h; ends near ~4050.
  - 002 (green): lowest; starts ~2450, rises to ~3400 by ~10 h; dips to ~3000 around ~60 h; remains ~3100–3500 thereafter with mild variations; ends near ~3400–3450.

Bottom panel title: "Domain-minimum CIN (most negative = strongest inhibition)"
- x-axis: Model time (hours), 0 to 200.
- y-axis: "CIN (domain min) (J/kg)" from 0 to ~5 (ticks at 0–4).
- All three curves nearly overlap: start near ~4.7–4.9 at 0 h, then drop sharply to ~0 by ~6–10 h, remaining at 0 for the remainder of the simulation.
- Legend (upper-right) repeats the three experiments.


**Inference:** Domain-max CAPE is clearly separated among experiments (001 highest, 002 lowest, baseline in between) over nearly the entire simulation, implying systematic differences in instability that likely contribute to different convective vigor and storm evolution. In contrast, the domain-minimum CIN rapidly becomes ~0 for all runs, suggesting that the most inhibited points in the domain lose inhibition early (or CIN is being computed such that minima are clipped at zero). The CAPE separation aligns qualitatively with the intensity differences seen elsewhere, but the mechanism (momentum vs thermodynamic mediation) cannot be concluded from CAPE alone without knowing what was perturbed.

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Top: CAPE (domain max) (J/kg), ~2400 to ~5000; Bottom: CIN (domain min) (J/kg), 0 to ~5

**Notes:** The "domain-minimum CIN" curve is positive and rapidly goes to exactly 0 and stays there, despite the annotation that "most negative" indicates strongest inhibition; this suggests CIN may be plotted as magnitude/absolute value, clipped at 0, or otherwise not following the stated sign convention.

**Legend:**
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid

### 9. `structure-anomalies.png` — _plot_

![structure-anomalies.png](https://i.postimg.cc/2y4QbBhx/structure-anomalies.png)

**Caption:** Δrmw (exp − baseline)

**Description:** Subtype: composite multi-panel line_plot (3 panels), storm-structure metric anomalies relative to baseline (exp − baseline).

Top panel title: "Δrmw (exp − baseline)"
- x-axis: Model time (hours), 0 to 200.
- y-axis: Δrmw (km), roughly −25 to +70 km.
- Series:
  - EXP_RQ3_H31_001 — blue: near 0 early; becomes strongly positive during ~10–30 h (about +20 to +35 km, with a local max near ~+35–40 around ~20–25 h); then decreases and becomes slightly negative (~−5 to −15 km) during ~40–70 h; afterward hovers near small positive values (~0 to +10 km) from ~80–200 h.
  - EXP_RQ3_H31_002 — orange: very large positive anomaly early, peaking about +65–70 km near ~18–22 h; then swings negative, reaching about −15 to −25 km around ~40–55 h; later returns closer to zero with small oscillations, with a notable positive bump near ~+20 km around ~85–90 h and another bump near ~+15–20 km around ~170 h; ends near ~0 to +5 km.

Middle panel title: "Δhpblmax (exp − baseline)"
- y-axis: Δhpblmax (km), roughly −1.4 to +1.0 km.
- 001 (blue): increases from ~0 to ~+0.2 km early; rises to ~+0.8 to +1.0 km around ~50–65 h; dips briefly slightly negative near ~75 h; then stays mostly +0.2 to +0.5 km through ~200 h, with a local peak near ~+0.8 km around ~145 h; ends ~+0.2 km.
- 002 (orange): mostly negative; gradually decreases to ~−0.4 km by ~35–45 h; then drops to around −1.1 to −1.3 km near ~80–100 h; recovers toward ~−0.5 km by ~140 h; dips again near ~−1.1 km around ~150–160 h; ends near ~−0.5 km.

Bottom panel title: "Δzwmax (exp − baseline)"
- x-axis label shown on this panel: "Model time (hours)".
- y-axis: Δzwmax (km AGL), roughly −8 to +8 km.
- Both series are noisy/oscillatory, especially early.
- 001 (blue): early swings include a deep negative near ~−8 km around ~20–25 h, and positive spikes up to ~+7 km near ~25–30 h; after ~80 h anomalies are smaller (typically within about −2 to +2 km) and drift slightly negative late, ending around ~−2 to −3 km.
- 002 (orange): early mostly positive spikes up to ~+6 to +7 km across ~10–80 h; later fluctuations around 0 to +2 km; ends near ~0 to +1 km.

Legends (upper-right of each panel) list EXP_RQ3_H31_001 (blue) and EXP_RQ3_H31_002 (orange).

**Inference:** Compared to baseline, EXP_RQ3_H31_001 tends to have a higher maximum PBL height (positive Δhpblmax) and only modest late-time RMW changes, while EXP_RQ3_H31_002 tends to have a lower maximum PBL height (negative Δhpblmax) and large early-time RMW expansion followed by contraction. These structural shifts occur over the same periods where intensity differences (relative to baseline) are large in other figures, suggesting a linkage between structure and intensity. However, without knowing how 001/002 differ physically (e.g., drag vs flux constraints), this figure alone cannot establish whether momentum/BL-structure changes are the primary mediation pathway.

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Top: Δrmw (km), approx −25 to +70; Middle: Δhpblmax (km), approx −1.4 to +1.0; Bottom: Δzwmax (km AGL), approx −8 to +8

**Legend:**
- EXP_RQ3_H31_001 — blue solid
- EXP_RQ3_H31_002 — orange solid

### 10. `structure-comparison.png` — _plot_

![structure-comparison.png](https://i.postimg.cc/KcLrsCVV/structure-comparison.png)

**Caption:** Storm structure metrics (smoothed)

**Description:** Subtype: composite multi-panel line_plot (3 panels), smoothed storm-structure metrics for three experiments.

Title: "Storm structure metrics (smoothed)". Shared x-axis (bottom panel): "Model time (hours)", 0 to 200.
Legend (top-right of figure):
- EXP_RQ3_H31_baseline — blue
- EXP_RQ3_H31_001 — orange
- EXP_RQ3_H31_002 — green

Top panel (rmw):
- y-axis: rmw (km), ~0 to 80.
- All start near ~75–78 km at 0 h.
- Baseline (blue): sharp drop to near ~0–2 km by ~18–20 h; remains near-zero until ~35–40 h; then increases to ~20–25 km around ~45–60 h; gradually settles around ~18–22 km through ~200 h.
- 001 (orange): drops from ~75 to ~20–25 km by ~20–25 h; then remains mostly ~15–25 km, with a slow upward drift after ~80 h to ~25–27 km by ~150–200 h.
- 002 (green): highly variable early; drops to ~25–30 km by ~20 h but with excursions back upward (~50–70 km) around ~20–30 h; then collapses to near ~0–5 km around ~40–60 h; stays low (~5–15 km) from ~70–165 h; then a late spike up to ~35–40 km near ~170–175 h before returning to ~22–24 km by ~200 h.

Middle panel (hpblmax):
- y-axis: hpblmax (km), ~0.6 to ~3.3 km.
- Baseline (blue): increases from ~0.7 km to ~1.2 km by ~50 h; then rises to ~2.2 km by ~90 h; continues to ~2.9–3.0 km by ~170–190 h.
- 001 (orange): consistently above baseline; rises faster, reaching ~2.0 km by ~50 h and ~2.7–2.9 km by ~100–130 h; peaks around ~3.2–3.3 km near ~180–190 h; slight dip at the end.
- 002 (green): consistently lowest; remains ~0.7–0.9 km through ~70–80 h; then increases steadily to ~1.8–2.1 km by ~140–160 h; ends near ~2.4–2.5 km.

Bottom panel (zwmax):
- y-axis: zwmax (km AGL), 0 to 15.
- All begin near 0 and rapidly increase in the first ~10–20 h.
- Baseline (blue): peaks near ~14 km around ~15–20 h, then drops to ~4–8 km and remains mostly ~5–7 km with mild oscillations, ending ~7–7.5 km.
- 001 (orange): rises to ~6–8 km by ~15–20 h, then peaks around ~12–13 km near ~30–40 h; afterward generally ~5–7 km; ends near ~5–6 km.
- 002 (green): rises to ~10–12 km early; exhibits repeated spikes, including a peak near ~14–15 km around ~70–75 h and additional peaks ~10–12 km around ~80–90 h; later stabilizes around ~6–8 km, ending near ~7.5–8 km.


**Inference:** Across runs, EXP_RQ3_H31_001 maintains a deeper boundary layer (higher hpblmax) and attains comparable or slightly smaller rmw than baseline in the mature stage, while EXP_RQ3_H31_002 has a shallower boundary layer for most times and exhibits more erratic rmw behavior (including early collapse and a late spike). These structural differences are consistent with the intensity ranking seen in the intensity plots (001 stronger/earlier, 002 weaker/delayed), implying structure–intensity coupling. However, the figure does not indicate whether these structural changes are caused by altered surface drag (momentum pathway) or by altered surface energy input (thermodynamic pathway), so it cannot by itself confirm the RQ2 mediation hypothesis.

**X-axis:** Model time (hours), 0 to 200

**Y-axis:** Top: rmw (km), ~0 to 80; Middle: hpblmax (km), ~0.6 to ~3.3; Bottom: zwmax (km AGL), 0 to 15

**Notes:** The baseline rmw collapses to ~0–2 km for an extended period (~20–40 h), which may reflect how rmw is diagnosed (e.g., gridpoint discretization/thresholding) rather than a physically plausible near-zero RMW; worth verifying the rmw calculation and any minimum-radius clipping.

**Legend:**
- EXP_RQ3_H31_baseline — blue solid
- EXP_RQ3_H31_001 — orange solid
- EXP_RQ3_H31_002 — green solid

### 11. `vorticity-levels-comparison.png` — _plot_

![vorticity-levels-comparison.png](https://i.postimg.cc/y69Xr25t/vorticity-levels-comparison.png)

**Caption:** Vorticity time series (levels)

**Description:** Subtype: composite multi-panel line_plot (6 time series panels).

Overall figure title: “Vorticity time series (levels)”. Six panels show vorticity (scaled by ×10^-3 s^-1) at different heights versus model time for three experiments.

Panels (left-to-right, top-to-bottom):
1) “vortsfc” (surface):
- Blue (EXP_RQ3_H31__baseline) rises from ~0 at 0 h to ~5 by ~40–50 h, then rapidly to ~12–14 by ~70–90 h; peaks around ~16–17 near ~100–120 h; stays mostly 14–16 afterward with modest variability through 200 h.
- Orange (EXP_RQ3_H31__001) intensifies earlier: reaches ~5 by ~30–40 h, then jumps to ~12–16 by ~50–70 h (early peak ~16 near ~60 h); afterward oscillates mostly ~11–14 through 200 h.
- Green (EXP_RQ3_H31__002) is delayed early: remains ~0–2 until ~50–60 h, then climbs to ~5–7 by ~80–100 h; surges to ~15–16 around ~115–135 h; then decreases to ~10–12 by ~150–160 h with a pronounced dip to ~6–8 around ~170 h; recovers to ~14–15 by ~190–200 h.

2) “vort1km” (1 km):
- Blue increases from ~0 to ~4–5 by ~35–45 h, then to ~10–13 by ~80–120 h; later reaches the highest values among runs, peaking near ~15 around ~170–185 h, ending ~13–14.
- Orange strengthens earliest, reaching ~10–13 by ~50–70 h; then fluctuates around ~10–12 for most of 80–200 h, ending ~11–12.
- Green stays ~0–2 until ~60–70 h, rises to ~6–8 by ~90–120 h; hovers ~9–10 around ~130–160 h; dips sharply to ~6 near ~175 h; rebounds to ~12–13 by ~190–200 h.

3) “vort2km” (2 km):
- Blue rises to ~4–5 by ~40–50 h, then to ~9–10 by ~70–90 h; thereafter oscillates around ~9–11 through 200 h.
- Orange again leads early, reaching ~9–10 by ~50–60 h; then varies around ~8–10 with intermittent dips (~7–8) and peaks (~10–11), ending ~9–10.
- Green delayed: ~0–1 until ~55–65 h, then increases to ~6–8 by ~90–120 h; remains mostly ~8–10 through ~200 h, with a noticeable drop to ~6–7 around ~165–175 h.

4) “vort3km” (3 km):
- Blue increases to ~4–5 by ~50–60 h, then to ~9–11 by ~90–110 h; declines to ~7–8 around ~130–170 h; re-intensifies to ~9–10 by 200 h.
- Orange rises early to ~9–10 by ~50–60 h; peaks near ~11 around ~100–110 h; then settles ~7–8 from ~120–200 h.
- Green remains ~0–1 until ~60–70 h, then rises steadily to ~6–8 by ~110–130 h; reaches ~10–11 around ~140–160 h (highest in that window), dips to ~5–7 around ~175–185 h, ending ~10.

5) “vort4km” (4 km):
- Blue rises to ~3–4 by ~50–60 h, then peaks around ~10–11 near ~85–95 h; decreases to ~6–7 by ~120–150 h; ends ~7–8.
- Orange jumps early to ~8–9 by ~50–60 h; fluctuates ~6–9 through ~120 h; then trends down to ~6–7 and stays ~6–7 to 200 h.
- Green delayed early (~0–1 until ~60–70 h); climbs to ~5–7 by ~100–120 h; peaks around ~11–12 near ~130–145 h; then declines to ~5–7 by ~160–185 h; rises again to ~10 by 200 h.

6) “vort5km” (5 km):
- Blue rises to ~3–4 by ~50–60 h; peaks around ~10–11 near ~85–95 h; then decreases to ~5–7 by ~120–170 h; modest recovery to ~7–9 by ~185–200 h.
- Orange shows an early step-like increase to ~8–9 near ~50 h; then fluctuates mostly ~6–8 through 200 h, ending ~7.
- Green delayed until ~60–80 h (stays ~0–1), then climbs to ~4–6 by ~100–120 h; peaks near ~11–12 around ~135–150 h; drops to ~5–7 near ~160–185 h; then surges sharply to the largest end value, ~12+ by ~200 h.

Across panels, orange tends to intensify earliest at low/mid levels, blue often attains the largest late-time low-level (1 km) vorticity, and green is generally delayed early but can reach comparable or higher mid–upper-level values later, with notable late-time surges at 4–5 km.

**Inference:** The three experiments produce clearly different timing and vertical distribution of vortex spin-up.

Relative to the blue baseline, the orange run shows earlier vorticity growth across multiple levels (an “early spin-up” signature), while the green run shows delayed development followed by later strengthening and more pronounced variability/secondary maxima at mid–upper levels (especially 4–5 km late in the simulation).

In the context of mechanism testing (momentum/structure vs thermodynamic mediation), this figure mainly supports the idea that the perturbations alter storm structure and its evolution (timing of spin-up and vertical placement of vorticity), not just a uniform intensity shift. However, the figure alone does not isolate whether these structural differences originate from momentum/BL pathway changes or from thermodynamic (flux) changes—additional diagnostics (surface fluxes, BL inflow/jet/RMW, energy budgets) would be needed to attribute causality.

**X-axis:** Model time (hours), ~0 to 200

**Y-axis:** Vorticity at levels (×10^-3 s^-1). Panel-specific ranges visible: vortsfc ~0–18; vort1km ~0–15; vort2km ~0–11; vort3km ~0–11; vort4km ~0–11; vort5km ~0–12.5

**Notes:** Experiment IDs in the legend are labeled “EXP_RQ3_H31__…”, which appears inconsistent with the provided Context focused on RQ2/EXP_RQ2_* experiments; attribution to specific drag/flux perturbations cannot be confirmed from this figure alone.

**Legend:**
- EXP_RQ3_H31__baseline — blue solid
- EXP_RQ3_H31__001 — orange solid
- EXP_RQ3_H31__002 — green solid
