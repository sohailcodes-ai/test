import argparse
import importlib
import signal
import sys

from testlab.common import pause

TECHNIQUES = {
    "blackbox": "black_box",
    "whitebox": "white_box",
    "unit": "unit",
    "integration": "integration",
    "system": "system",
    "acceptance": "acceptance",
    "regression": "regression",
    "boundary": "boundary",
    "equivalence": "equivalence",
    "decision-table": "decision_table",
}

DISPLAY = {
    "blackbox": "Black-Box Testing",
    "whitebox": "White-Box Testing",
    "unit": "Unit Testing",
    "integration": "Integration Testing",
    "system": "System Testing",
    "acceptance": "Acceptance Testing",
    "regression": "Regression Testing",
    "boundary": "Boundary Value Analysis",
    "equivalence": "Equivalence Partitioning",
    "decision-table": "Decision Table Testing",
}

LINE = "-" * 44


def run_technique(name):
    module_name = TECHNIQUES[name]
    module = importlib.import_module(f"testlab.testing.{module_name}")
    return module.run()


def run_all():
    print()
    print("RUN ALL TESTS")
    print(LINE)
    total_passed = 0
    total_count = 0
    for name in TECHNIQUES:
        passed, count = run_technique(name)
        total_passed += passed
        total_count += count
        print(f"  {DISPLAY[name]:28} {passed}/{count}")
    print()
    print(LINE)
    print(f"  TOTAL{'':25} {total_passed}/{total_count}")
    print()
    if total_passed == total_count:
        print("  All tests passed.")
    else:
        print("  Some tests failed.")
    return total_passed == total_count


def show_menu():
    print()
    print("TESTLAB")
    print("Software Testing Laboratory")
    print()
    print("Leave Calculator")
    print(LINE)
    print()
    print("What would you like to explore?")
    print()
    for i, name in enumerate(TECHNIQUES, 1):
        print(f" {i:2}  {DISPLAY[name]}")
    print()
    print(" A  Run all tests")
    print(" Q  Exit")
    print()


def handle_interrupt(signum, frame):
    print("\n\nExiting TESTLAB.")
    sys.exit(0)


def interactive():
    signal.signal(signal.SIGINT, handle_interrupt)
    while True:
        show_menu()
        try:
            choice = input("Select > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            handle_interrupt(None, None)
        print()

        if choice == "q":
            break
        if choice == "a":
            run_all()
            continue
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(TECHNIQUES):
                name = list(TECHNIQUES)[idx - 1]
                passed, count = run_technique(name)
                print()
                print(f"  {passed}/{count} passed")
                try:
                    pause()
                except (EOFError, KeyboardInterrupt):
                    handle_interrupt(None, None)
                continue
        print("Invalid selection. Try again.")


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="testlab",
        description="TESTLAB - Software Testing Laboratory",
    )
    parser.add_argument(
        "technique",
        nargs="?",
        help="Technique to run (blackbox, whitebox, unit, integration, "
             "system, acceptance, regression, boundary, equivalence, "
             "decision-table) or 'all'.",
    )
    args = parser.parse_args(argv)

    if args.technique is None:
        interactive()
        return

    name = args.technique.lower()
    if name == "all":
        run_all()
        return
    if name not in TECHNIQUES:
        print(f"Unknown technique: {args.technique}")
        print(f"Valid: {', '.join(TECHNIQUES)}, all")
        raise SystemExit(1)

    run_technique(name)
