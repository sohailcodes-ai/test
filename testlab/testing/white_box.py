from testlab.leave import LeaveCalculator, MAX_LEAVE_DAYS
from testlab.common import heading, note, blank, table_header, table_separator, table_row, summary

TITLE = "WHITE-BOX TESTING"

DESCRIPTION = (
    "White-box testing means we look at the actual code logic. We pick "
    "inputs that exercise specific conditions and branches."
)

ASPECT = (
    "The calculator checks four conditions before approving a request:\n"
    "  1. Is the leave type valid?\n"
    "  2. Are the days greater than 0?\n"
    "  3. Are the days within the 30-day limit?\n"
    "  4. Are the days within the available balance?"
)


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()
    note("Aspect under test:")
    note(ASPECT)
    blank()

    table_header([
        ("Case", 5), ("Condition changed", 31), ("Result", 8)
    ])
    table_separator([
        ("Case", 5), ("Condition changed", 31), ("Result", 8)
    ])

    cases = [
        (40, 5, "casual", "APPROVE", "All conditions pass"),
        (10, 0, "casual", "REJECT", "Days > 0 fails"),
        (10, 11, "casual", "REJECT", "Days <= balance fails"),
        (40, 31, "casual", "REJECT", "Days <= 30 fails"),
        (10, 5, "invalid", "REJECT", "Leave type fails"),
    ]

    passed = 0
    for idx, (balance, days, leave_type, expected_path, focus) in enumerate(cases, 1):
        calc = LeaveCalculator(balance=balance, leave_type=leave_type)
        approved, actual_word = calc.request(days)
        actual_path = "APPROVE" if approved else "REJECT"
        ok = actual_path == expected_path
        passed += ok
        status = "PASS" if ok else "FAIL"
        table_row([
            (idx, 5), (focus, 31), (actual_path, 8)
        ])

    print()
    summary(len(cases), passed)
    blank()
    note("Each case changes one condition while the others stay valid.")
    note("This shows which part of the internal logic each input exercises.")
    return passed, len(cases)
