# Unit Tests for AGENTIC-devDOCS Automation Scripts

This directory contains unit tests for the automation scripts in the AGENTIC-devDOCS project.

## Test Files

- `test_create_issues.py` - Tests for the create_issues.py script
- `test_generate_docs.py` - Tests for the generate_docs.py script

## Running Tests

To run the tests, first install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run the tests:

```bash
python -m pytest tests/ -v
```

Or use the test runner script:

```bash
python run_tests.py
```

## Test Coverage

The tests cover:

1. IssueInfo dataclass creation and attribute access
2. IssueCreator initialization with GitHub API mocking
3. DocumentationGenerator initialization and basic functionality
4. File parsing and categorization functions

## Known Issues

The create_issues.py script has some syntax errors that prevent full testing. These would need to be fixed for complete test coverage.

## Future Improvements

1. Fix syntax errors in create_issues.py to enable full test coverage
2. Add tests for the parse_issues_from_file method
3. Add tests for the create_issue method
4. Add integration tests that test the full workflow
5. Add tests for error conditions and edge cases