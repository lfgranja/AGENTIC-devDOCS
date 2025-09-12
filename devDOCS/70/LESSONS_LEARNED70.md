# Lessons Learned from PR #70

1.  **Bot Feedback is Critical**: This PR was a direct result of bot feedback (`qodo-merge-pro`) correctly identifying that the schema for `kentaro-m/auto-assign-action` was incorrect. This highlights the importance of carefully reviewing bot suggestions, as they can catch critical functional errors.

2.  **Schema Matters**: The `kentaro-m/auto-assign-action` has distinct schemas for different use cases (`reviewGroups` vs. a list of `reviewers` with a `labels` key). A small difference in the YAML structure can completely change the behavior of the action. Always refer to the action's official documentation for the correct schema.

3.  **Iterative Correction**: The process of fixing this issue was iterative. An initial incorrect fix was made, which was then corrected based on further feedback. This demonstrates the value of a tight feedback loop (code -> review -> correct) in CI/CD development.
