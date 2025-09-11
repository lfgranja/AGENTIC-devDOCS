# Issues to Create from PR #41

Based on the future work identified, the following issues should be created:

---

### Issue 1: Update Auto-Assign Reviewer Mapping

*   **Title**: `chore(config): Update auto-assign reviewer mapping`
*   **Description**: The current `.github/auto_assign.yml` file uses placeholder usernames for reviewer assignments. This task is to update the file with a realistic mapping of labels to the actual GitHub usernames or teams responsible for those areas of the code.
*   **Labels**: `enhancement`, `ci`, `documentation`
*   **Tasks**:
    *   [ ] Identify the correct reviewers or teams for the existing labels (`python`, `ci`, `tests`, `documentation`).
    *   [ ] Update the `.github/auto_assign.yml` file with the correct mappings.
    *   [ ] Verify the changes in a test PR.

---

### Issue 2: Automate PR to Project Board Triage

*   **Title**: `feat(ci): Automate PR to Project Board Triage`
*   **Description**: To provide better visibility into the development pipeline, we should create a workflow that automatically adds new pull requests to a specific column on our GitHub Project board. This would complete our automated triage process (label -> assign -> track).
*   **Labels**: `enhancement`, `ci`
*   **Tasks**:
    *   [ ] Research a GitHub Action for interacting with Project boards.
    *   [ ] Design a workflow that triggers when a PR is opened.
    *   [ ] Configure the workflow to add the new PR to a designated "Triage" or "In Review" column on a project board.
