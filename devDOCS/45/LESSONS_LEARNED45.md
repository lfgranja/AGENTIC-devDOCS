# Lessons Learned from PR #45

1.  **PAT is Crucial for Project Actions**: The `actions/add-to-project` action requires a Personal Access Token (PAT) with `project` scope. The standard `GITHUB_TOKEN` does not have sufficient permissions. This is a key security consideration for any workflow that interacts with organization- or user-level resources like GitHub Projects.

2.  **Action Parameter Evolution**: The initial research suggested a `labeled` parameter, but further investigation and a correction showed that `column-name` is the correct parameter for specifying a destination column in the current version of the action. This highlights the importance of checking the latest documentation for any third-party action.

3.  **Completing the Automation Cycle**: This workflow completes a full triage cycle: a PR is opened, the `pr-labeler` adds a label, the `auto-assigner` assigns a reviewer based on the label, and the `triage-to-project` workflow adds the PR to a project board for tracking. This demonstrates a powerful, fully automated review pipeline.
