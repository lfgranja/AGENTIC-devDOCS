# Future Work and TODOs from PR #36

1.  **Expand Labeler Configuration**: The current `.github/labeler.yml` is very basic, only identifying `documentation` changes. This configuration should be expanded to include more granular rules for different parts of the codebase.
    *   Add labels for `ci`, `bug`, `enhancement`, `python`, `tests`, etc., based on file paths and conventional commit keywords.
    *   Investigate using more complex glob patterns to identify changes in specific modules or components.

2.  **Add a Validation Workflow for `labeler.yml`**: To prevent errors from incorrect syntax in the labeler configuration file, a separate CI workflow could be added. This workflow would run on changes to `.github/labeler.yml` and use a schema validation tool (like `pykwalify` or a JSON Schema validator) to ensure the file structure is correct.

3.  **Re-evaluate the `github-script` Labeler**: The approach that was overwritten during the merge conflict resolution used `actions/github-script` to programmatically determine labels. While we opted for the simpler `actions/labeler`, the scripted approach offers more flexibility. A future task could be to re-evaluate if a hybrid approach or a more advanced script could provide more intelligent labeling without sacrificing clarity.
