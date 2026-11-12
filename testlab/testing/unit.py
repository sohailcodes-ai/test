from testlab.leave import LeaveCalculator
from testlab.common import heading, note, blank, table_header, table_separator, table_row, summary

TITLE = "UNIT TESTING"

DESCRIPTION = (
    "Unit testing checks individual functions in isolation, separate from "
    "the rest of the system."
)

ASPECT = (
    "Individual units of the Leave Calculator:\n"
    "  days_valid()            - is the requested day count valid?\n"
    "  leave_type_valid()      - is the leave type recognised?\n"
    "  within_balance()        - is the request within the balance?\n"
    "  within_maximum()        - is the request within the maximum?\n"
    "  calculate_remaining_balance() - balance after approval"
)


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()
    note("Aspect under test:")
    note(ASPECT)
    blank()

    cases = [
        ("days_valid(5)", LeaveCalculator().days_valid(5), True, "a positive day count is valid"),
        ("days_valid(0)", LeaveCalculator().days_valid(0), False, "zero days is not valid"),
        ("days_valid(-2)", LeaveCalculator().days_valid(-2), False, "negative days is not valid"),
        ('days_valid("five")', LeaveCalculator().days_valid("five"), False, "non-numeric input is not valid"),
        ("leave_type_valid('casual')", LeaveCalculator(leave_type="casual").leave_type_valid(), True, "casual is a recognised leave type"),
        ("leave_type_valid('invalid')", LeaveCalculator(leave_type="invalid").leave_type_valid(), False, "invalid is not a recognised leave type"),
        ("within_balance(3) with balance 10", LeaveCalculator(balance=10).within_balance(3), True, "3 days is within a balance of 10"),
        ("within_balance(12) with balance 10", LeaveCalculator(balance=10).within_balance(12), False, "12 days exceeds a balance of 10"),
        ("calculate_remaining_balance(6) from 20", LeaveCalculator(balance=20).calculate_remaining_balance(6), 14, "20 minus 6 leaves 14"),
    ]

    passed = 0
    table_header([
        ("Unit", 38), ("Expected", 10), ("Actual", 10), ("Status", 7)
    ])
    table_separator([
        ("Unit", 38), ("Expected", 10), ("Actual", 10), ("Status", 7)
    ])
    for desc, actual, expected, why in cases:
        ok = actual == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        table_row([
            (desc, 38), (str(expected), 10), (str(actual), 10), (status, 7)
        ])

    print()
    summary(len(cases), passed)
    blank()
    note("Each unit is called directly and checked on its own.")
    note("This is what distinguishes unit testing from black-box testing,")
    note("which tests the system through its inputs and outputs.")
    return passed, len(cases)
