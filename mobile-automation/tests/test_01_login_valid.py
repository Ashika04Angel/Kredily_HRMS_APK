"""
Test Journey 1: Valid Login Workflow
Automates employee login with valid credentials and verifies dashboard navigation.
"""
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import Config

@pytest.mark.smoke
@pytest.mark.login
def test_valid_login_journey(driver):
    """
    Step 1: Open Kredily App
    Step 2: Enter valid email
    Step 3: Proceed to password screen
    Step 4: Enter password and tap Sign In
    Step 5: Assert dashboard greeting and attendance widget
    """
    login_page = LoginPage(driver)
    
    # 1. Assert Login screen is loaded
    assert login_page.is_login_screen_visible(), "Login identifier screen should be visible"
    
    # 2. Enter registered employee email
    login_page.enter_email(Config.VALID_USER["email"])
    login_page.click_continue()
    
    # 3. Enter password & Sign In
    login_page.enter_password(Config.VALID_USER["password"])
    login_page.click_sign_in()
    
    # 4. Verify Dashboard is displayed
    dashboard_page = DashboardPage(driver)
    greeting = dashboard_page.get_greeting()
    
    assert "Good Morning" in greeting or "Employee" in greeting or len(greeting) > 0, \
        f"Expected greeting on dashboard, got: '{greeting}'"
    assert dashboard_page.is_attendance_dashlet_visible(), "Attendance clocking dashlet should be visible on dashboard"
