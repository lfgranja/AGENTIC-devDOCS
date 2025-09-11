# Future Work and TODOs from PR #41

1.  **Refine Reviewer Mapping**: The current `.github/auto_assign.yml` uses a placeholder reviewer. This configuration needs to be updated with a realistic map of labels to actual GitHub usernames or teams.

2.  **Explore Advanced Assignment Rules**: The `kentaro-m/auto-assign-action` might support more advanced features. We could investigate using different numbers of reviewers for different labels or assigning reviewers based on file paths in addition to labels.

3.  **Integrate with Project Boards**: To complete the triage process, a new workflow could be created that automatically adds newly labeled and assigned PRs to a specific column on a GitHub Project board. This would provide full visibility into the review pipeline.
