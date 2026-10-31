# genpark-personal-agent-ultradian-rhythm-phase-forecaster-skill

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Personal Agent Ultradian Rhythm Phase Forecaster models 90-minute human biological oscillations and Borbely's classic Two-Process Sleep Regulation framework to predict alertness peaks, post-prandial energy dips, and optimal nap durations.

```mermaid
flowchart TD
    A[Wakeup Time & Planned Active Hours] --> B[90-Minute BRAC Cycle Harmonic Decomposer]
    B --> C[Peak Synthesis Windows & Trough Recovery Times]
    D[Hours Awake & Sleep Baseline] --> E[Two-Process S & C Alertness Model]
    E --> F[Net Cognitive Alertness & Fatigue Regime]
    F --> G[Sleep-Inertia-Free Nap Duration Prescriber]
```

## Features
- **90-Minute Cycle Decomposition**: Maps continuous workdays into biological basic rest-activity cycles.
- **Borbely Two-Process Sleep Pressure**: Models homeostatic sleep debt accumulation vs circadian phase drive.
- **Sleep Inertia Prevention**: Strictly guides naps to 20 minutes (pre-SWS) or 90 minutes (full cycle).

## Quickstart

```python
from client import PersonalAgentUltradianPhaseForecaster

forecaster = PersonalAgentUltradianPhaseForecaster()
res = forecaster.forecast_ultradian_energy_windows("07:00", 12)
print("First Peak Window:", res["cycles"][0]["peak_phase_time"])
```

## FastMCP Integration

```bash
python -m genpark-personal-agent-ultradian-rhythm-phase-forecaster-skill.mcp_server
```

## License
MIT
