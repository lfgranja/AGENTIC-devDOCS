# Complete Development Workflow for Open Source Projects

This document provides a comprehensive development workflow for open source projects, incorporating best practices from various successful projects.

## 1. Repository Setup

1. Fork the repository on GitHub
2. Clone your forked repository locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/PROJECT_NAME.git
   ```
3. Navigate to the project directory:
   ```bash
   cd PROJECT_NAME
   ```
4. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/PROJECT_NAME.git
   ```
5. Verify remotes:
   ```bash
   git remote -v
   ```

## 2. Issue Selection and Branching

### Issue Selection
1. Review open issues on GitHub, prioritizing:
   - Issues with `bug` label
   - Issues with `priority:high` label
   - Issues in the current milestone
2. For new features, create an issue first to discuss the proposal
3. Comment on the issue to indicate you're working on it
4. Assign the issue to yourself if possible

### Branching Strategy
1. Sync with upstream:
   ```bash
   git fetch upstream
   git checkout dev
   git merge upstream/dev
   ```
2. Create a new branch for your issue:
   ```bash
   git switch -c feature/issue-NUMBER-brief-description dev
   ```
   - Replace `NUMBER` with the actual issue number
   - Use descriptive branch names in `kebab-case`
   - Always branch from `dev`

## 3. Development Process

1. Create a detailed TODO list for the issue using `todo_write` tool
2. Follow the project's style guide for coding standards
3. Write tests for new functionality
4. Run existing tests to ensure nothing is broken
5. Follow TDD (Test-Driven Development) where applicable - See detailed implementation guidelines in AGENTIC.md
6. Commit frequently with descriptive messages following Conventional Commits

## 4. Code Quality and Testing

1. Run linting tools:
   - Python: `poetry run ruff check .`
   - TypeScript: `npm run lint`
   - Rust: `cargo clippy`
2. Run formatting tools:
   - Python: `poetry run ruff format .`
   - TypeScript: `npm run format`
   - Rust: `cargo fmt`
3. Run type checking:
   - Python: `poetry run mypy .`
4. Run tests:
   - Python: `poetry run pytest`
   - TypeScript: `npm run test`
   - Rust: `cargo test`
5. Always run project-specific build, linting and type-checking commands after making changes (see Verify (Standards) in AGENTIC.md)

## 5. Commit Guidelines

1. Create a Conventional Commit message:
   ```bash
   type(scope): description

   [optional body]

   [optional footer]
   ```
2. Use appropriate commit types:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation changes
   - `style`: Code style changes (formatting, missing semicolons, etc.)
   - `refactor`: Code refactoring
   - `perf`: Performance improvements
   - `test`: Adding or modifying tests
   - `build`: Build system changes
   - `ci`: CI configuration changes
   - `chore`: Maintenance tasks
   - `revert`: Reverting a previous commit
3. Use appropriate scopes (examples):
   - Backend components: `backend`
   - Frontend components: `frontend`
   - Desktop components: `desktop`
   - CLI components: `cli`
   - API components: `api`
   - File system integrations: `nemo`, `nautilus`, `dolphin`, `vfs`
   - CI/CD components: `ci`
4. Keep descriptions concise, imperative, lowercase first letter, no period
5. Reference issues in the footer:
   ```bash
   Fixes #123
   Closes #456
   ```

## 6. Pre-Push Checklist

1. Stage only changes related to the current issue:
   ```bash
   # Add specific files related to the current issue
   git add path/to/modified-file.ts
   git add path/to/newly-created-test-file.test.ts
   ```
2. Review staged changes:
   ```bash
   git diff --staged
   ```
3. Run all quality checks (linting, formatting, type checking, tests)
4. Create a final commit with a Conventional Commit message:
   ```bash
   git commit -m "type(scope): description. Fixes #ISSUE_NUMBER"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/issue-NUMBER-brief-description
   ```

## 7. Pull Request Process

1. Create a pull request from your branch to the `dev` branch of the upstream repository
2. Use the PR template if available
3. Provide a clear description of the changes
4. Link to the related issue
5. Request review from maintainers
6. Address any feedback received during the review process

## 8. Post-PR Approval Process

Follow strictly the process documented in `.qwen/POSTPR.md` after a PR has been approved. This document contains the complete post-PR approval process with detailed steps for documentation creation, issue tracking, and quality assurance.

**Additionally, as part of the merge process, evaluate all contributions (comments, reviews, suggestions, and enhancements) from `gemini-code-assist`, `qodo-merge-pro`, or any other reviewers. For valid contributions, either incorporate them into new issues or consolidate them into existing ones, ensuring proper categorization, labeling, and priority assignment.**

## 9. Project Architecture and Technology Stack

