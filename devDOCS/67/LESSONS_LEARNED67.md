# Lessons Learned from PR #67

1.  **CI/CD Debugging is Iterative**: The process of fixing the CI/CD failures highlighted that debugging workflows often requires an iterative approach. Initial corrections might not cover all edge cases or interactions, necessitating further investigation and adjustments.

2.  **`pull_request` vs. `pull_request_target` Nuances**: Reconfirmed the critical difference between `pull_request` and `pull_request_target` events, especially regarding secret access and permissions for PRs from forks. Misunderstanding this can lead to `Resource not accessible by integration` errors.

3.  **Action Parameter Specificity**: The `actions/add-to-project` action requires precise parameter usage. The `column-name` input is not supported for GitHub Projects V2, emphasizing the need to consult the latest action documentation carefully.

4.  **Forcing CI/CD Re-evaluation**: Creating an empty commit (`git commit --allow-empty`) and pushing it is an effective way to force a re-evaluation of all CI/CD workflows on a PR branch, which is useful during debugging.

5.  **Robustness of `gh` CLI**: Encountered some unexpected behavior with `gh` CLI commands (e.g., `--pr` flag, multi-line commit messages). This suggests a need for more robust command construction or a deeper understanding of shell escaping in this environment.
