"""
Test Journey 3: Dashboard Validation Workflow
Validates dashboard widgets, quick action tiles, and bottom navigation tabs.
"""
import pytest
from pages.dashboard_page import DashboardPage

@pytest.mark.smoke
@pytest.mark.dashboard
def test_dashboard_widgets_and_navigation(logged_in_dashboard):
    """
    Step 1: Verify employee header greeting
    Step 2: Verify attendance clocking dashlet presence
    Step 3: Verify leave balances summary card presence
    Step 4: Verify navigation tabs functionality
    """
    dashboard = logged_in_dashboard
    
    # 1. Verify Greeting & Header
    greeting = dashboard.get_greeting()
    assert len(greeting) > 0, "Dashboard greeting header should be visible"
    
    # 2. Verify Attendance Dashlet
    assert dashboard.is_attendance_dashlet_visible(), "Attendance widget should be rendered"
    
    # 3. Verify Leave Balances Card
    assert dashboard.is_leave_card_visible(), "Leave balances card should be rendered"
    
    # 4. Verify Tab Navigation
    dashboard.navigate_to_attendance()
    dashboard.navigate_to_leave()
    dashboard.navigate_to_payroll()
    dashboard.navigate_to_profile()
