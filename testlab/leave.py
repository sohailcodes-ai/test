MAX_LEAVE_DAYS = 30
VALID_LEAVE_TYPES = ("casual", "sick", "earned")


class LeaveCalculator:
    """Subject under test: a small leave request calculator.

    Rules:
      - Requested leave must be greater than 0.
      - Requested leave cannot exceed the available balance.
      - Requested leave cannot exceed the allowed maximum.
      - Leave type must be a recognised type.
      - Valid requests are approved and reduce the balance.
    """

    def __init__(self, balance=0, leave_type="casual"):
        self.balance = balance
        self.leave_type = leave_type

    def days_valid(self, days):
        try:
            return float(days) > 0
        except (TypeError, ValueError):
            return False

    def leave_type_valid(self):
        return self.leave_type in VALID_LEAVE_TYPES

    def within_balance(self, days):
        return days <= self.balance

    def within_maximum(self, days):
        return days <= MAX_LEAVE_DAYS

    def calculate_remaining_balance(self, days):
        return self.balance - days

    def request(self, days):
        if not self.leave_type_valid():
            return False, "REJECTED"
        if not self.days_valid(days):
            return False, "REJECTED"
        if not self.within_maximum(days):
            return False, "REJECTED"
        if not self.within_balance(days):
            return False, "REJECTED"
        self.balance -= days
        return True, "APPROVED"

    def remaining(self):
        return self.balance
