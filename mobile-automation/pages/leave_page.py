"""
Leave Page Object for Kredily HRMS Android Mobile App
"""
from pages.base_page import BasePage

class LeavePage(BasePage):
    # Locators
    LEAVE_BALANCES_CONTAINER = ("accessibility id", "container_leave_balances")
    APPLY_LEAVE_BTN = ("accessibility id", "btn_apply_leave_main")
    LEAVE_TYPE_DROPDOWN = ("accessibility id", "select_leave_type")
    CASUAL_LEAVE_OPTION = ("accessibility id", "option_casual_leave")
    SICK_LEAVE_OPTION = ("accessibility id", "option_sick_leave")
    FROM_DATE_PICKER = ("accessibility id", "picker_from_date")
    TO_DATE_PICKER = ("accessibility id", "picker_to_date")
    REASON_INPUT = ("accessibility id", "input_leave_reason")
    SUBMIT_LEAVE_BTN = ("accessibility id", "btn_submit_leave_request")
    LEAVE_CONFIRMATION_TOAST = ("accessibility id", "toast_leave_submitted_success")
    LEAVE_HISTORY_LIST = ("accessibility id", "list_leave_history_logs")
    ERROR_VALIDATION_MSG = ("accessibility id", "text_leave_validation_error")

    def click_apply_leave(self):
        self.click(self.APPLY_LEAVE_BTN[0], self.APPLY_LEAVE_BTN[1])

    def select_leave_type(self, leave_type="Casual Leave"):
        self.click(self.LEAVE_TYPE_DROPDOWN[0], self.LEAVE_TYPE_DROPDOWN[1])
        if "casual" in leave_type.lower():
            self.click(self.CASUAL_LEAVE_OPTION[0], self.CASUAL_LEAVE_OPTION[1])
        else:
            self.click(self.SICK_LEAVE_OPTION[0], self.SICK_LEAVE_OPTION[1])

    def enter_reason(self, reason):
        self.set_text(self.REASON_INPUT[0], self.REASON_INPUT[1], reason)

    def submit_leave(self):
        self.click(self.SUBMIT_LEAVE_BTN[0], self.SUBMIT_LEAVE_BTN[1])

    def apply_leave(self, leave_type, reason):
        self.click_apply_leave()
        self.select_leave_type(leave_type)
        self.enter_reason(reason)
        self.submit_leave()

    def get_confirmation_message(self):
        return self.get_text(self.LEAVE_CONFIRMATION_TOAST[0], self.LEAVE_CONFIRMATION_TOAST[1])

    def is_leave_history_displayed(self):
        return self.is_displayed(self.LEAVE_HISTORY_LIST[0], self.LEAVE_HISTORY_LIST[1])

    def get_validation_error(self):
        return self.get_text(self.ERROR_VALIDATION_MSG[0], self.ERROR_VALIDATION_MSG[1])
