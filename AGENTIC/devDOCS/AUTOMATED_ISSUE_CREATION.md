# Automated Issue Creation Process After PR Merge

This document describes the automated process for creating issues in the repository after a PR has been merged, based on the ISSUES_TO_CREATE{PR_NUMBER}.md documentation.

## Trigger

The issue creation process is triggered automatically when a PR is merged into the main branch (typically `dev` or `main`).

## Prerequisites

Before the automated issue creation process can run, the following must be true:
1. The PR must be successfully merged
2. The ISSUES_TO_CREATE{PR_NUMBER}.md file must exist in the devDOCS/{PR_NUMBER}/ directory
3. The file must be in the correct format as specified in the documentation standards

## Process Steps

### 1. Parse ISSUES_TO_CREATE Documentation
The system parses the ISSUES_TO_CREATE{PR_NUMBER}.md file to extract:
- Issue titles
- Issue descriptions
- Labels
- Milestones
- Priority levels
- Complexity estimates
- Context information

### 2. Validate Extracted Information
The system validates the extracted information:
- Ensures all required fields are present
- Validates label names against the repository's existing labels
- Validates milestone names against the repository's existing milestones
- Checks for any formatting issues

### 3. Authenticate with Repository
The system authenticates with the repository using appropriate credentials (typically a GitHub token with the necessary permissions).

### 4. Create Issues
For each issue identified in the documentation:
1. Create a new issue in the repository
2. Set the issue title from the documentation
3. Set the issue description, including:
   - Main description from the documentation
   - Context information
   - Any relevant links to the merged PR or related issues
4. Apply labels to the issue
5. Assign to the appropriate milestone if specified
6. Add a comment to the original PR linking to the newly created issue

### 5. Handle Errors
If any issues occur during the creation process:
1. Log the error with details
2. Continue creating other issues if possible
3. Create a summary issue or comment on the PR with details of any failures
4. Notify maintainers of the failures

### 6. Update Documentation
After creating the issues:
1. Update the ISSUES_TO_CREATE{PR_NUMBER}.md file to indicate which issues have been created
2. Add links to the newly created issues
3. Commit and push the updated documentation

## Issue Creation Format

When creating issues, the system follows this format:

### Title
Uses the title specified in the ISSUES_TO_CREATE{PR_NUMBER}.md file.

### Description
The description includes:
1. Main description from the documentation
2. Context information
3. Link to the merged PR
4. Any additional relevant information

### Labels
Applies all labels specified in the documentation, validating them against the repository's existing labels.

### Milestones
Assigns to the specified milestone if it exists in the repository.

### Priority and Complexity
Adds priority and complexity information as labels:
- Priority: `priority:high`, `priority:medium`, `priority:low`
- Complexity: `complexity:high`, `complexity:medium`, `complexity:low`

## Cross-Referencing

The system creates cross-references between related issues and the original PR:
1. Adds a comment to the original PR with links to all created issues
2. Adds links in the issue descriptions back to the original PR
3. Links related issues to each other when appropriate

## Integration with Repository Features

The process integrates with repository features:
1. **Labels**: Uses existing labels or creates new ones if necessary
2. **Milestones**: Assigns to existing milestones
3. **Assignees**: Can assign issues to specific developers if specified
4. **Projects**: Can add issues to repository projects if configured

## Error Handling and Recovery

The system handles errors gracefully:
1. If the ISSUES_TO_CREATE{PR_NUMBER}.md file is missing or malformed, the process fails gracefully
2. If individual issues cannot be created, the process continues with other issues
3. All errors are logged with detailed information
4. Maintainers are notified of any failures

## Notification System

After creating issues:
1. Notifies the PR author of the created issues
2. Notifies maintainers of new issues
3. Posts a summary comment on the merged PR
4. Sends notifications to relevant channels (if configured)

## Manual Override

Maintainers can manually override the automated process:
1. Skip issue creation for specific issues
2. Modify issue details before creation
3. Manually create issues and update the documentation
4. Disable automated issue creation for specific PRs

## Audit Trail

The system maintains an audit trail:
1. Logs all issue creation activities
2. Tracks which issues were created automatically vs. manually
3. Maintains a history of changes to the ISSUES_TO_CREATE{PR_NUMBER}.md file
4. Records any errors or issues encountered during the process

## Configuration

The process can be configured through:
1. Configuration files in the repository
2. Environment variables
3. Repository settings
4. Command-line parameters (for manual runs)

## Testing

The automated issue creation process is tested:
1. With unit tests for individual components
2. With integration tests that simulate the full process
3. With manual testing in a development environment
4. With periodic validation in production