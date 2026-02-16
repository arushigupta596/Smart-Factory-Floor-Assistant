#!/usr/bin/env python3
"""
Quick test to verify all tools and agents are working
"""

from factory_agent import tools

print("=" * 60)
print("TESTING SMART FACTORY FLOOR ASSISTANT")
print("=" * 60)

# Test 1: Production Status
print("\n1️⃣  Testing get_production_status('all')...")
result = tools.get_production_status("all")
print(f"✅ Found {result['total_lines']} production lines")

# Test 2: Active Alarms
print("\n2️⃣  Testing get_active_alarms()...")
alarms = tools.get_active_alarms()
print(f"✅ Found {len(alarms)} active alarms/issues")
for alarm in alarms:
    print(f"   - {alarm['line_id']}: {alarm['alarm_code']} ({alarm['status']})")

# Test 3: Fault Details
print("\n3️⃣  Testing get_fault_details('E-412')...")
fault = tools.get_fault_details("E-412")
print(f"✅ {fault['fault']['error_code']}: {fault['fault']['description']}")

# Test 4: Maintenance History
print("\n4️⃣  Testing get_maintenance_history('M-07')...")
history = tools.get_maintenance_history("M-07")
print(f"✅ Machine M-07: {history['summary']['total_events']} maintenance events")
print(f"   - Emergency events: {history['summary']['emergency_count']}")

# Test 5: Quality Summary
print("\n5️⃣  Testing get_quality_summary('current_shift')...")
quality = tools.get_quality_summary("current_shift")
print(f"✅ Shift quality: {quality['shift_summary']['defect_rate']}% defect rate")

# Test 6: Shift Performance Report
print("\n6️⃣  Testing get_shift_performance_report()...")
report = tools.get_shift_performance_report()
perf = report['shift_performance']
print(f"✅ Shift Performance:")
print(f"   - Lines Running: {perf['lines_running']}")
print(f"   - Lines Down: {perf['lines_down']}")
print(f"   - Average OEE: {perf['average_oee']}%")
print(f"   - Overall Attainment: {perf['overall_attainment_pct']}%")
print(f"   - Critical Issues: {len(report['critical_issues'])}")

# Test 7: Agent Load
print("\n7️⃣  Testing agent import...")
from factory_agent.agent import root_agent, production_monitor_agent, maintenance_agent, quality_agent
print(f"✅ Root Agent: {root_agent.name}")
print(f"✅ Sub-agents: {len(root_agent.sub_agents)} loaded")
print(f"   - {production_monitor_agent.name}")
print(f"   - {maintenance_agent.name}")
print(f"   - {quality_agent.name}")

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED!")
print("=" * 60)
print("\nNext step: Launch the ADK web UI")
print("Run: adk web")
print("Then open: http://localhost:8000")
print("=" * 60)
