# Lessons Learned from PR #41

1.  **Leverage Existing Marketplace Actions**: Implementing the auto-assign functionality was significantly simplified by using a pre-existing, well-documented action (`kentaro-m/auto-assign-action`). This reinforces the principle of not reinventing the wheel for common CI/CD tasks.

2.  **Configuration as Code**: Separating the workflow logic (the `auto-assign.yml` workflow file) from the assignment rules (the `auto_assign.yml` configuration file) is a powerful pattern. It allows for easy updates to the reviewer list or rules without touching the core workflow execution logic.

3.  **Security in Tooling**: The repeated failures with multi-line commit messages highlight the security constraints of the execution environment. This forces a more atomic, step-by-step approach to shell commands, which can be safer and easier to debug, even if it requires more steps.
