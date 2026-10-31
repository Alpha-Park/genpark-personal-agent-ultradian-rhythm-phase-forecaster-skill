# -*- coding: utf-8 -*-
"""
Personal Agent Ultradian Rhythm Phase Forecaster FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentUltradianPhaseForecaster

mcp = FastMCP("genpark-personal-agent-ultradian-rhythm-phase-forecaster-skill")
forecaster = PersonalAgentUltradianPhaseForecaster()

@mcp.tool()
def forecast_ultradian_energy_windows(
    wake_time_hhmm: str = "07:00",
    planned_hours: int = 16
) -> str:
    """
    Forecasts daily 90-minute ultradian energy peaks and recovery troughs.
    """
    res = forecaster.forecast_ultradian_energy_windows(wake_time_hhmm, planned_hours)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_two_process_alertness(
    hours_awake: float,
    baseline_sleep_hours: float = 7.5
) -> str:
    """
    Evaluates net cognitive alertness using Borbely's Two-Process sleep regulation model.
    """
    res = forecaster.evaluate_two_process_alertness(hours_awake, baseline_sleep_hours)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_optimal_nap_window(
    hours_awake: float,
    target_recovery_need: float = 0.70
) -> str:
    """
    Determines optimal restorative nap duration (20-min power nap vs 90-min full cycle) preventing sleep inertia.
    """
    res = forecaster.calculate_optimal_nap_window(hours_awake, target_recovery_need)
    return json.dumps(res, indent=2)

def main():
    print("Testing Ultradian Phase Forecaster FastMCP Server:")
    print(evaluate_two_process_alertness(8.0))

if __name__ == "__main__":
    main()
