# Post-Push Documentation Generation Process

This document describes the automated process for generating development documentation after a push to a branch, particularly after a PR has been approved.

## Trigger

The documentation generation process is triggered automatically after a push to a branch that has an associated PR, or when a PR is approved.

## Process Steps

### 1. Identify Changed Files
The system identifies all files that were modified in the push, focusing on:
- Source code files
- Test files
- Configuration files
- Documentation files

### 2. Analyze Changes
The system analyzes the changes to identify:
- New features implemented
- Bugs fixed
- Performance improvements
- Refactoring work
- Test additions or modifications

### 3. Generate LESSONS_LEARNED Documentation
Based on the analysis, the system generates or updates the LESSONS_LEARNED{PR_NUMBER}.md file with:

1. **Technical Challenges**: Identification of any technical challenges encountered and their solutions
2. **Design Decisions**: Key design decisions made during implementation and their rationale
3. **Unexpected Issues**: Any unexpected issues or bugs discovered during development
4. **Performance Considerations**: Performance-related insights and optimizations
5. **Testing Strategies**: Effective testing strategies used during development
6. **Deviations**: Any deviations from the original plan and reasons for them

### 4. Generate FUTURE_WORK_TODO Documentation
The system generates or updates the FUTURE_WORK_TODO{PR_NUMBER}.md file with:

1. **Areas for Improvement**: Identified areas where the implementation could be improved
2. **Potential Optimizations**: Possible optimizations for performance, memory usage, etc.
3. **Related Features**: Ideas for related features that could be implemented
4. **Technical Debt**: Any technical debt introduced and plans to address it
5. **Extension Ideas**: Ideas for extending the current implementation

### 5. Generate ISSUES_TO_CREATE Documentation
The system generates or updates the ISSUES_TO_CREATE{PR_NUMBER}.md file with:

1. **Issue Descriptions**: Detailed descriptions of issues that should be created
2. **Labels**: Appropriate labels for each issue (e.g., enhancement, bug, technical debt)
3. **Milestones**: Assignment to appropriate milestones if applicable
4. **Priority**: Priority levels for each issue (high, medium, low)
5. **Complexity**: Estimated complexity of each issue (low, medium, high)
6. **Context**: Relevant context and background information for each issue

## Documentation Format

All generated documentation follows the formats specified in the example files in devDOCS/example-pr-xyz/:

- LESSONS_LEARNED{PR_NUMBER}.md
- FUTURE_WORK_TODO{PR_NUMBER}.md
- ISSUES_TO_CREATE{PR_NUMBER}.md

## Review Process

After generation, the documentation is reviewed by:
1. The developer who made the changes
2. A designated reviewer or maintainer
3. The system checks for completeness and adherence to the format

## Storage

The generated documentation is stored in the devDOCS/{branch-name-or-PR-number}/ directory, with filenames following the naming convention:
- LESSONS_LEARNED{PR_NUMBER}.md
- FUTURE_WORK_TODO{PR_NUMBER}.md
- ISSUES_TO_CREATE{PR_NUMBER}.md

## Updates

The documentation is updated automatically with each new push to the branch, with:
- New information added to existing sections
- Outdated information marked as such or removed
- Cross-references to related documentation

## Integration with CI/CD

The documentation generation process is integrated with the CI/CD pipeline:
1. Runs automatically on each push to a branch with an associated PR
2. Fails the build if documentation cannot be generated properly
3. Posts a comment on the PR with links to the generated documentation
4. Notifies relevant team members of documentation updates

## Manual Updates

Developers can manually update the documentation at any time by:
1. Editing the files directly in the devDOCS/{branch-name-or-PR-number}/ directory
2. Following the established formats
3. Committing and pushing the changes

## Quality Assurance

The system ensures documentation quality by:
1. Validating the format of generated documentation
2. Checking for completeness of required sections
3. Ensuring consistency in terminology and style
4. Verifying that all identified issues have sufficient detail for implementation