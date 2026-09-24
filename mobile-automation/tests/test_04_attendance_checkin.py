"""
Test Journey 4: Attendance Clock-in / Check-in Workflow
Automates attendance screen navigation, location display verification, and clock-in punch.
"""
import pytest
from pages.attendance_page import AttendancePage

@pytest.mark.smoke
@pytest.mark.attendance
def test_attendance_clock_in_workflow(logged_in_dashboard, driver):
    """
    Step 1: Open Attendance screen from Dashboard
    Step 2: Verify current status & location detection
    Step 3: Tap Clock In button and confirm punch
    Step 4: Assert Punch success confirmation and daily logs
    """
    dashboard = logged_in_dashboard
    dashboard.navigate_to_attendance()
    
    attendance_page = AttendancePage(driver)
    
    # 1. Verify Status & Location display
    status = attendance_page.get_clock_status()
    assert len(status) > 0, "Current clock status should be displayed"
    
    location = attendance_page.get_detected_location()
    assert len(location) > 0, "Location address should be detected"
    
    # 2. Perform Clock-In punch
    attendance_page.perform_clock_in()
    
    # 3. Verify confirmation toast or updated daily logs
    assert attendance_page.is_daily_log_visible() or attendance_page.is_punch_success_displayed(), \
        "Attendance punch confirmation or daily log should be visible"
