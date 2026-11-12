TESTLAB
=======

Software Testing Laboratory

TESTLAB is a small project I built to demonstrate different software testing techniques. Instead of explaining each technique only through theory, I used a Leave Calculator and wrote real test cases to show how each one works.

The application under test is a simple Leave Calculator with these rules:

- Requested leave must be greater than 0.
- Requested leave cannot exceed the available balance.
- Requested leave cannot exceed the allowed maximum (30 days).
- Leave type must be a recognised type (casual, sick, earned).
- Valid requests are approved and reduce the balance.

I chose the Leave Calculator because it has enough rules to demonstrate different testing approaches meaningfully, but it's still easy to understand without prior domain knowledge.

Testing techniques demonstrated
-------------------------------

The ten demonstrations cover four different kinds of testing. They are not all the same category:

Testing approaches
  Black-Box Testing   - behaviour only, no knowledge of internals
  White-Box Testing   - internal conditions and branches exercised directly

Testing levels
  Unit Testing        - individual functions in isolation
  Integration Testing - multiple components working together
  System Testing      - the complete calculator end to end
  Acceptance Testing  - behaviour checked against business requirements

Testing type
  Regression Testing  - previously passing tests re-run after a change

Test-design techniques
  Boundary Value Analysis     - values at and around input range limits
  Equivalence Partitioning    - one representative from each input partition
  Decision Table Testing      - every combination of conditions covered

Each technique shows an explanation, what is being tested, the test cases, execution results, expected vs actual output, PASS/FAIL, and a short reason why those cases were chosen.

Requirements
------------

- Python 3 (3.8 or later recommended)
- No external dependencies

How to run
----------

Open PowerShell in the project folder:

    cd path\to\test

Check that Python is installed:

    python --version

Run the interactive menu:

    python testlab.py

Run all demonstrations and see a summary:

    python testlab.py all

Run an individual technique:

    python testlab.py blackbox
    python testlab.py whitebox
    python testlab.py unit
    python testlab.py integration
    python testlab.py system
    python testlab.py acceptance
    python testlab.py regression
    python testlab.py boundary
    python testlab.py equivalence
    python testlab.py decision-table

Show help:

    python testlab.py --help

Run the project's own test suite:

    python -m unittest discover -s tests

What you'll see
---------------

When you select a technique, TESTLAB prints a short explanation, then runs the actual test cases against the Leave Calculator. For each case you'll see the input, expected result, actual result, and PASS/FAIL status. At the end it shows how many passed and a short explanation of why those particular cases demonstrate that technique. The results come from real execution — nothing is hard-coded.

Project structure
-----------------

testlab/              - application source
  leave.py            - Leave Calculator (subject under test)
  cli.py              - command line interface
  common.py           - shared output helpers
  testing/            - one module per testing technique
  __main__.py         - python -m testlab entry point
tests/                - automated tests for the project itself
  test_leave.py       - tests of the Leave Calculator
testlab.py            - executable entry script
README.md             - this file

Limitations
-----------

- This is a demonstration tool, not a production leave management system.
- The Leave Calculator is intentionally small; real systems have many more rules.
- The testing demonstrations are illustrative, not a replacement for a full test suite.
- Data is held in memory only; nothing is persisted.
