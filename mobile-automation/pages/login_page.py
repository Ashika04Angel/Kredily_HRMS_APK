"""
Login Page Object for Kredily HRMS Android Mobile App
"""
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators (Appium / UiAutomator2 selectors)
    EMAIL_INPUT = ("accessibility id", "input_email_or_mobile")
    CONTINUE_BTN = ("accessibility id", "btn_continue_identifier")
    PASSWORD_INPUT = ("accessibility id", "input_password")
    SIGN_IN_BTN = ("accessibility id", "btn_sign_in")
    FORGOT_PASSWORD_LINK = ("accessibility id", "link_forgot_password")
    ERROR_ALERT = ("accessibility id", "text_error_alert")
    HEADER_LOGO = ("accessibility id", "img_kredily_logo")
    SHOW_PASSWORD_ICON = ("accessibility id", "btn_toggle_password_visibility")

    def enter_email(self, email):
        self.set_text(self.EMAIL_INPUT[0], self.EMAIL_INPUT[1], email)

    def click_continue(self):
        self.click(self.CONTINUE_BTN[0], self.CONTINUE_BTN[1])

    def enter_password(self, password):
        self.set_text(self.PASSWORD_INPUT[0], self.PASSWORD_INPUT[1], password)

    def click_sign_in(self):
        self.click(self.SIGN_IN_BTN[0], self.SIGN_IN_BTN[1])

    def login(self, email, password):
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_sign_in()

    def get_error_message(self):
        return self.get_text(self.ERROR_ALERT[0], self.ERROR_ALERT[1])

    def is_login_screen_visible(self):
        return self.is_displayed(self.EMAIL_INPUT[0], self.EMAIL_INPUT[1])
