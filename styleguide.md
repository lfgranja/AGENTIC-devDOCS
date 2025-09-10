# Open Source Project Code Style Guide (for AI Agent Consumption)

This document provides actionable style guidelines for the AI agent when generating or modifying code within open source projects.

---

## 1. General Principles

*   **Consistency:** Match the style of surrounding code.
*   **Readability:** Prioritize clear, unambiguous code.
*   **Idiomatic:** Use language-specific and framework-specific idioms.
*   **Maintainability:** Write code that is easy to maintain and extend.

---

## 2. Language-Specific Guidelines

### 2.1. Python (Backend)

*   **Linting/Formatting Tool:** Use `ruff`.
    *   **Lint Command:** `poetry run ruff check .`
    *   **Format Command:** `poetry run ruff format .`
*   **Type Checking Tool:** Use `mypy`.
    *   **Command:** `poetry run mypy .`
*   **Naming Conventions:**
    *   Variables, functions, modules: `snake_case`
    *   Classes: `PascalCase`
    *   Constants: `SCREAMING_SNAKE_CASE`
*   **Docstrings:** Use Google-style docstrings for all public modules, classes, and functions (enforced by `pydocstyle` via `ruff`).
*   **Imports:** Group and alphabetize imports (standard library, third-party, local). `ruff` handles this automatically.
*   **Error Handling:** Use specific `try-except` blocks. Avoid bare `except`. Log errors appropriately.
*   **Testing:** Use `pytest` for writing tests. Follow the Arrange-Act-Assert pattern.

### 2.2. TypeScript / Svelte (Frontend)

*   **Linting Tool:** Use `eslint`.
    *   **Command:** `npm run lint`
*   **Formatting Tool:** Use `prettier`.
    *   **Command:** `npm run format`
*   **Naming Conventions:**
    *   Variables, functions, properties: `camelCase`
    *   Components, types: `PascalCase`
    *   CSS classes: `kebab-case`
*   **TypeScript Usage:** Always use explicit types. Define interfaces/types for complex data.
*   **Svelte:** Follow Svelte's component structure (script, markup, style blocks).
*   **Tailwind CSS:** Prefer utility classes.
*   **Testing:** Use appropriate testing frameworks (e.g., Vitest, Jest).

### 2.3. Rust (Desktop Core)

*   **Formatting Tool:** Use `rustfmt`.
    *   **Command:** `cargo fmt`
*   **Linting Tool:** Use `clippy`.
    *   **Command:** `cargo clippy`
*   **Naming Conventions:**
    *   Functions, variables, modules: `snake_case`
    *   Types (structs, enums, traits): `PascalCase`
    *   Constants: `SCREAMING_SNAKE_CASE`
*   **Error Handling:** Use `Result<T, E>` for recoverable errors. Use `?` operator for propagation.
*   **Testing:** Use built-in testing framework with `#[cfg(test)]` attribute.

### 2.4. Go (CLI Tools)

*   **Formatting Tool:** Use `gofmt`.
    *   **Command:** `gofmt -w .`
*   **Linting Tool:** Use `golangci-lint`.
    *   **Command:** `golangci-lint run`
*   **Naming Conventions:**
    *   Variables, functions, packages: `camelCase`
    *   Exported identifiers: `PascalCase`
*   **Error Handling:** Use Go's idiomatic error handling with `if err != nil`.
*   **Testing:** Use built-in `testing` package. Follow table-driven test patterns.

---

## 3. Commit Message Guidelines

*   **Format:** `type(scope): description`
    *   **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
    *   **Scope (optional):** `backend`, `frontend`, `desktop`, `cli`, `api`, `nemo`, `nautilus`, `dolphin`, `vfs`, `ci`, etc.
    *   **Description:** Concise, imperative, lowercase first letter, no period.
*   **Body (optional):** Explain *why* the change was made.
*   **Footer (optional):** Reference issues (e.g., `Fixes #123`).

---

## 4. Documentation Guidelines

*   **README.md:** Keep it up-to-date with project overview, installation instructions, and usage examples.
*   **Code Comments:** Add comments to explain complex logic or non-obvious implementation details.
*   **API Documentation:** Document all public APIs with clear descriptions of parameters, return values, and examples.
*   **Architecture Documentation:** Maintain documentation explaining the project's architecture and design decisions.

---

## 5. Testing Guidelines

*   **Test Coverage:** Aim for high test coverage, especially for critical functionality.
*   **Test Organization:** Organize tests in a structure that mirrors the source code.
*   **Test Descriptions:** Use descriptive test names that clearly indicate what is being tested.
*   **Mocking:** Use appropriate mocking strategies for external dependencies.
*   **Integration Tests:** Include integration tests for critical workflows.