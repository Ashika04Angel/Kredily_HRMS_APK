"""
Profile Page Object for Kredily HRMS Android Mobile App
"""
from pages.base_page import BasePage

class ProfilePage(BasePage):
    # Locators
    PROFILE_HEADER = ("accessibility id", "text_profile_name")
    DESIGNATION_TEXT = ("accessibility id", "text_profile_designation")
    DEPARTMENT_TEXT = ("accessibility id", "text_profile_department")
    WORK_EMAIL_TEXT = ("accessibility id", "text_profile_email")
    SECTION_PERSONAL_INFO = ("accessibility id", "section_personal_info")
    SECTION_WORK_INFO = ("accessibility id", "section_work_info")
    SECTION_BANK_DETAILS = ("accessibility id", "section_bank_details")
    LOGOUT_BTN = ("accessibility id", "btn_profile_logout")

    def get_profile_name(self):
        return self.get_text(self.PROFILE_HEADER[0], self.PROFILE_HEADER[1])

    def get_designation(self):
        return self.get_text(self.DESIGNATION_TEXT[0], self.DESIGNATION_TEXT[1])

    def logout(self):
        self.click(self.LOGOUT_BTN[0], self.LOGOUT_BTN[1])
