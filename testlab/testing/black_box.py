from testlab.leave import LeaveCalculator
from testlab.common import heading, note, blank, table_header, table_separator, table_row, summary

TITLE = "BLACK-BOX TESTING"

DESCRIPTION = (
    "Black-box testing checks what the system does, not how it does it. "
    "Tests are designed from inputs and expected outputs only."
)

ASPECT = (
    "Given a leave balance and a number of requested days, does the system "
    "approve or reject the request?"
)


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()
    note("Aspect under test:")
    note(ASPECT)
    blank()

    note("Input  ->  Leave Calculator  ->  Result")
    blank()

    table_header([
        ("Balance", 8), ("Days", 6), ("Expected", 11), ("Actual", 11), ("Status", 7)
    ])
    table_separator([
        ("Balance", 8), ("Days", 6), ("Expected", 11), ("Actual", 11), ("Status", 7)
    ])

    cases = [
        (10, 5, "APPROVED", "request is within the available balance"),
        (10, 10, "APPROVED", "request equals the available balance"),
        (10, 11, "REJECTED", "request exceeds the available balance"),
        (10, 0, "REJECTED", "requested leave must be greater than 0"),
        (10, -3, "REJECTED", "negative input is not valid"),
        (5, 31, "REJECTED", "request exceeds the maximum allowed"),
    ]

    passed = 0
    for balance, days, expected, why in cases:
        calc = LeaveCalculator(balance=balance)
        approved, actual_word = calc.request(days)
        actual = "APPROVED" if approved else "REJECTED"
        ok = actual == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        table_row([
            (balance, 8), (days, 6), (expected, 11), (actual, 11), (status, 7)
        ])

    print()
    summary(len(cases), passed)
    blank()
    note("Why these cases?")
    note("We only use inputs and expected results.")
    note("No knowledge of the internal code is needed to write them.")
    return passed, len(cases)
