from testlab.leave import LeaveCalculator
from testlab.common import heading, note, blank, table_header, table_separator, table_row, summary

TITLE = "SYSTEM TESTING"

DESCRIPTION = (
    "System testing checks the Leave Calculator as a complete system, "
    "using realistic inputs a user would actually provide."
)

ASPECT = (
    "Full request handling with employee, leave type, balance, and "
    "requested days combined into one call."
)


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()
    note("Aspect under test:")
    note(ASPECT)
    blank()

    cases = [
        ("Alice", "casual", 20, 5, "APPROVED", "employee requests leave within balance"),
        ("Bob", "sick", 3, 10, "REJECTED", "employee requests more leave than available"),
        ("Carol", "earned", 30, 30, "APPROVED", "employee uses full balance up to the maximum"),
    ]

    passed = 0
    table_header([
        ("Employee", 10), ("Type", 8), ("Balance", 8), ("Days", 6), ("Expected", 11), ("Actual", 11), ("Status", 7)
    ])
    table_separator([
        ("Employee", 10), ("Type", 8), ("Balance", 8), ("Days", 6), ("Expected", 11), ("Actual", 11), ("Status", 7)
    ])
    for employee, leave_type, balance, days, expected, why in cases:
        calc = LeaveCalculator(balance=balance, leave_type=leave_type)
        approved, actual_word = calc.request(days)
        actual = "APPROVED" if approved else "REJECTED"
        ok = actual == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        table_row([
            (employee, 10), (leave_type, 8), (balance, 8), (days, 6),
            (expected, 11), (actual, 11), (status, 7)
        ])

    print()
    summary(len(cases), passed)
    blank()
    note("Each test uses realistic user input and treats the calculator as a whole.")
    note("This is different from unit testing, which checks small parts individually.")
    return passed, len(cases)
