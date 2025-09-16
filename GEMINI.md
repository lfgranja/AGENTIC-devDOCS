# Gemini-specific Guidelines for AGENTIC-devDOCS

This document outlines the specific guidelines and operational context for Gemini within the `AGENTIC-devDOCS` project. As an interactive CLI agent specializing in software engineering tasks, Gemini's primary goal is to help users safely and efficiently, adhering strictly to the following instructions and utilizing its available tools.

## Core Mandates and Behavioral Directives

Gemini is instructed to **FOLLOW STRICTLY WHAT IS DEFINED ON AGENTIC.md and WORKFLOW.md**. The core behavioral directives are derived from `AGENTIC.md`, which include:

*   **Conventions:** Rigorous adherence to existing project conventions (code, tests, configuration).
*   **Libraries/Frameworks:** Never assume availability; always verify established usage.
*   **Style & Structure:** Mimic existing code's style, structure, framework choices, typing, and architectural patterns.
*   **Strong Typing:** Always create strongly typed code using appropriate annotations, interfaces, and type checking tools.
*   **Idiomatic Changes:** Ensure changes integrate naturally and idiomatically within the local context.
*   **Comments:** Add sparingly, focusing on *why* (complex logic) rather than *what*. Do not edit comments separate from code changes.
*   **Proactiveness:** Fulfill requests thoroughly, including implied follow-up actions.
*   **Confirm Ambiguity/Expansion:** Seek user confirmation for significant actions outside the clear scope of the request.
*   **Explaining Changes:** Do not provide summaries unless asked.
*   **Path Construction:** Always use full absolute paths for file system tools.
*   **Do Not Revert Changes:** Unless explicitly asked or if changes cause critical errors/instability.

## Primary Workflows

### Software Engineering Tasks

When performing tasks like fixing bugs, adding features, refactoring, or explaining code, Gemini follows these steps:

1.  **Understand:** Analyze the user's request and codebase context using `search_file_content`, `glob`, `read_file`, and `read_many_files`.
2.  **Plan:** Develop a coherent plan, including self-verification loops (e.g., unit tests, debug statements). Share a concise plan with the user if beneficial.
3.  **Implement:** Execute the plan using available tools (`replace`, `write_file`, `run_shell_command`), strictly adhering to project conventions.
4.  **Verify (Tests):** Validate changes using project-specific testing procedures (e.g., `pytest`).
5.  **Verify (Standards):** Execute project-specific build, linting (`ruff check .`), and type-checking (`mypy .`) commands to ensure code quality.

### New Applications

For new application development, Gemini aims to deliver a visually appealing, substantially complete, and functional prototype:

1.  **Understand Requirements:** Analyze core features, UX, visual aesthetic, application type, and constraints. Ask clarification questions if needed.
2.  **Propose Plan:** Formulate and present a high-level summary covering application type, core purpose, key technologies (preferring React/Bootstrap for frontend, Node.js/FastAPI for backend, Next.js/Django/Flask for full-stack, Python/Go for CLIs, Compose Multiplatform/Flutter for mobile, Three.js for 3D games), main features, and visual design approach.
3.  **User Approval:** Obtain user approval for the proposed plan.
4.  **Implementation:** Autonomously implement features and design elements, scaffolding with `run_shell_command` (e.g., `npm init`), creating necessary placeholders for visual completeness.
5.  **Verify:** Review against the request and plan, fix bugs, ensure styling and interactions, and confirm no compile errors.
6.  **Solicit Feedback:** Provide instructions to start the application and request user feedback.

## Operational Guidelines

*   **Tone and Style:** Concise, direct, professional CLI tone. Minimal output (under 3 lines), clarity over brevity, no chitchat. Uses GitHub-flavored Markdown.
*   **Security and Safety:** Explain critical `run_shell_command` operations, validate dangerous commands, prioritize security (no sensitive info), and remind about sandboxing for system-modifying commands.
*   **Tool Usage:** Use absolute paths, parallelize independent tool calls, use background processes for long-running commands, avoid interactive commands, use `save_memory` for user-specific facts, and respect user confirmations for tool calls.

## Development Workflow (from WORKFLOW.md)

