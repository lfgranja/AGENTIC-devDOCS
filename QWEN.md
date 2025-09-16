# AGENTIC-devDOCS Project Context

## Project Overview

This repository contains comprehensive guidelines for AI-powered software development agents, including behavioral directives, workflow processes, and best practices. It provides a framework for AI agents to effectively contribute to open source software development projects.

## Main Components

- **AGENTIC.md**: Behavioral guidelines for AI agents
- **WORKFLOW.md**: Development workflow for open source projects
- **POSTPR.md**: Post-PR approval process documentation
- **QWEN.md**: Qwen-specific directives (this file)
- **GEMINI.md**: Gemini-specific guidelines

## Technology Stack

- **Primary Language**: Python (for automation scripts)
- **Testing Framework**: Pytest
- **Dependencies**: PyGithub, GitPython, OpenAI, PyYAML
- **CI/CD**: GitHub Actions
- **Code Quality**: Ruff (linting/formatting), MyPy (type checking)

## Building and Running

### Dependencies

To install dependencies:
```bash
pip install -r requirements.txt
```

### Testing

To run tests:
```bash
python run_tests.py
```

Or directly with pytest:
```bash
python -m pytest tests/ -v
```

## Development Conventions

### Code Style

Follow the guidelines in `styleguide.md`:
- Python: Use `ruff` for linting and formatting
- Use explicit type annotations
- Follow naming conventions (snake_case for variables/functions, PascalCase for classes)

### Git Workflow

Follow the detailed workflow in `WORKFLOW.md`:
1. Fork and clone the repository
2. Create feature branches from `dev`
3. Follow conventional commit messages
4. Create pull requests to `dev` branch
5. Follow the post-PR approval process in `POSTPR.md`

### Documentation

Documentation is generated automatically through GitHub Actions after pushes. Documentation files are stored in the `devDOCS` directory.

## CI/CD Pipelines

The project uses GitHub Actions for continuous integration:
- **Continuous Integration** (`ci.yml`): Runs tests and code quality checks
- **Code Quality** (`code-quality.yml`): Runs additional code quality checks
- **Documentation Generation** (`post_push_documentation.yml`): Generates documentation after pushes
- **Issue Creation** (`post_merge_issue_creation.yml`): Creates GitHub issues from documentation after PR merge

## Key Directories

- `AGENTIC/`: Core guidelines and directives
- `devDOCS/`: Development documentation and generated files
- `tests/`: Unit tests for automation scripts
- `.github/workflows/`: CI/CD pipeline definitions

## Post-PR Process

After a PR is approved and merged, follow the process in `POSTPR.md`:
1. Create documentation in `devDOCS/`:
   - `LESSONS_LEARNED{PR_NUMBER}.md`
   - `FUTURE_WORK_TODO{PR_NUMBER}.md`
   - `ISSUES_TO_CREATE{PR_NUMBER}.md`
2. Automatically create issues from the `ISSUES_TO_CREATE` file
3. Share knowledge and perform follow-up actions