1. **Modular Design**: The project follows a modular architecture with:
   - Clear separation of concerns
   - Well-defined interfaces between components
   - Reusable components where appropriate

2. **Technology Stack**: Common technologies used in projects:
   - **Backend**: Python with appropriate frameworks
   - **Frontend**: TypeScript with Svelte and Tailwind CSS
   - **Desktop**: Rust with Tauri
   - **Mobile**: Platform-appropriate technologies
   - **CLI**: Python or Go

3. **Development Tools**:
   - **Version Control**: Git with GitHub for hosting
   - **Dependency Management**: Poetry (Python), npm (TypeScript), Cargo (Rust)
   - **Testing**: Pytest (Python), Jest/Vitest (TypeScript), Built-in testing (Rust)
   - **CI/CD**: GitHub Actions
   - **Documentation**: Markdown files in the repository

## 10. Core Development Principles

1. Always adhere to project conventions for style, structure, and architecture (see Core Mandates in AGENTIC.md)
2. Maintain backward compatibility when possible
3. Write clear, comprehensive documentation for new features
4. Follow security best practices (see Security and Safety Rules in AGENTIC.md)
5. Consider performance implications of changes
6. Write tests for all new functionality
7. Use descriptive variable and function names
8. Keep functions small and focused
9. Avoid code duplication
10. Follow the Boy Scout Rule: "Always leave the code better than you found it"

## 11. Collaboration and Communication

1. Participate in discussions on GitHub issues
2. Be respectful and constructive in all interactions
3. Ask for help when needed
4. Provide feedback to other contributors
5. Follow the project's code of conduct

## 12. Security Considerations for GitHub Actions Workflows

### 12.1. Safe Usage of `pull_request_target`

Workflows triggered by `pull_request_target` run with elevated permissions on the base repository, making them powerful but also potentially vulnerable if not used carefully. It is critical to ensure that these workflows never execute untrusted code from the pull request itself to prevent security vulnerabilities.

**Best Practices for `pull_request_target` Workflows:**

1.  **Never Checkout PR Code Directly**: Avoid using `actions/checkout` without specifying a `ref` or `fetch-depth` that explicitly targets the base branch or a trusted commit. If PR code must be accessed, do so in a separate, isolated job with restricted permissions.
2.  **Use Only Trusted Actions**: Only use GitHub Actions from trusted sources (e.g., official GitHub actions or actions from well-known vendors). Always pin actions to a full commit SHA (e.g., `actions/checkout@<full-commit-sha>`) instead of floating or version tags to prevent unexpected changes.
3.  **Execute Only Base Repository Scripts**: If the workflow needs to execute scripts, ensure they are part of the base repository and not supplied by the pull request. Avoid `run` steps that could inadvertently execute malicious code from the PR.
4.  **Minimize `GITHUB_TOKEN` Permissions**: Grant the `GITHUB_TOKEN` (or any other PAT) only the absolute minimum permissions required for the workflow to function. Adhere strictly to the principle of least privilege.
5.  **Implement Guard Conditions**: Consider adding conditional steps or checks to prevent the workflow from proceeding if certain security criteria are not met (e.g., if the PR author is not a trusted contributor).
6.  **Thorough Review**: All `pull_request_target` workflows must undergo rigorous security review.

### 12.2. Personal Access Token (PAT) Management Strategy

A robust strategy for managing Personal Access Tokens (PATs) is essential for maintaining the security of our CI/CD automation. Adhering to the following guidelines will help minimize risks associated with PAT usage:

1.  **Naming Conventions:**
    *   Establish clear and consistent naming conventions for PATs (e.g., `repo-name_ci-purpose_env`).
    *   Include information about the PAT's purpose, scope, and associated repository/environment in its name or description.

2.  **Principle of Least Privilege:**
    *   Grant PATs only the absolute minimum scopes (permissions) required for their intended function. Avoid granting broad or unnecessary permissions.
    *   Regularly review PAT scopes to ensure they remain aligned with current needs and revoke any excessive permissions.

3.  **Rotation and Lifecycle Management:**
    *   Implement a policy for regular PAT rotation (e.g., quarterly or semi-annually) to limit the window of exposure if a PAT is compromised.
    *   Define a clear lifecycle for PATs, including creation, usage, and timely revocation when no longer needed (e.g., when a project is archived or a user leaves the team).
    *   Utilize GitHub's features for PAT expiration where possible.

4.  **Secure Storage and Usage:**
    *   Never hardcode PATs directly into workflow files or repositories.
    *   Store PATs securely as GitHub Secrets and access them via `secrets.PAT_NAME` in workflows.
    *   Avoid exposing PATs in logs or build outputs.