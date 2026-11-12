from testlab.leave import LeaveCalculator
from testlab.common import heading, note, blank, table_header, table_separator, table_row, summary

TITLE = "INTEGRATION TESTING"

DESCRIPTION = (
    "Integration testing checks that multiple components work correctly "
    "together when their outputs feed into each other."
)

ASPECT = (
    "The integrated flow: Leave Request -> Validation -> Balance "
    "Calculation -> Approval Decision"
)

FLOW = (
    "  Leave Request\n"
    "        |\n"
    "    Validation\n"
    "        |\n"
    "  Balance Calculation\n"
    "        |\n"
    "  Approval Decision"
)


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()
    note("Aspect under test:")
    note(ASPECT)
    blank()
    note("Component flow:")
    note(FLOW)
    blank()

    passed = 0
    count = 0

    single = [
        (10, 5, "APPROVED", "valid request within balance"),
        (10, 11, "REJECTED", "request exceeds the balance"),
        (3, 31, "REJECTED", "request exceeds the maximum"),
    ]
    table_header([
        ("Balance", 8), ("Days", 6), ("Expected", 11), ("Actual", 11), ("Status", 7)
    ])
    table_separator([
        ("Balance", 8), ("Days", 6), ("Expected", 11), ("Actual", 11), ("Status", 7)
    ])
    for balance, days, expected, why in single:
        calc = LeaveCalculator(balance=balance)
        approved, actual_word = calc.request(days)
        actual = "APPROVED" if approved else "REJECTED"
        ok = actual == expected
        passed += ok
        count += 1
        status = "PASS" if ok else "FAIL"
        table_row([
            (balance, 8), (days, 6), (expected, 11), (actual, 11), (status, 7)
        ])

    blank()
    note("Sequential requests on one calculator (balance carries over):")
    table_header([
        ("Start bal.", 9), ("Days", 6), ("Result", 9), ("Remaining", 10), ("Status", 7)
    ])
    table_separator([
        ("Start bal.", 9), ("Days", 6), ("Result", 9), ("Remaining", 10), ("Status", 7)
    ])

    shared = LeaveCalculator(balance=20)
    sequential = [
        (8, "APPROVED", "first request approved"),
        (7, "APPROVED", "second request uses updated balance"),
    ]
    for days, expected, why in sequential:
        start = shared.balance
        approved, actual_word = shared.request(days)
        actual = "APPROVED" if approved else "REJECTED"
        remaining = shared.remaining()
        ok = actual == expected
        passed += ok
        count += 1
        status = "PASS" if ok else "FAIL"
        table_row([
            (start, 9), (days, 6), (expected, 9), (str(remaining), 10), (status, 7)
        ])

    blank()
    note("Rejected request must not change the balance:")
    calc = LeaveCalculator(balance=10)
    calc.request(11)
    before = calc.remaining()
    ok = before == 10
    passed += ok
    count += 1
    status = "PASS" if ok else "FAIL"
    table_row([
        (10, 8), (11, 6), ("REJECTED", 11), (str(before), 11), (status, 7)
    ])

    print()
    summary(count, passed)
    blank()
    note("These tests exercise several components in sequence and check that")
    note("state (the balance) is carried correctly between them.")
    note("A failure here means a component works alone but not together.")
    return passed, count
