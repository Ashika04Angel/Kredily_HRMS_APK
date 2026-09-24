"""
Base Page Object for Kredily HRMS Mobile Automation
"""
import time
import logging

logger = logging.getLogger("MobileAutomation")

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        except Exception as e:
            logger.error(f"Failed to find element: {by}='{locator}' - {e}")
            raise

    def find_elements(self, by, locator):
        try:
            return self.driver.find_elements(by, locator)
        except Exception as e:
            logger.error(f"Failed to find elements: {by}='{locator}' - {e}")
            return []

    def click(self, by, locator):
        logger.info(f"Clicking on: {locator}")
        element = self.find_element(by, locator)
        element.click()

    def set_text(self, by, locator, text):
        logger.info(f"Entering text into {locator}")
        element = self.find_element(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        element = self.find_element(by, locator)
        text = element.text
        logger.info(f"Retrieved text '{text}' from {locator}")
        return text

    def is_displayed(self, by, locator):
        try:
            element = self.find_element(by, locator)
            return element.is_displayed()
        except Exception:
            return False

    def is_enabled(self, by, locator):
        try:
            element = self.find_element(by, locator)
            return element.is_enabled()
        except Exception:
            return False

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        logger.info(f"Screenshot captured: {filename}")
