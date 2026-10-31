# -*- coding: utf-8 -*-
import json
from client import PersonalAgentUltradianPhaseForecaster

forecaster = PersonalAgentUltradianPhaseForecaster()

print("=" * 64)
print("DEMO: Personal Ultradian Rhythm & Two-Process Sleep Model")
print("=" * 64)

# 1. Forecast 90-min ultradian cycles
cycles = forecaster.forecast_ultradian_energy_windows(wake_time_hhmm="06:30", planned_hours=14)
print(f"\n1. Ultradian Schedule from Wakeup ({cycles['wake_time']}):")
for c in cycles["cycles"][:4]:
    print(f"  Cycle {c['cycle_index']} [{c['window']}]: Peak at {c['peak_phase_time']} (Energy: {c['expected_peak_energy']}) -> {c['recommended_focus']}")

# 2. Evaluate two-process alertness at hour 7
alertness = forecaster.evaluate_two_process_alertness(hours_awake=7.0, baseline_sleep_hours=7.5)
print(f"\n2. Two-Process Alertness (7 Hours Awake):")
print(f"   Process S (Pressure): {alertness['homeostatic_sleep_pressure_s']} | Process C (Circadian): {alertness['circadian_alertness_drive_c']}")
print(f"   Composite Alertness: {alertness['composite_alertness_score']} ({alertness['cognitive_regime']})")

# 3. Prescribe restorative nap
nap = forecaster.calculate_optimal_nap_window(hours_awake=8.5, target_recovery_need=0.65)
print(f"\n3. Nap Prescription:")
print(f"   Recommendation: {nap['recommendation']} ({nap['nap_duration_minutes']} min)")
print(f"   Inertia Risk: {nap['inertia_risk']}")
