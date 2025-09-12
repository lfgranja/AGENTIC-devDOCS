# Issues to Create from PR #67

Based on the future work identified, the following issues should be created:

---

### Issue 1: Refine Project Board Triage for GitHub Projects V2 Status

*   **Title**: `feat(ci): Refine Project Board Triage for GitHub Projects V2 Status`
*   **Description**: The `triage-to-project` workflow currently adds PRs to a Project V2 board but cannot set a specific status column due to `column-name` being unsupported. This issue aims to implement a method to set the PR's status field (e.g., "In Review") within the Project V2 board.

**Tasks**:
*   [ ] Research how to update Project V2 item fields (specifically status) using GitHub Actions (e.g., `actions/github-script` or a dedicated action).
*   [ ] Modify the `triage-to-project.yml` workflow to include a step that sets the desired status field for newly added PRs.
*   [ ] Verify that PRs are correctly added to the project board with the specified status." --label "enhancement,ci"