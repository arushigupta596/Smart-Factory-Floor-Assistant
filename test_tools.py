"""
Quick test script to verify all factory tools work correctly
Run this before starting the agent to verify data access
"""

from factory_agent import tools


def test_all_tools():
    """Test all factory data tools"""
    print("🧪 Testing Smart Factory Tools\n")
    print("="*60)

    # Test 1: Factory Overview
    print("\n1️⃣ Testing Factory Overview...")
    try:
        overview = tools.get_factory_overview()
        print(f"✅ Factory Overview: {overview['production_lines']['total']} lines, "
              f"{overview['faults']['total_open']} open faults")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 2: Production Line Status
    print("\n2️⃣ Testing Production Line Status...")
    try:
        status = tools.get_production_line_status()
        print(f"✅ Found {len(status['production_lines'])} production lines")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 3: Specific Line Efficiency
    print("\n3️⃣ Testing Line Efficiency for LINE-A2...")
    try:
        efficiency = tools.get_line_efficiency("LINE-A2")
        print(f"✅ LINE-A2 Efficiency: {efficiency['efficiency']}%")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 4: Open Faults
    print("\n4️⃣ Testing Open Machine Faults...")
    try:
        faults = tools.get_machine_faults(status="open")
        print(f"✅ Found {faults['count']} open faults")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 5: Machine-Specific Faults
    print("\n5️⃣ Testing Faults for Machine M005...")
    try:
        machine_faults = tools.get_fault_by_machine("M005")
        print(f"✅ Machine M005 has {machine_faults['count']} fault(s)")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 6: Maintenance History
    print("\n6️⃣ Testing Maintenance History...")
    try:
        maintenance = tools.get_maintenance_history()
        print(f"✅ Found {maintenance['count']} maintenance records")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 7: Scheduled Maintenance
    print("\n7️⃣ Testing Scheduled Maintenance...")
    try:
        scheduled = tools.get_scheduled_maintenance()
        print(f"✅ Found {scheduled['count']} scheduled maintenance tasks")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 8: Quality Inspections
    print("\n8️⃣ Testing Quality Inspections...")
    try:
        inspections = tools.get_quality_inspections()
        print(f"✅ Found {inspections['count']} quality inspections")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 9: Failed Inspections
    print("\n9️⃣ Testing Failed Inspections...")
    try:
        failed = tools.get_failed_inspections()
        print(f"✅ Found {failed['count']} failed inspections")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test 10: Quality Standards
    print("\n🔟 Testing Quality Standards...")
    try:
        standards = tools.get_quality_standards("Widget-X200")
        print(f"✅ Widget-X200 acceptable defect rate: {standards['standards']['acceptable_defect_rate']}%")
    except Exception as e:
        print(f"❌ Failed: {e}")

    print("\n" + "="*60)
    print("✅ All tool tests completed!\n")


if __name__ == "__main__":
    test_all_tools()
