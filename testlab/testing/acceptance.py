from testlab.leave import LeaveCalculator
from testlab.common import heading, note, blank, summary

TITLE = "ACCEPTANCE TESTING"

DESCRIPTION = (
    "Acceptance testing checks the system against business requirements "
    "from the user's perspective: does it do what the business needs?"
)


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()

    cases = [
        (
            "An employee must not request more leave than available.",
            "Given: Balance = 5 days",
            "When:    Request = 6 days",
            "Then:    Request must be rejected.",
            5, 6, "REJECTED",
        ),
        (
            "Requested leave must be greater than 0.",
            "Given: Balance = 10 days",
            "When:    Request = 0 days",
            "Then:    Request must be rejected.",
            10, 0, "REJECTED",
        ),
        (
            "A valid request within the available balance must be approved.",
            "Given: Balance = 10 days",
            "When:    Request = 5 days",
            "Then:    Request must be approved.",
            10, 5, "APPROVED",
        ),
    ]

    passed = 0
    for requirement, given, when, then, balance, days, expected in cases:
        note(f"Requirement: {requirement}")
        note(given)
        note(when)
        note(then)

        calc = LeaveCalculator(balance=balance)
        approved, actual_word = calc.request(days)
        actual = "APPROVED" if approved else "REJECTED"
        ok = actual == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        note(f"Result: {expected} / {actual}  [{status}]")
        blank()

    print()
    summary(len(cases), passed)
    blank()
    note("Each case is written from a business requirement, not from the")
    note("code. This differs from system testing, which checks the system")
    note("works end-to-end; acceptance testing checks it satisfies the")
    note("business need.")
    return passed, len(cases)
