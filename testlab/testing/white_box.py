from testlab.leave import LeaveCalculator, MAX_LEAVE_DAYS
from testlab.common import heading, note, blank, table_header, table_separator, table_row, summary

TITLE = "WHITE-BOX TESTING"

DESCRIPTION = (
    "White-box testing looks at the internal program logic. Test inputs are "
    "chosen to exercise specific conditions and branches in the code."
)

ASPECT = (
    "The request is checked against four conditions:\n"
    "  1. Leave type is valid\n"
    "  2. Days are greater than 0\n"
    "  3. Days are within the 30-day limit\n"
    "  4. Days are within the available balance"
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
    note("Each case isolates one condition while the others remain valid.")
    note("This lets us see which part of the internal logic is being exercised.")
    return passed, len(cases)
