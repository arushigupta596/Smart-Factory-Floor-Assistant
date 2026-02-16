"""
Factory data access tools for Smart Factory Floor Assistant
ADK-compatible tool functions - uses docstrings for tool discovery
"""

import json
from pathlib import Path
from typing import Dict, List, Any


# Data directory path
DATA_DIR = Path(__file__).parent.parent / "data"


def load_json_data(filename: str) -> Dict[str, Any]:
    """Load JSON data from the data directory"""
    filepath = DATA_DIR / filename
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": f"Data file {filename} not found"}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON in {filename}"}


# === PRODUCTION TOOLS ===

def get_production_status(line_id: str = "all") -> dict:
    """
    Returns current production status including OEE percentage, units produced, shift target, and active alarms for one or all production lines. Use line_id='all' for overview or specify line e.g. 'Line_3' for detail.
    
    Args:
        line_id: Production line identifier ('Line_1', 'Line_2', 'Line_3', 'Line_4') or 'all' for all lines
    
    Returns:
        Dictionary with production line status data
    """
    data = load_json_data("production_lines.json")
    
    if "error" in data:
        return data
    
    if line_id == "all":
        return {"production_lines": data, "total_lines": len(data)}
    
    if line_id in data:
        return {"line": data[line_id]}
    
    return {"error": f"Line {line_id} not found. Available lines: {', '.join(data.keys())}"}


def get_active_alarms() -> list:
    """
    Returns a list of all currently active machine alarms and lines that are down. Use this to get a quick overview of all production issues on the floor right now.
    
    Returns:
        List of active alarms with line_id, alarm_code, status, and units_lost
    """
    data = load_json_data("production_lines.json")
    
    if "error" in data:
        return [data]
    
    active_alarms = []
    
    for line_id, line_data in data.items():
        if line_data["status"] == "DOWN" or line_data["active_alarm"] is not None:
            units_lost = line_data["shift_target"] - line_data["units_produced"]
            active_alarms.append({
                "line_id": line_id,
                "alarm_code": line_data["active_alarm"],
                "status": line_data["status"],
                "units_produced": line_data["units_produced"],
                "shift_target": line_data["shift_target"],
                "units_lost": units_lost,
                "oee": line_data["oee"],
                "operator": line_data["operator_name"]
            })
    
    return active_alarms


# === MAINTENANCE TOOLS ===

def get_fault_details(error_code: str) -> dict:
    """
    Looks up an error code and returns the full fault details including root cause, recommended corrective action, safety precautions, required parts, and SOP reference number. Use this when a machine shows an error code.
    
    Args:
        error_code: Machine error code (e.g., 'E-412', 'E-201')
    
    Returns:
        Dictionary with complete fault diagnostic information
    """
    data = load_json_data("machine_faults.json")
    
    if "error" in data:
        return data
    
    if error_code in data:
        return {"fault": data[error_code]}
    
    available_codes = ', '.join(data.keys())
    return {"error": f"Error code {error_code} not found. Available codes: {available_codes}"}


def get_maintenance_history(machine_id: str) -> dict:
    """
    Returns the maintenance history for a specific machine including all past maintenance events, dates, technicians, parts replaced, and costs. Also returns summary statistics. Use machine IDs like M-07, C-2, P-01.
    
    Args:
        machine_id: Machine identifier (e.g., 'M-07', 'M-03', 'M-11', 'C-2', 'C-4', 'P-01')
    
    Returns:
        Dictionary with maintenance history and summary statistics
    """
    data = load_json_data("maintenance_history.json")
    
    if "error" in data:
        return data
    
    if machine_id not in data:
        available_machines = ', '.join(data.keys())
        return {"error": f"Machine {machine_id} not found. Available machines: {available_machines}"}
    
    history = data[machine_id]
    
    # Calculate summary statistics
    total_events = len(history)
    last_maintenance_date = history[0]["date"] if history else None
    emergency_count = sum(1 for event in history if event["type"] == "EMERGENCY")
    total_cost = sum(event["cost_usd"] for event in history)
    
    return {
        "machine_id": machine_id,
        "maintenance_history": history,
        "summary": {
            "total_events": total_events,
            "last_maintenance_date": last_maintenance_date,
            "emergency_count": emergency_count,
            "total_cost_usd": total_cost
        }
    }


# === QUALITY TOOLS ===

def get_quality_summary(batch_id: str = "current_shift") -> dict:
    """
    Returns quality inspection results including defect count, defect rate, top defect types, and disposition recommendation (RELEASE/REWORK/SCRAP/REVIEW) for a specific batch or the current shift overall. Use batch IDs like B-2041 or 'current_shift' for shift summary.
    
    Args:
        batch_id: Batch identifier (e.g., 'B-2040', 'B-2041', etc.) or 'current_shift' for overall shift summary
    
    Returns:
        Dictionary with quality data and disposition information
    """
    data = load_json_data("quality_logs.json")
    
    if "error" in data:
        return data
    
    if batch_id == "current_shift":
        return {"shift_summary": data["current_shift"]}
    
    if batch_id in data.get("batches", {}):
        return {"batch": data["batches"][batch_id]}
    
    available_batches = ', '.join(data.get("batches", {}).keys())
    return {"error": f"Batch {batch_id} not found. Available batches: {available_batches}"}


# === COMPREHENSIVE REPORTING TOOL ===

def get_shift_performance_report() -> dict:
    """
    Generates a comprehensive shift performance report combining production and quality data. Returns overall attainment percentage, average OEE across all lines, quality summary, and a list of critical issues requiring attention. Use this for end-of-shift reviews or management briefings.
    
    Returns:
        Dictionary with complete shift performance metrics and critical issues
    """
    prod_data = load_json_data("production_lines.json")
    quality_data = load_json_data("quality_logs.json")
    
    if "error" in prod_data:
        return prod_data
    if "error" in quality_data:
        return quality_data
    
    # Production metrics
    lines_running = sum(1 for line in prod_data.values() if line["status"] == "RUNNING")
    lines_down = sum(1 for line in prod_data.values() if line["status"] == "DOWN")
    
    total_units_produced = sum(line["units_produced"] for line in prod_data.values())
    total_shift_target = sum(line["shift_target"] for line in prod_data.values())
    
    average_oee = sum(line["oee"] for line in prod_data.values()) / len(prod_data)
    overall_attainment_pct = (total_units_produced / total_shift_target * 100) if total_shift_target > 0 else 0
    
    # Identify critical issues
    critical_issues = []
    for line_id, line_data in prod_data.items():
        if line_data["oee"] < 70:
            critical_issues.append({
                "type": "LOW_OEE",
                "line_id": line_id,
                "oee": line_data["oee"],
                "message": f"{line_id} OEE at {line_data['oee']}% (Critical - below 70%)"
            })
        
        if line_data["active_alarm"]:
            critical_issues.append({
                "type": "ACTIVE_ALARM",
                "line_id": line_id,
                "alarm_code": line_data["active_alarm"],
                "status": line_data["status"],
                "message": f"{line_id} has active alarm {line_data['active_alarm']} - Status: {line_data['status']}"
            })
    
    return {
        "shift_performance": {
            "lines_running": lines_running,
            "lines_down": lines_down,
            "average_oee": round(average_oee, 1),
            "total_units_produced": total_units_produced,
            "total_shift_target": total_shift_target,
            "overall_attainment_pct": round(overall_attainment_pct, 1)
        },
        "quality_summary": quality_data.get("current_shift", {}),
        "critical_issues": critical_issues
    }
