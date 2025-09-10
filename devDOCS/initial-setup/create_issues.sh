#!/bin/bash

# Script to create GitHub issues from documentation
# You need to authenticate with GitHub CLI first using 'gh auth login'

REPO="lfgranja/AGENTIC-devDOCS"

echo "Creating issues for AGENTIC-devDOCS project..."

# Issue 1: Add Comprehensive LICENSE File
gh issue create \
  --repo $REPO \
  --title "Add comprehensive LICENSE file to repository" \
  --body "Add a proper LICENSE file to the repository that clearly specifies the licensing terms for the project. The file should include the full text of the license and any necessary copyright information.

**Context:** The project currently references a LICENSE file, but it may not be properly set up with the full license text. A comprehensive license file is essential for clarifying the terms under which the project can be used, modified, and distributed." \
  --label "documentation"

# Issue 2: Expand CONTRIBUTING.md with Detailed Guidelines
gh issue create \
  --repo $REPO \
  --title "Expand CONTRIBUTING.md with detailed contribution guidelines" \
  --body "Enhance the CONTRIBUTING.md file with more detailed guidelines for contributors, including code style guidelines, testing requirements, documentation standards, and the review process.

**Context:** While the project has a basic CONTRIBUTING.md file, it could be expanded with more detailed information to help new contributors understand the project's expectations and processes." \
  --label "documentation"

# Issue 3: Create Architecture Documentation for Automation Tools
gh issue create \
  --repo $REPO \
  --title "Create architecture documentation for automation tools" \
  --body "Develop comprehensive architecture documentation that explains how the automation tools (generate_docs.py and create_issues.py) work together, their data flow, and their internal structure.

**Context:** Users and contributors need to understand how the automation tools work to effectively use and contribute to them. Detailed architecture documentation would help with onboarding and maintenance." \
  --label "documentation"

# Issue 4: Add Unit Tests for Python Scripts
gh issue create \
  --repo $REPO \
  --title "Add unit tests for Python automation scripts" \
  --body "Implement unit tests for the generate_docs.py and create_issues.py scripts to ensure their functionality is working correctly and to prevent regressions during development.

**Context:** Currently, the automation scripts lack unit tests, which makes it difficult to ensure their correctness and prevents confident refactoring. Adding unit tests would improve the reliability and maintainability of the codebase." \
  --label "enhancement,test"

# Issue 5: Implement CI/CD Pipeline with GitHub Actions
gh issue create \
  --repo $REPO \
  --title "Implement CI/CD pipeline with GitHub Actions" \
  --body "Set up a CI/CD pipeline using GitHub Actions to automate testing, code quality checks, and documentation generation on each pull request and push to the main branch.

**Context:** A CI/CD pipeline would automate quality checks and testing, ensuring that all contributions meet the project's standards and that issues are caught early in the development process." \
  --label "enhancement,ci"

# Issue 6: Add Configuration Support for Automation Tools
gh issue create \
  --repo $REPO \
  --title "Add configuration support for automation tools" \
  --body "Implement configuration file support for the automation tools to allow users to customize their behavior without modifying the code. This should include options for different output formats, API keys, and other settings.

**Context:** Currently, the automation tools require command-line arguments for all customization. Adding configuration file support would improve usability and make it easier to use the tools in different environments." \
  --label "enhancement"

echo "All issues have been created successfully!"