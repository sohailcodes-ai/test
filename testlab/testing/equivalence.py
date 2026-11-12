from testlab.leave import LeaveCalculator
from testlab.common import heading, note, blank, summary

TITLE = "EQUIVALENCE PARTITIONING"

DESCRIPTION = (
    "Equivalence Partitioning divides inputs into groups that the system "
    "treats the same way. We only need one representative value from each "
    "group to test."
)

ASPECT = (
    "Requested leave partitions:\n"
    "  Invalid partition: 0 or below\n"
    "  Valid partition:   1 - 30\n"
    "  Invalid partition: 31 or above"
)


def run():
    heading(TITLE)
    note(DESCRIPTION)
    blank()
    note("Aspect under test:")
    note(ASPECT)
    blank()

    cases = [
        (0, "REJECTED", "0 or below (invalid)", "zero is in the invalid partition"),
        (15, "APPROVED", "1-30 (valid)", "15 is a representative of the valid partition"),
        (31, "REJECTED", "31 or above (invalid)", "31 is in the invalid partition"),
    ]

    passed = 0
    for days, expected, partition, why in cases:
        calc = LeaveCalculator(balance=100)
        approved, actual_word = calc.request(days)
        actual = "APPROVED" if approved else "REJECTED"
        ok = actual == expected
        passed += ok
        mark = "OK" if ok else "XX"
        note(f"  {days:>3} days  [{partition}]  ->  {actual}  {mark}  ({why})")

    print()
    summary(len(cases), passed)
    blank()
    note("One value from each partition is enough because all values in a")
    note("partition are expected to behave the same way.")
    note("This keeps the test count low while covering each class of input.")
    return passed, len(cases)
