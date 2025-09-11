# Lessons Learned from PR #36

1.  **`pull_request_target` is Essential for Fork Workflows**: The primary issue was a permissions error (`Resource not accessible by integration`). The key lesson is that workflows triggered by `pull_request` from forked repositories receive a read-only `GITHUB_TOKEN`. To perform write actions like adding a label, the workflow must be triggered by `pull_request_target`, which runs in the context of the base repository and has access to the necessary permissions and secrets.

2.  **Verify Workflow Dependencies**: The `actions/labeler` action requires a `.github/labeler.yml` configuration file to function. The workflow was failing silently on this dependency before the permission issue became apparent. It's crucial to ensure all required configuration files for a GitHub Action are present.

3.  **Confirm the Base Branch Name**: An initial assumption was that the development branch was named `dev`. A quick check of remote branches (`git branch -r`) revealed it was actually `main`. This highlights the importance of verifying repository conventions rather than assuming them.

4.  **Handling Merge Conflicts in Workflows**: A significant merge conflict occurred with another labeler workflow implemented using `actions/github-script`. This indicates parallel development on the same functionality. The resolution required a clear decision to stick with the simpler, more configurable `actions/labeler` approach to directly address the original issue's scope.
