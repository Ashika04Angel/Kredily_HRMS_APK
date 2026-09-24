"""
Configuration and Desired Capabilities for Kredily Mobile Automation
"""
import os

class Config:
    # Appium Server Details
    APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723/wd/hub")
    
    # APK Path & Metadata
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    APK_PATH = os.path.join(os.path.dirname(BASE_DIR), "kredily-mobile-v2.apk")
    
    # Android App Package & Main Activity
    APP_PACKAGE = "com.kredily.mobile"
    APP_ACTIVITY = "com.kredily.mobile.MainActivity"
    
    # Appium Capabilities
    DESIRED_CAPABILITIES = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": os.getenv("DEVICE_NAME", "Android Emulator"),
        "platformVersion": os.getenv("PLATFORM_VERSION", "13.0"),
        "app": APK_PATH,
        "appPackage": APP_PACKAGE,
        "appActivity": APP_ACTIVITY,
        "noReset": False,
        "fullReset": False,
        "autoGrantPermissions": True,
        "newCommandTimeout": 300,
        "uiautomator2ServerLaunchTimeout": 60000,
        "uiautomator2ServerInstallTimeout": 60000,
    }
    
    # Test User Credentials
    VALID_USER = {
        "email": "peoplekredily1@yopmail.com",
        "password": "Pass@9865",
        "employee_name": "Test Employee",
        "designation": "Software Quality Assurance Intern",
        "department": "Engineering / QA"
    }
    
    INVALID_USER = {
        "email": "peoplekredily1@yopmail.com",
        "password": "InvalidPassword@123",
        "malformed_email": "invalid_format@@yopmail..com"
    }
    
    # Timeouts (seconds)
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    POLL_FREQUENCY = 0.5