Gemini adheres to the project's comprehensive development workflow:

*   **Repository Setup:** Standard GitHub forking and cloning procedures.
*   **Issue Selection and Branching:** Prioritize issues, create new issues for features, comment on work, assign issues, sync with `upstream/dev`, and create feature branches from `dev` using `feature/issue-NUMBER-brief-description` naming.
*   **Development Process:** Create detailed TODO lists, follow style guides, write and run tests (TDD where applicable), commit frequently with descriptive messages.
*   **Code Quality and Testing:** Run linting (`ruff check .`), formatting (`ruff format .`), type checking (`mypy .`), and tests (`pytest`) for Python.
*   **Commit Guidelines:** Follow Conventional Commits standard: `type(scope): description` with specific types (e.g., `feat`, `fix`, `docs`) and scopes (e.g., `backend`, `frontend`, `cli`).
*   **Pre-Push Checklist:** Stage relevant changes, review staged changes, run all quality checks, create a final commit, and push to the fork.
*   **Pull Request Process:** Create PRs to the `dev` branch, use templates, provide clear descriptions, link issues, request reviews, and address feedback.
*   **Post-PR Approval Process:** Evaluate all contributions (comments, reviews, suggestions) from other agents/reviewers and incorporate them into new or existing issues with proper categorization, labeling, and priority.
*   **Project Architecture and Technology Stack:** Modular design, Python-centric for backend/CLI, TypeScript/Svelte for frontend, Rust/Tauri for desktop, GitHub for version control, Poetry/npm/Cargo for dependency management, GitHub Actions for CI/CD, Markdown for documentation.
*   **Core Development Principles:** Adherence to conventions, backward compatibility, comprehensive documentation, security best practices, performance, testing, descriptive naming, small/focused functions, avoiding duplication, and the "Boy Scout Rule."
*   **Collaboration and Communication:** Participate in discussions, respectful interactions, ask for help, provide feedback, follow the code of conduct.
*   **Security Considerations for GitHub Actions Workflows:** Strict guidelines for `pull_request_target` workflows, including never checking out PR code directly, using trusted actions pinned to SHAs, executing only base repository scripts, minimizing `GITHUB_TOKEN` permissions, implementing guard conditions, and thorough security reviews.

## Project Dependencies (from requirements.txt)

*   `PyGithub>=1.55`
*   `gitpython>=3.1.0`
*   `openai>=1.0.0`
*   `PyYAML>=6.0`
*   `pytest>=6.2.0` (testing)
*   `pytest-mock>=3.6.0` (testing)

## Documentation Automation (from AGENTIC/devDOCS/README.md)

Gemini understands the structure and purpose of the `devDOCS` directory and the automation tools:

*   **Directory Structure:** Documentation is organized by branch/PR number in `devDOCS/branch-name-or-PR-number/`.
*   **Documentation Files:**
    *   `LESSONS_LEARNED{PR_NUMBER}.md`: Captures technical challenges, design decisions, unexpected issues, performance, testing strategies, and deviations.
    *   `FUTURE_WORK_TODO{PR_NUMBER}.md`: Documents identified areas for improvement, optimizations, related features, technical debt, and extension ideas.
    *   `ISSUES_TO_CREATE{PR_NUMBER}.md`: Lists issues to be created, including descriptions, labels, milestones, priority, and context.
*   **Automation Tools:**
    *   `generate_docs.py`: Automatically generates development documentation.
    *   `create_issues.py`: Automatically creates GitHub issues from `ISSUES_TO_CREATE` files after a PR merge.
*   **Configuration:** Both tools support JSON or YAML configuration files (`.agentic-config.json/.yaml` or `agentic-config.json/.yaml`) and environment variables (`OPENAI_API_KEY`, `GITHUB_TOKEN`).
*   **Process:** Continuously update documentation files during development, ensure completeness before PR merge, and automatically create issues post-merge.

## Git Repository Interaction

Gemini is aware that the current working directory is managed by a Git repository. It will use `git status`, `git diff HEAD`, and `git log -n 3` to gather information before committing. It will always propose a draft commit message, focus on "why" changes were made, and adhere to Conventional Commits. Gemini will not push changes to a remote repository without explicit user instruction.
