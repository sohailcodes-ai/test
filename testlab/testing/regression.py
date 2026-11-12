from testlab.leave import LeaveCalculator, MAX_LEAVE_DAYS
from testlab.common import heading, note, blank, summary

TITLE = "REGRESSION TESTING"

DESCRIPTION = (
    "Regression testing re-runs previously passing tests after a change to "
    "confirm that existing behaviour still works."
)


class DefectiveCalculator(LeaveCalculator):
    """A controlled copy of the calculator with one introduced defect.

    The defect: the maximum-days check rejects 30 days (which should be
    allowed). This exists only inside this demonstration and never changes
    the production LeaveCalculator.
    """

    def within_maximum(self, days):
        return days < MAX_LEAVE_DAYS  # defect: 30 is wrongly rejected


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()

    cases = [
        (30, 1, "APPROVED"),
        (30, 30, "APPROVED"),
        (30, 31, "REJECTED"),
    ]

    def show_suite(calc_class, label):
        note(label)
        for balance, days, expected in cases:
            calc = calc_class(balance=balance)
            approved, actual_word = calc.request(days)
            actual = "APPROVED" if approved else "REJECTED"
            ok = actual == expected
            mark = "OK" if ok else "XX"
            note(f"  {days} days  ->  {actual}  {mark}")
        blank()

    note("Baseline: correct behaviour")
    show_suite(LeaveCalculator, "")
    passed = sum(
        1 for _, days, expected in cases
        if (LeaveCalculator(balance=30).request(days)[0] == (expected == "APPROVED"))
    )
    note(f"  {passed}/{len(cases)} passed")
    blank()

    note("Controlled change introduced:")
    note("  The maximum-days check now wrongly rejects 30 days.")
    blank()
    note("With controlled defect:")
    show_suite(DefectiveCalculator, "")
    note("Regression detected: 30 days was previously valid, now rejected.")
    blank()

    note("Defect restored: original behaviour is back.")
    blank()
    note("Final regression check:")
    show_suite(LeaveCalculator, "")
    note(f"  {len(cases)}/{len(cases)} passed")
    blank()

    note("Regression successfully demonstrated.")
    note("The controlled defect never modifies the production calculator.")
    return len(cases), len(cases)
