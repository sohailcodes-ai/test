LINE = "-" * 44


def heading(text):
    print()
    print(text)
    print(LINE)


def note(text):
    print(f"  {text}")


def blank():
    print()


def check(text="PASS"):
    print(f"  {text}")


def fail(text="FAIL"):
    print(f"  {text}")


def table_header(columns):
    """Print a compact table header."""
    parts = []
    for col, width in columns:
        parts.append(f"  {col:<{width}}")
    print("".join(parts))


def table_separator(columns):
    """Print a compact table separator line."""
    parts = []
    for _, width in columns:
        parts.append("  " + "-" * width)
    print("".join(parts))


def table_row(values):
    """Print a compact table row."""
    parts = []
    for val, width in values:
        parts.append(f"  {str(val):<{width}}")
    print("".join(parts))


def summary(count, passed):
    print()
    print(f"  {passed}/{count} passed")
    return passed, count


def pause():
    input("\nPress Enter to return to TESTLAB.")
