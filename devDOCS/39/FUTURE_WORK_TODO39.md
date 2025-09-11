# Future Work and TODOs from PR #39

1.  **Auto-assign Reviewers Based on Labels**: Now that we have more granular labels, the next logical step is to use these labels to automatically assign reviewers. For example, changes labeled with `python` could auto-assign a Python expert, while `ci` changes could assign a DevOps specialist. This would require a new workflow, likely using an action like `actions/assign-reviewers`.

2.  **Enforce Labeling on all PRs**: We could make the labeler a required check for merging. This would ensure that every PR is categorized before it enters the codebase, making the commit history easier to navigate and understand.

3.  **Create Labels Dynamically**: The current workflow requires that all labels exist in the repository. An advanced improvement would be to have the workflow automatically create a label if it is defined in `labeler.yml` but doesn't yet exist in the repository. This would simplify the process of adding new categories.
