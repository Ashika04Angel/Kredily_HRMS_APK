"""
Pytest configuration, fixtures, and execution hooks for Mobile Automation
"""
import pytest
import os
import sys
import logging

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.driver_factory import DriverFactory
from config.config import Config

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("MobileAutomation")

@pytest.fixture(scope="function")
def driver(request):
    """
    Initializes driver before each test function and tears it down after.
    """
    logger.info(f"--- Starting Mobile Test: {request.node.name} ---")
    driver_instance = DriverFactory.get_driver()
    yield driver_instance
    logger.info(f"--- Completed Mobile Test: {request.node.name} ---")
    try:
        driver_instance.quit()
    except Exception as e:
        logger.warning(f"Error during driver teardown: {e}")

@pytest.fixture
def logged_in_dashboard(driver):
    """
    Precondition fixture that performs valid login and yields DashboardPage.
    """
    from pages.login_page import LoginPage
    from pages.dashboard_page import DashboardPage
    
    login_page = LoginPage(driver)
    login_page.login(Config.VALID_USER["email"], Config.VALID_USER["password"])
    dashboard_page = DashboardPage(driver)
    return dashboard_page
