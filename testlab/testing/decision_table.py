from testlab.leave import LeaveCalculator
from testlab.common import heading, note, blank, table_header, table_separator, table_row, summary

TITLE = "DECISION TABLE TESTING"

DESCRIPTION = (
    "Decision Table Testing lists combinations of input conditions and the "
    "expected action for each, ensuring no rule interaction is missed."
)

ASPECT = (
    "Conditions:\n"
    "  1. Leave type is valid\n"
    "  2. Requested days > 0\n"
    "  3. Requested days <= maximum\n"
    "  4. Requested days <= balance\n"
    "Actions: APPROVED or REJECTED."
)


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()
    note("Aspect under test:")
    note(ASPECT)
    blank()

    note("Decision table:")
    table_header([
        ("Leave Type", 11), ("Days > 0", 9), ("Days <= Max", 10), ("Days <= Balance", 13), ("Result", 9)
    ])
    table_separator([
        ("Leave Type", 11), ("Days > 0", 9), ("Days <= Max", 10), ("Days <= Balance", 13), ("Result", 9)
    ])
    table_rows = [
        ("Valid", "Yes", "Yes", "Yes", "APPROVED"),
        ("Invalid", "Yes", "Yes", "Yes", "REJECTED"),
        ("Valid", "No", "Yes", "Yes", "REJECTED"),
        ("Valid", "Yes", "No", "Yes", "REJECTED"),
        ("Valid", "Yes", "Yes", "No", "REJECTED"),
        ("Invalid", "No", "No", "No", "REJECTED"),
    ]
    for row in table_rows:
        table_row([(v, w) for v, w in zip(row, [11, 9, 10, 13, 9])])

    blank()

    cases = [
        ("casual", 10, 5, "APPROVED", "all conditions true"),
        ("invalid", 10, 5, "REJECTED", "leave type invalid"),
        ("casual", 10, 0, "REJECTED", "days not greater than 0"),
        ("casual", 100, 31, "REJECTED", "days exceed maximum"),
        ("casual", 3, 5, "REJECTED", "days exceed balance"),
        ("invalid", 3, 0, "REJECTED", "multiple conditions fail"),
    ]

    passed = 0
    table_header([
        ("Leave Type", 11), ("Balance", 8), ("Days", 6), ("Expected", 11), ("Actual", 11), ("Status", 7)
    ])
    table_separator([
        ("Leave Type", 11), ("Balance", 8), ("Days", 6), ("Expected", 11), ("Actual", 11), ("Status", 7)
    ])
    for leave_type, balance, days, expected, condition_note in cases:
        calc = LeaveCalculator(balance=balance, leave_type=leave_type)
        approved, actual_word = calc.request(days)
        actual = "APPROVED" if approved else "REJECTED"
        ok = actual == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        table_row([
            (leave_type, 11), (balance, 8), (days, 6),
            (expected, 11), (actual, 11), (status, 7)
        ])

    print()
    summary(len(cases), passed)
    blank()
    note("The table captures every meaningful combination of conditions, so")
    note("no rule interaction is missed. Each row becomes one test case.")
    return passed, len(cases)
