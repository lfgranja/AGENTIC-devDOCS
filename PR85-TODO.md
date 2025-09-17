# TODO List for PR #85: docs: Document tool usage order with MCP clarification

This document outlines the remaining tasks to get PR #85 merged, addressing all feedback and ensuring CI passes.

## 1. Address Critical CI Failure (SyntaxError in `create_issues.py`)

**Context:** The GitHub Actions CI is failing with a `SyntaxError: unterminated string literal` in `AGENTIC/devDOCS/create_issues.py` at line 386. This is blocking the PR from being merged. Previous attempts to fix this programmatically have failed due to the file's large size and duplicated code making `replace` operations unreliable.

**Action:** **[PENDING MANUAL INTERVENTION]** Manually fix the `SyntaxError` in `AGENTIC/devDOCS/create_issues.py`. This involves:
    *   Identifying the exact malformed regex string at line 386 (and potentially other similar malformed regexes in the duplicated code block).
    *   Correcting the unterminated string literal by adding the missing closing quote and `$` anchor.
    *   Removing the duplicated `IssueCreator` class and related functions to prevent future issues with `replace` and to clean up the codebase.

**Verification:** After manual fix, run local tests and linting (`ruff check .`, `mypy .`) to ensure no new errors are introduced.

## 2. Address Remaining Review Comments from `qodo-merge-pro[bot]`

### 2.1. Safety Guidance (Medium priority)

**Context:** The shell command section references an "Explain Critical Commands" rule; `qodo-merge-pro[bot]` suggests linking to or restating the concrete criteria for what counts as critical and what must be explained (dry-run flags, destructive operations, paths) to make the guidance actionable.

**Action:** Update `AGENTIC/AGENTIC.md` to explicitly define the criteria for "Explain Critical Commands" within the "Execute Terminal Commands" section.

**Verification:** Review the updated section in `AGENTIC.md` for clarity and completeness.

### 2.2. Fallback Criteria (Medium priority)

**Context:** The error handling and fallback guideline is broad; `qodo-merge-pro[bot]` suggests adding explicit examples or decision points (timeouts, missing data, permission errors) for when to escalate from one tier to the next to reduce ambiguity.

**Action:** Update `AGENTIC/AGENTIC.md` to include explicit examples of failure conditions that might trigger a fallback in the "Error Handling and Fallback" section.

**Verification:** Review the updated section in `AGENTIC.md` for clarity and completeness.

## 3. Acknowledge and Plan for High-Level Suggestion

### 3.1. Programmatic Enforcement of Tool Usage Hierarchy (High impact)

**Context:** `qodo-merge-pro[bot]` suggests that relying on prompt documentation is insufficient and recommends programmatically enforcing the tool usage order within the agent's tool selection logic.

**Action:** This is an architectural enhancement that is outside the scope of this documentation-focused PR. A new issue (#86: "Feature: Implement programmatic enforcement of tool usage hierarchy") has already been created to track this. No further action is required within this PR beyond acknowledging the suggestion.

**Verification:** Confirm that Issue #86 exists and accurately reflects the suggestion.

## 4. Final Review and Merge Preparation

**Context:** After all code and documentation changes are implemented and verified, the PR will be ready for final review and merging.

**Action:**
    *   Perform a final review of all changes in the PR.
    *   Ensure all CI checks pass.
    *   Request a final review from relevant stakeholders.

---