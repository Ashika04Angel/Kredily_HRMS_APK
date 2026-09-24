"""
Test Journey 2: Invalid Login & Error Validation Workflow
Automates negative authentication cases (incorrect password & malformed inputs).
"""
import pytest
from pages.login_page import LoginPage
from config.config import Config

@pytest.mark.regression
@pytest.mark.login
def test_invalid_password_error_handling(driver):
    """
    Step 1: Enter valid email identifier
    Step 2: Enter invalid password
    Step 3: Tap Sign In
    Step 4: Verify error banner/toast appears without app crash
    """
    login_page = LoginPage(driver)
    
    login_page.enter_email(Config.INVALID_USER["email"])
    login_page.click_continue()
    
    login_page.enter_password(Config.INVALID_USER["password"])
    login_page.click_sign_in()
    
    # Assert error message is presented
    error_msg = login_page.get_error_message()
    assert "Invalid" in error_msg or "password" in error_msg.lower() or len(error_msg) > 0, \
        f"Expected invalid password error, got: '{error_msg}'"

@pytest.mark.regression
@pytest.mark.login
def test_malformed_email_client_validation(driver):
    """
    Step 1: Enter malformed email format
    Step 2: Verify input validation triggers
    """
    login_page = LoginPage(driver)
    login_page.enter_email(Config.INVALID_USER["malformed_email"])
    login_page.click_continue()
    
    # Form should remain on login screen without advancing
    assert login_page.is_login_screen_visible(), "Should prevent navigation on malformed email input"
