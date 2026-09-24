"""
Dashboard Page Object for Kredily HRMS Android Mobile App
"""
from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Locators
    GREETING_HEADER = ("accessibility id", "text_dashboard_greeting")
    EMPLOYEE_NAME = ("accessibility id", "text_employee_name")
    ATTENDANCE_DASHLET = ("accessibility id", "dashlet_attendance_clocking")
    CLOCK_IN_CTA = ("accessibility id", "btn_dashboard_clock_in")
    LEAVE_BALANCE_CARD = ("accessibility id", "card_leave_balance_summary")
    APPLY_LEAVE_CTA = ("accessibility id", "btn_quick_apply_leave")
    PAYROLL_TILE = ("accessibility id", "tile_quick_payroll")
    REGULARIZE_TILE = ("accessibility id", "tile_quick_regularize")
    DIRECTORY_TILE = ("accessibility id", "tile_quick_directory")
    ANNOUNCEMENTS_SECTION = ("accessibility id", "section_announcements_wishes")
    TAB_ATTENDANCE = ("accessibility id", "tab_bottom_attendance")
    TAB_LEAVE = ("accessibility id", "tab_bottom_leave")
    TAB_PAYROLL = ("accessibility id", "tab_bottom_payroll")
    TAB_PROFILE = ("accessibility id", "tab_bottom_profile")

    def get_greeting(self):
        return self.get_text(self.GREETING_HEADER[0], self.GREETING_HEADER[1])

    def is_attendance_dashlet_visible(self):
        return self.is_displayed(self.ATTENDANCE_DASHLET[0], self.ATTENDANCE_DASHLET[1])

    def is_leave_card_visible(self):
        return self.is_displayed(self.LEAVE_BALANCE_CARD[0], self.LEAVE_BALANCE_CARD[1])

    def click_clock_in_dashlet(self):
        self.click(self.CLOCK_IN_CTA[0], self.CLOCK_IN_CTA[1])

    def click_apply_leave_shortcut(self):
        self.click(self.APPLY_LEAVE_CTA[0], self.APPLY_LEAVE_CTA[1])

    def navigate_to_attendance(self):
        self.click(self.TAB_ATTENDANCE[0], self.TAB_ATTENDANCE[1])

    def navigate_to_leave(self):
        self.click(self.TAB_LEAVE[0], self.TAB_LEAVE[1])

    def navigate_to_payroll(self):
        self.click(self.TAB_PAYROLL[0], self.TAB_PAYROLL[1])

    def navigate_to_profile(self):
        self.click(self.TAB_PROFILE[0], self.TAB_PROFILE[1])
