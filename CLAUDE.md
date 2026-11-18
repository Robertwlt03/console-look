# console-look: working notes for Claude

## Toolchain

- Python 3.13 or newer, standard library only: `src/console_look.py` is the whole Python half.
- Swift 6 package `ConsoleLook`: `Sources/ConsoleLook/Console.swift`.
- swift format (`.swift-format`) and SwiftLint (`.swiftlint.yml`), lines at most 100 characters.

## Commands

- Python tests: `PYTHONPATH=src python3 -m unittest discover -s Tests`
- Swift tests: `swift test`
- Format check: `swift format lint --strict --recursive Sources Tests Package.swift`
- SwiftLint: `swiftlint lint --quiet --strict`

## Hard rules

- No dependency beyond the Python standard library and Foundation.
- Python and Swift draw the same pieces with the same marks, colors and spacing; a change to one
  half goes into the other in the same commit, or the README says why it does not.
- Text goes out through `show`, `relay` and `data`; only cursor codes (spinner, list redraw,
  hidden cursor) may be printed directly.

## Where things go

- Python code and its command line: `src/console_look.py`
- Swift code: `Sources/ConsoleLook/`
- Tests: `Tests/test_console_look.py` (Python), `Tests/ConsoleLookTests/` (Swift)

## Before every commit

Run both test suites, the format check and SwiftLint; add a line to `CHANGELOG.md` under a new
version for anything a user notices.

## Git

- English everywhere; commit messages follow Conventional Commits (`feat:`, `fix:`, `docs:` …).
- Work on a branch and merge into `main` through a pull request with green CI.
- A release is a tag `vX.Y.Z` that matches `pyproject.toml` and `CHANGELOG.md`.
