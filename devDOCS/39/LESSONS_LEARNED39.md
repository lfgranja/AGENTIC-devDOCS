# Lessons Learned from PR #39

1.  **Simplicity of `actions/labeler`**: This task reinforced how straightforward it is to expand the functionality of the `actions/labeler` workflow. The configuration is declarative and easy to read, making it simple to add new rules without changing any code.

2.  **Glob Patterns for Specificity**: Using glob patterns like `AGENTIC/**/*.py` and `tests/**/*.py` is an effective way to create specific rules and avoid conflicts (e.g., labeling a test file as `python` instead of `tests`). This allows for a high degree of control over how labels are applied.

3.  **Iterative Workflow Improvement**: This PR is a perfect example of iterative improvement. We first fixed the broken workflow (Issue #22) and then immediately enhanced it (Issue #37). This two-step process (fix, then enhance) is a robust pattern for evolving CI/CD pipelines.
