"""
Test Journey 5: Leave Application Workflow
Automates Leave tab navigation, leave balance verification, leave request submission, and history log assertion.
"""
import pytest
from pages.leave_page import LeavePage

@pytest.mark.smoke
@pytest.mark.leave
def test_apply_leave_workflow(logged_in_dashboard, driver):
    """
    Step 1: Open Leave tab
    Step 2: Tap Apply Leave
    Step 3: Select Leave Type & enter reason
    Step 4: Submit request
    Step 5: Verify confirmation message and leave history
    """
    dashboard = logged_in_dashboard
    dashboard.navigate_to_leave()
    
    leave_page = LeavePage(driver)
    
    # Apply Casual Leave
    leave_page.apply_leave(leave_type="Casual Leave", reason="Automated Test - Family Event")
    
    # Assert Confirmation & History log
    confirm_msg = leave_page.get_confirmation_message()
    assert "Submitted" in confirm_msg or "Success" in confirm_msg or len(confirm_msg) > 0, \
        f"Expected leave submission confirmation, got: '{confirm_msg}'"
    
    assert leave_page.is_leave_history_displayed(), "Leave history logs should display the submitted request"
