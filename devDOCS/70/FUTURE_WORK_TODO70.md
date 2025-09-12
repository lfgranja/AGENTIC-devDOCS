# Future Work and TODOs from PR #70

1.  **Consolidate Reviewer Configuration**: Now that the schema is correct, we can consolidate the configuration. The current setup has a separate rule for each label, even though they all assign the same reviewer. These can be combined into a single rule to make the file more concise.

2.  **Add More Granular Reviewer Groups**: As the team grows, we can create more granular reviewer groups. For example, we could have a `python-core` group and a `python-docs` group, each with different reviewers, and assign them based on more specific labels.

3.  **Test the Auto-Assign Workflow**: We should create a test plan to formally verify that the auto-assign workflow functions as expected in various scenarios (e.g., multiple labels, no matching labels, etc.). This could involve creating test PRs and observing the workflow's behavior.
