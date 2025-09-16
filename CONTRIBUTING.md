# Contributing to AGENTIC-devDOCS

Thank you for your interest in contributing to AGENTIC-devDOCS! This document provides comprehensive guidelines for contributing to this project, ensuring a smooth and collaborative development process.

## How to Contribute

We welcome contributions of all kinds, from bug reports to new features and documentation improvements.

1.  **Report Issues**: If you find any bugs, have suggestions for improvements, or want to propose a new feature, please open an issue on GitHub. Provide as much detail as possible, including steps to reproduce bugs, expected behavior, and screenshots where applicable.

2.  **Submit Pull Requests**:
    *   **Fork the repository**: Start by forking the `lfgranja/AGENTIC-devDOCS` repository to your GitHub account.
    *   **Create a new branch**: Create a new branch from the `dev` branch for your changes. Use a descriptive branch name, e.g., `feature/issue-123-add-new-feature` or `fix/issue-456-bug-description`.
    *   **Make your changes**: Implement your changes, ensuring they adhere to the project's guidelines outlined below.
    *   **Commit your changes**: Write clear and concise commit messages following the [Conventional Commits](#commit-message-guidelines) standard.
    *   **Submit a pull request**: Open a pull request from your branch to the `dev` branch of the main repository. Provide a clear description of your changes, reference the issue it addresses (e.g., `Fixes #123`), and explain the "why" behind your changes.

## Development Setup

To get started with development, follow these steps:

### Prerequisites

*   **Python**: Ensure you have Python 3.12 or newer installed.

### Environment Setup

1.  **Clone your forked repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/AGENTIC-devDOCS.git
    cd AGENTIC-devDOCS
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running Tests

It's crucial to run tests to ensure your changes haven't introduced any regressions.

*   **Run all tests**:
    ```bash
    python run_tests.py
    ```
*   **Run tests directly with pytest**:
    ```bash
    python -m pytest tests/ -v
    ```

### Code Quality Checks

We use `ruff` for linting and formatting, and `mypy` for type checking to maintain code quality and consistency.

*   **Run linter and formatter (`ruff`)**:
    ```bash
    ruff check .
    ruff format .
    ```
*   **Run type checker (`mypy`)**:
    ```bash
    mypy .
    ```
    *Note: If `ruff` or `mypy` commands are not found, you might need to install them globally or ensure your Python environment is correctly activated.*

## Contribution Guidelines

### Code Style

Adherence to the project's code style is mandatory. Please refer to the [`styleguide.md`](styleguide.md) for detailed language-specific guidelines. Key points include:

*   **Consistency**: Match the style of surrounding code.
*   **Naming Conventions**: Use `snake_case` for variables, functions, and modules; `PascalCase` for classes; and `SCREAMING_SNAKE_CASE` for constants in Python.
*   **Docstrings**: Use Google-style docstrings for all public modules, classes, and functions.
*   **Imports**: Group and alphabetize imports.
*   **Error Handling**: Use specific `try-except` blocks.

### Testing

All new features and bug fixes should be accompanied by appropriate tests.

*   **Test Coverage**: Aim for high test coverage, especially for critical functionality.
*   **Test Organization**: Organize tests in a structure that mirrors the source code (e.g., `tests/test_module.py` for `module.py`).
*   **Test Descriptions**: Use descriptive test names that clearly indicate what is being tested.
*   **Mocking**: Use appropriate mocking strategies for external dependencies (e.g., `pytest-mock`).

### Documentation

Clear and up-to-date documentation is vital for the project's success.

*   **README.md**: Keep the main `README.md` up-to-date with project overview, installation instructions, and usage examples.
*   **Code Comments**: Add comments to explain complex logic or non-obvious implementation details.
*   **API Documentation**: Document all public APIs with clear descriptions of parameters, return values, and examples.
*   **Architecture Documentation**: Maintain documentation explaining the project's architecture and design decisions.

### Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for commit messages. This helps with automated changelog generation and understanding the history of changes.

*   **Format**: `type(scope): description`
    *   **Types**: `feat` (new feature), `fix` (bug fix), `docs` (documentation only changes), `style` (formatting, missing semicolons, etc.), `refactor` (code change that neither fixes a bug nor adds a feature), `perf` (code change that improves performance), `test` (adding missing tests or correcting existing tests), `build` (changes that affect the build system or external dependencies), `ci` (changes to our CI configuration files and scripts), `chore` (other changes that don't modify src or test files), `revert` (reverts a previous commit).
    *   **Scope (optional)**: A noun describing the section of the codebase affected (e.g., `backend`, `frontend`, `cli`, `ci`, `docs`).
    *   **Description**: A concise, imperative, lowercase first letter, no period at the end.
*   **Body (optional)**: A longer explanation of the commit message, explaining *why* the change was made.
*   **Footer (optional)**: Reference issues (e.g., `Fixes #123`, `Closes #456`).

### Pull Request Best Practices

*   **Clear Description**: Provide a detailed description of your changes, including the problem it solves, how it was solved, and any relevant context.
*   **Link Issues**: Always link your pull request to the relevant issue(s) using keywords like `Fixes #`, `Closes #`, or `Resolves #`.
*   **Self-Review**: Before submitting, review your own code for any obvious errors, style violations, or missing tests.

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## Questions?

If you have any questions about contributing, feel free to open an issue for discussion.
