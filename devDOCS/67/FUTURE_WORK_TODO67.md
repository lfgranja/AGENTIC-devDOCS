# Future Work and TODOs from PR #67

1.  **Refine `triage-to-project` for Project V2 Status**: Since `column-name` is not supported for GitHub Projects V2, investigate how to set a specific status field (e.g., "Status: In Review") for PRs added to the project board. This might require using `actions/github-script` or a different action.

2.  **Comprehensive Workflow Testing**: Develop a strategy for more comprehensive testing of GitHub Actions workflows, possibly using a dedicated testing framework or more elaborate integration tests that simulate PR events and verify outcomes.

3.  **Standardize `gh` CLI Usage**: Document best practices for using the `gh` CLI within this environment, especially regarding multi-line inputs and shell escaping, to prevent future command execution errors.
