from testlab.leave import LeaveCalculator
from testlab.common import heading, note, blank, summary

TITLE = "BOUNDARY VALUE ANALYSIS"

DESCRIPTION = (
    "Boundary Value Analysis tests values at and around the edges of an "
    "input range, because that is where defects most commonly occur."
)

ASPECT = "Requested leave must be between 1 and 30 days."


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()
    note("Aspect under test:")
    note(ASPECT)
    blank()
    note("Rule: days must be between 1 and 30")
    blank()
    note("We test values immediately below, at, and above each boundary.")
    blank()

    boundary_cases = [
        (0, "REJECTED", "below lower boundary"),
        (1, "APPROVED", "lower boundary"),
        (2, "APPROVED", "just above lower boundary"),
        (29, "APPROVED", "just below upper boundary"),
        (30, "APPROVED", "upper boundary"),
        (31, "REJECTED", "above upper boundary"),
    ]

    passed = 0
    for days, expected, position in boundary_cases:
        calc = LeaveCalculator(balance=100)
        approved, actual_word = calc.request(days)
        actual = "APPROVED" if approved else "REJECTED"
        ok = actual == expected
        passed += ok
        mark = "OK" if ok else "XX"
        note(f"  {days:>3} days  ->  {actual}  {mark}  ({position})")

    print()
    summary(len(boundary_cases), passed)
    blank()
    note("Note: available balance is another business constraint. Even if")
    note("days are within 1-30, a request can still be rejected if it")
    note("exceeds the employee's balance.")
    blank()
    note("Boundary Value Analysis targets values at and around the limits")
    note("of an input range, because that is where defects most commonly hide.")
    return passed, len(boundary_cases)
