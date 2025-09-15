# AGENTIC-devDOCS Project Context for Qwen Code

## Project Overview

This repository contains comprehensive guidelines for AI-powered software development agents, including behavioral directives, workflow processes, and best practices. The project provides tools and documentation for automating development documentation generation and GitHub issue creation.

## Project Structure

```
AGENTIC-devDOCS/
├── AGENTIC/                    # Core behavioral guidelines and workflows
│   ├── AGENTIC.md             # Main behavioral guidelines for agents
│   ├── WORKFLOW.md            # Development workflow for open source projects
│   ├── POSTPR.md              # Post-PR approval process documentation
│   ├── QWEN.md                # Qwen-specific directives (this file)
│   ├── GEMINI.md              # Gemini-specific guidelines
│   └── devDOCS/               # Automation tools for documentation and issue creation
│       ├── generate_docs.py   # Generates development documentation
│       ├── create_issues.py   # Creates GitHub issues from documentation
│       ├── config.py          # Configuration management
│       └── ...                # Additional tools and examples
├── tests/                     # Unit tests for automation scripts
├── .github/workflows/         # CI/CD workflows
├── requirements.txt           # Python dependencies
├── README.md                 # Project overview
├── CONTRIBUTING.md           # Contribution guidelines
├── LICENSE                   # MIT License
├── styleguide.md             # Code style guide
├── run_tests.py              # Test runner
└── validate_workflows.py     # Workflow validation script
```

## Core Behavioral Guidelines

Based on AGENTIC.md, the agent should:

1. **Adhere to Conventions**: Rigorously follow existing project conventions when reading or modifying code
2. **Verify Libraries/Frameworks**: Never assume a library is available; verify its usage in the project
3. **Mimic Style**: Match the style, structure, and architectural patterns of existing code
4. **Use Strong Typing**: Always create strongly typed code with appropriate type annotations
5. **Add Comments Sparingly**: Focus on *why* something is done rather than *what* is done
6. **Be Proactive**: Fulfill user requests thoroughly, including reasonable implied follow-up actions
7. **Confirm Ambiguity**: Don't take significant actions beyond the clear scope without confirming with the user
8. **Use Absolute Paths**: Always construct full absolute paths for file system tools

## Development Workflows

Based on WORKFLOW.md, the agent should follow these processes:

### Repository Setup
1. Fork the repository on GitHub
2. Clone your forked repository locally
3. Add the upstream repository
4. Verify remotes

### Issue Selection and Branching
1. Review open issues on GitHub, prioritizing bugs and high-priority issues
2. Comment on the issue to indicate you're working on it
3. Create a new branch for your issue from `dev`

### Development Process
1. Create a detailed TODO list using `todo_write` tool
2. Follow the project's style guide for coding standards
3. Write tests for new functionality
4. Run existing tests to ensure nothing is broken
5. Follow TDD where applicable
6. Commit frequently with descriptive messages following Conventional Commits

### Code Quality and Testing
1. Run linting tools (ruff for Python)
2. Run formatting tools (ruff format for Python)
3. Run type checking (mypy for Python)
4. Run tests (pytest for Python)
5. Always run project-specific build, linting and type-checking commands after changes

### Commit Guidelines
1. Follow Conventional Commits standard
2. Use appropriate commit types (feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert)
3. Use appropriate scopes
4. Keep descriptions concise and imperative
5. Reference issues in the footer

## Automation Tools

The project includes automation tools in the `AGENTIC/devDOCS/` directory:

### Documentation Generation (generate_docs.py)
Automatically generates development documentation based on code changes:
- Creates LESSONS_LEARNED{PR_NUMBER}.md
- Creates FUTURE_WORK_TODO{PR_NUMBER}.md
- Creates ISSUES_TO_CREATE{PR_NUMBER}.md

### Issue Creation (create_issues.py)
Automatically creates GitHub issues from ISSUES_TO_CREATE documentation after a PR has been merged.

### Configuration Management (config.py)
Handles configuration loading from JSON or YAML files.

## Testing

The project uses pytest for testing with the following commands:
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python run_tests.py
# or
python -m pytest tests/ -v
```

## Building and Running

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   python run_tests.py
   ```

3. Validate workflows:
   ```bash
   python validate_workflows.py
   ```

## Development Conventions

### Code Style
1. Follow the style guide in `styleguide.md`
2. For Python code:
   - Use `ruff` for linting and formatting
   - Use `mypy` for type checking
   - Use `pytest` for testing
3. Write clear, comprehensive documentation for new features
4. Follow security best practices

### Documentation
1. Keep README.md up-to-date with project overview and usage examples
2. Add comments to explain complex logic or non-obvious implementation details
3. Document all public APIs with clear descriptions
4. Maintain architecture documentation

### Git Workflow
1. Follow the branching strategy (branch from `dev`)
2. Create descriptive branch names in `kebab-case`
3. Commit frequently with meaningful messages
4. Follow Conventional Commits standard
5. Push to your fork and create pull requests

### Post-PR Process
After a PR is approved but before merging:
1. Create documentation in the `devDOCS/` directory:
   - LESSONS_LEARNED{PR_NUMBER}.md
   - FUTURE_WORK_TODO{PR_NUMBER}.md
   - ISSUES_TO_CREATE{PR_NUMBER}.md
2. After PR is merged, automatically create issues documented in ISSUES_TO_CREATE{PR_NUMBER}.md

## CI/CD Pipelines

The project uses GitHub Actions for continuous integration:
- **Continuous Integration**: Runs tests and code quality checks
- **Post-Push Documentation Generation**: Automatically generates development documentation
- **Post-Merge Issue Creation**: Automatically creates GitHub issues from documentation
- **PR Labeler**: Automatically labels pull requests
- **PR Reviewer Assigner**: Automatically assigns reviewers to pull requests
- **Code Quality and Security**: Runs code quality checks and security scans
- **Release**: Creates GitHub releases when tags are pushed

## Security Considerations

1. Apply security best practices
2. Never expose, log, or commit secrets, API keys, or sensitive information
3. For GitHub Actions workflows using `pull_request_target`:
   - Never checkout PR code directly
   - Use only trusted actions pinned to full commit SHAs
   - Execute only base repository scripts
   - Minimize `GITHUB_TOKEN` permissions
   - Implement guard conditions
   - Thoroughly review workflows

## Key Technologies

- **Backend**: Python
- **Testing**: pytest, pytest-mock
- **Dependencies**: PyGithub, gitpython, openai, PyYAML
- **CI/CD**: GitHub Actions
- **Documentation**: Markdown files
- **Code Quality**: ruff, mypy

## Important Files

- `AGENTIC/AGENTIC.md`: Main behavioral guidelines for agents
- `AGENTIC/WORKFLOW.md`: Development workflow for open source projects
- `AGENTIC/POSTPR.md`: Post-PR approval process documentation
- `AGENTIC/devDOCS/generate_docs.py`: Generates development documentation
- `AGENTIC/devDOCS/create_issues.py`: Creates GitHub issues from documentation
- `requirements.txt`: Python dependencies
- `tests/`: Unit tests for automation scripts
- `.github/workflows/`: CI/CD workflows

This context provides the necessary information for an AI agent to understand and work with the AGENTIC-devDOCS project effectively.