"""
Attendance Page Object for Kredily HRMS Android Mobile App
"""
from pages.base_page import BasePage

class AttendancePage(BasePage):
    # Locators
    PUNCH_BUTTON = ("accessibility id", "btn_attendance_punch_action")
    CLOCK_STATUS_TEXT = ("accessibility id", "text_current_clock_status")
    LOCATION_ADDRESS = ("accessibility id", "text_detected_location_address")
    CONFIRM_PUNCH_MODAL_BTN = ("accessibility id", "btn_confirm_punch_modal")
    SELFIE_CAPTURE_BTN = ("accessibility id", "btn_capture_attendance_selfie")
    PUNCH_SUCCESS_TOAST = ("accessibility id", "toast_punch_success")
    DAILY_LOG_LIST = ("accessibility id", "list_attendance_daily_logs")
    MONTHLY_SUMMARY_CARD = ("accessibility id", "card_attendance_monthly_summary")
    REGULARIZE_ATTENDANCE_BTN = ("accessibility id", "btn_regularize_attendance")

    def get_clock_status(self):
        return self.get_text(self.CLOCK_STATUS_TEXT[0], self.CLOCK_STATUS_TEXT[1])

    def get_detected_location(self):
        return self.get_text(self.LOCATION_ADDRESS[0], self.LOCATION_ADDRESS[1])

    def perform_clock_in(self):
        self.click(self.PUNCH_BUTTON[0], self.PUNCH_BUTTON[1])
        if self.is_displayed(self.CONFIRM_PUNCH_MODAL_BTN[0], self.CONFIRM_PUNCH_MODAL_BTN[1]):
            self.click(self.CONFIRM_PUNCH_MODAL_BTN[0], self.CONFIRM_PUNCH_MODAL_BTN[1])

    def perform_clock_out(self):
        self.click(self.PUNCH_BUTTON[0], self.PUNCH_BUTTON[1])
        if self.is_displayed(self.CONFIRM_PUNCH_MODAL_BTN[0], self.CONFIRM_PUNCH_MODAL_BTN[1]):
            self.click(self.CONFIRM_PUNCH_MODAL_BTN[0], self.CONFIRM_PUNCH_MODAL_BTN[1])

    def is_punch_success_displayed(self):
        return self.is_displayed(self.PUNCH_SUCCESS_TOAST[0], self.PUNCH_SUCCESS_TOAST[1])

    def is_daily_log_visible(self):
        return self.is_displayed(self.DAILY_LOG_LIST[0], self.DAILY_LOG_LIST[1])
