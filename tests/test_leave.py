import unittest

from testlab.leave import LeaveCalculator, MAX_LEAVE_DAYS


class TestLeaveCalculator(unittest.TestCase):
    def test_valid_request_approved(self):
        calc = LeaveCalculator(balance=10)
        approved, result = calc.request(5)
        self.assertTrue(approved)
        self.assertEqual(result, "APPROVED")

    def test_request_exceeds_balance_rejected(self):
        calc = LeaveCalculator(balance=10)
        approved, result = calc.request(11)
        self.assertFalse(approved)
        self.assertEqual(result, "REJECTED")

    def test_request_equals_balance_approved(self):
        calc = LeaveCalculator(balance=10)
        approved, _ = calc.request(10)
        self.assertTrue(approved)

    def test_zero_days_rejected(self):
        calc = LeaveCalculator(balance=10)
        approved, _ = calc.request(0)
        self.assertFalse(approved)

    def test_negative_days_rejected(self):
        calc = LeaveCalculator(balance=10)
        approved, _ = calc.request(-3)
        self.assertFalse(approved)

    def test_exceeds_maximum_rejected(self):
        calc = LeaveCalculator(balance=100)
        approved, _ = calc.request(MAX_LEAVE_DAYS + 1)
        self.assertFalse(approved)

    def test_maximum_days_approved(self):
        calc = LeaveCalculator(balance=100)
        approved, _ = calc.request(MAX_LEAVE_DAYS)
        self.assertTrue(approved)

    def test_invalid_leave_type_rejected(self):
        calc = LeaveCalculator(balance=10, leave_type="invalid")
        approved, _ = calc.request(5)
        self.assertFalse(approved)

    def test_balance_reduced_on_approval(self):
        calc = LeaveCalculator(balance=10)
        calc.request(4)
        self.assertEqual(calc.remaining(), 6)

    def test_balance_unchanged_on_rejection(self):
        calc = LeaveCalculator(balance=10)
        calc.request(11)
        self.assertEqual(calc.remaining(), 10)

    def test_days_valid_unit(self):
        calc = LeaveCalculator()
        self.assertTrue(calc.days_valid(5))
        self.assertFalse(calc.days_valid(0))
        self.assertFalse(calc.days_valid(-1))

    def test_calculate_remaining_balance(self):
        calc = LeaveCalculator(balance=20)
        self.assertEqual(calc.calculate_remaining_balance(6), 14)


if __name__ == "__main__":
    unittest.main()
