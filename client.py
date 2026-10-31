# -*- coding: utf-8 -*-
"""
Personal Agent Ultradian Rhythm Phase Forecaster Client
Zero-dependency 90-minute harmonic cycle decomposition, two-process sleep-wakefulness
alertness forecaster, and restorative power-nap window calculator.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentUltradianPhaseForecaster:
    """
    Forecasts biological ultradian 90-minute oscillation phases, Borbely two-process
    sleep pressure, and optimal power-nap opportunities.
    """

    def forecast_ultradian_energy_windows(
        self,
        wake_time_hhmm: str = "07:00",
        planned_hours: int = 16
    ) -> Dict[str, Any]:
        """
        Decomposes daily wakefulness into 90-minute ultradian cycles with peak and trough phases.
        Cycle phase: t_phase = (t_hours * 60) % 90.
        """
        try:
            parts = wake_time_hhmm.strip().split(":")
            wake_hour = int(parts[0])
            wake_minute = int(parts[1])
        except:
            wake_hour, wake_minute = 7, 0

        wake_total_minutes = wake_hour * 60 + wake_minute
        cycles = []
        total_cycles = planned_hours * 60 // 90

        for c_idx in range(total_cycles):
            c_start_min = wake_total_minutes + (c_idx * 90)
            c_peak_min = c_start_min + 45
            c_end_min = c_start_min + 90

            start_str = f"{(c_start_min // 60) % 24:02d}:{c_start_min % 60:02d}"
            peak_str = f"{(c_peak_min // 60) % 24:02d}:{c_peak_min % 60:02d}"
            end_str = f"{(c_end_min // 60) % 24:02d}:{c_end_min % 60:02d}"

            # Subjective energy rating based on time of day (post-wake boost, post-lunch dip, evening resurgence)
            mid_hour = (c_peak_min / 60.0) % 24.0
            circadian_mod = math.sin((mid_hour - 6.0) * math.pi / 12.0) - 0.25 * math.cos((mid_hour - 14.0) * math.pi / 6.0)
            base_energy = round(max(0.20, min(0.98, 0.60 + 0.35 * circadian_mod)), 2)

            cycles.append({
                "cycle_index": c_idx + 1,
                "window": f"{start_str} - {end_str}",
                "peak_phase_time": peak_str,
                "trough_phase_time": end_str,
                "expected_peak_energy": base_energy,
                "recommended_focus": "DEEP_SYNTHESIS" if base_energy >= 0.75 else ("MODERATE_COMMUNICATION" if base_energy >= 0.50 else "RECOVERY_AND_REFLECT")
            })

        return {
            "wake_time": wake_time_hhmm,
            "planned_hours": planned_hours,
            "total_ultradian_cycles": len(cycles),
            "cycles": cycles,
            "highest_energy_cycle": max(cycles, key=lambda c: c["expected_peak_energy"])
        }

    def evaluate_two_process_alertness(
        self,
        hours_awake: float,
        baseline_sleep_hours: float = 7.5
    ) -> Dict[str, Any]:
        """
        Borbely Two-Process Model:
        Process S (Homeostatic sleep pressure): S(t) = 1 - (1 - S0) * exp(-t / 18.2)
        Process C (Circadian alertness): C(t) = 0.5 + 0.45 * sin(2*pi*(t - 2)/24)
        Alertness = C(t) * (1 - 0.7 * S(t))
        """
        t = max(0.0, float(hours_awake))
        s0 = max(0.05, min(0.40, 1.0 - (baseline_sleep_hours / 8.0) * 0.9))
        process_s = round(1.0 - (1.0 - s0) * math.exp(-t / 18.2), 3)

        # Circadian phase oscillation
        process_c = round(0.5 + 0.45 * math.sin(2.0 * math.pi * (t - 2.0) / 24.0), 3)

        # Combined net cognitive alertness (0.0 to 1.0)
        net_alertness = round(max(0.05, min(1.0, process_c * (1.0 - 0.65 * process_s))), 3)

        if net_alertness >= 0.70:
            regime = "PEAK_COGNITIVE_ALERTNESS"
        elif net_alertness >= 0.45:
            regime = "STABLE_MAINTENANCE"
        elif net_alertness >= 0.25:
            regime = "ELEVATED_SLEEP_PRESSURE_DIP"
        else:
            regime = "CRITICAL_FATIGUE_TERMINATION"

        return {
            "hours_awake": t,
            "homeostatic_sleep_pressure_s": process_s,
            "circadian_alertness_drive_c": process_c,
            "composite_alertness_score": net_alertness,
            "cognitive_regime": regime,
            "optimal_for_complex_decisions": net_alertness >= 0.60
        }

    def calculate_optimal_nap_window(
        self,
        hours_awake: float,
        target_recovery_need: float = 0.70
    ) -> Dict[str, Any]:
        """
        Determines whether user should take a 15-20 min power nap or 90 min full cycle nap.
        Prevents sleep inertia by strictly avoiding slow-wave awakening (between 30 and 70 minutes).
        """
        t = max(0.0, float(hours_awake))
        need = max(0.1, min(1.0, target_recovery_need))

        if t < 6.0 and need < 0.50:
            return {
                "recommendation": "NAP_NOT_RECOMMENDED",
                "nap_duration_minutes": 0,
                "rationale": "Insufficient sleep pressure; nap will disrupt subsequent nocturnal sleep latency."
            }

        # If high sleep debt and afternoon window: 90-min full cycle
        if need >= 0.80 or t >= 10.0:
            return {
                "recommendation": "FULL_ULTRADIAN_CYCLE_NAP",
                "nap_duration_minutes": 90,
                "sleep_stages_covered": "NREM1, NREM2, SWS (Deep), and REM",
                "inertia_risk": "LOW (Awakening at natural cycle completion)",
                "expected_alertness_boost_pct": 45.0
            }
        else:
            return {
                "recommendation": "STAGE_2_POWER_NAP",
                "nap_duration_minutes": 20,
                "sleep_stages_covered": "Light NREM1 and NREM2 sleep spindle consolidation",
                "inertia_risk": "VERY_LOW (Terminates strictly before slow-wave delta sleep onset)",
                "expected_alertness_boost_pct": 25.0
            }
