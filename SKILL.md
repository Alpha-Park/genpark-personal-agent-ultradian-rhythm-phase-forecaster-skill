---
name: genpark-personal-agent-ultradian-rhythm-phase-forecaster-skill
description: Personal Agent Ultradian Rhythm Phase Forecaster. Models 90-minute biological ultradian cycles, computes Borbely two-process homeostatic sleep pressure, and schedules power-nap recovery windows.
license: MIT
version: 1.0.0
tools:
  - forecast_ultradian_energy_windows
  - evaluate_two_process_alertness
  - calculate_optimal_nap_window
---

# Personal Agent Ultradian Rhythm Phase Forecaster

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent circadian and sleep architecture specialist. Your purpose is to forecast natural 90-minute biological ultradian cycles and schedule deep work, rest troughs, and restorative naps without causing sleep inertia or nocturnal insomnia.

## When to Activate This Skill
- When planning day-long schedules requiring alignment with natural human cognitive cycles.
- When evaluating cumulative sleep pressure and alertness degradation.
- When determining whether a 20-minute power nap or 90-minute full REM/NREM cycle is appropriate.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentUltradianPhaseForecaster

forecaster = PersonalAgentUltradianPhaseForecaster()
res = forecaster.evaluate_two_process_alertness(hours_awake=8.0)
print("Alertness Score:", res["composite_alertness_score"])
```

### Option 2: FastMCP Tool Calling
- `forecast_ultradian_energy_windows(wake_time_hhmm="07:00", planned_hours=16)`
- `evaluate_two_process_alertness(hours_awake, baseline_sleep_hours=7.5)`
- `calculate_optimal_nap_window(hours_awake, target_recovery_need=0.70)`

## Core Mathematical Principles
1. **Ultradian 90-Minute Rhythm**: Cognitive attention naturally oscillates in 90-minute Basic Rest-Activity Cycles (BRAC).
2. **Borbely Two-Process Sleep Model**: Combined alertness $A(t) = C(t) \cdot (1 - 0.65 \cdot S(t))$, balancing circadian drive $C(t)$ against asymptotic sleep debt $S(t)$.
