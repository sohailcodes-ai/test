TESTLAB
=======

Software Testing Laboratory

A small terminal application that demonstrates ten software testing
techniques using one simple subject under test: a Leave Calculator.

It is intended for teaching BCA students about software testing through
concrete, executable examples. There is no database, no authentication,
no web interface, and no AI.

Application under test
----------------------

The Leave Calculator is a small leave request system with these rules:

- Requested leave must be greater than 0.
- Requested leave cannot exceed the available balance.
- Requested leave cannot exceed the allowed maximum (30 days).
- Leave type must be a recognised type (casual, sick, earned).
- Valid requests are approved and reduce the balance.

Testing techniques demonstrated
-------------------------------

The ten demonstrations cover four different kinds of testing. They are not
all the same category:

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

Each technique follows the same teaching flow: an explanation, the aspect
under test, the test cases, execution, expected vs actual results, PASS/
FAIL, and a short reason why those cases demonstrate the technique.

How to run
----------

Requires Python 3. No external dependencies.

Interactive menu:

    python testlab.py

Run everything and see a summary:

    python testlab.py all

Run a single technique:

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

You can also run the package directly:

    python -m testlab

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

Running the project's own tests:

    python -m unittest discover -s tests

Limitations
-----------

- This is a demonstration tool, not a production leave management system.
- The Leave Calculator is intentionally small; real systems have many more
  rules.
- The testing demonstrations are illustrative, not a replacement for a
  full test suite.
- Data is held in memory only; nothing is persisted.
