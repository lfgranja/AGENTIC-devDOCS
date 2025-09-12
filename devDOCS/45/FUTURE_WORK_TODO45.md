# Future Work and TODOs from PR #45

1.  **Move Items Between Columns**: The current workflow only adds new PRs to a single column. A future enhancement would be to move the PR to different columns based on its status (e.g., move to "Done" when merged, or to a "Changes Requested" column if a review requests changes).

2.  **Add Issues to Projects**: We can create a similar workflow that automatically adds newly created *issues* to the project board, not just pull requests. This would provide a unified view of all work in the project.

3.  **Error Handling for Project Triage**: The current workflow assumes the project and column exist. We could add a step to verify their existence or create them if they are missing, making the workflow more resilient.
