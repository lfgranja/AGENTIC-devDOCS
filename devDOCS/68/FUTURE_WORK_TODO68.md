# Future Work and TODOs from PR #68

1.  **Automated Security Scanning of Workflows**: Implement a CI check that automatically scans GitHub Actions workflows for security best practice violations, such as unpinned actions or overly permissive tokens. Tools like `StepSecurity` or `OpenSSF Scorecard` could be integrated.

2.  **Centralized PAT Management**: The use of multiple PATs (`ADD_TO_PROJECT_PAT`, `ASSIGNER_PAT`) is becoming necessary. We should document a clear strategy for managing these PATs, including naming conventions, scope guidelines, and rotation policies.

3.  **Refine `pr-reviewer-assigner` Logic**: The `pr-reviewer-assigner` script is currently a simple `if/else` chain. It could be refactored to use a more scalable and configurable approach, such as reading a mapping from a YAML file, similar to how the `auto-assign-action` works.
