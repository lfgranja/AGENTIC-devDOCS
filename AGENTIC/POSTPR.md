# Post-PR Approval Process

This document contains the complete post-PR approval process with detailed steps for documentation creation, issue tracking, and quality assurance.

## 1. Documentation Creation

After a PR has been approved, create the following documentation in the `devDOCS/` directory:

### 1.1. LESSONS_LEARNED{PR_NUMBER}.md

Create a document that captures key lessons learned during the development process:

- Technical challenges encountered and how they were solved
- Design decisions made and their rationale
- Unexpected issues or bugs discovered
- Performance considerations
- Testing strategies that proved effective
- Any deviations from the original plan and reasons why

### 1.2. FUTURE_WORK_TODO{PR_NUMBER}.md

Document future work related to the implemented feature or bug fix:

- Identified areas for improvement
- Potential optimizations
- Related features that could be implemented next
- Technical debt introduced (if any) and plans to address it
- Ideas for extending the current implementation

### 1.3. ISSUES_TO_CREATE{PR_NUMBER}.md

Based on the work completed and future considerations, create a list of issues that should be created in the repository:

- Detailed descriptions of each issue
- Appropriate labels and milestones
- Priority levels
- Estimated complexity
- Any relevant context or background information

## 2. Issue Creation Process

After the PR is merged, automatically create the issues documented in `ISSUES_TO_CREATE{PR_NUMBER}.md`:

1. Parse the ISSUES_TO_CREATE{PR_NUMBER}.md file
2. For each issue:
   - Create a new issue in the repository
   - Apply appropriate labels (e.g., `enhancement`, `bug`, `technical debt`, `help wanted`)
   - Assign to the appropriate milestone if applicable
   - Set priority levels using labels (e.g., `priority:high`, `priority:medium`, `priority:low`)
   - Include all relevant context and background information from the document
3. Link related issues to each other
4. Update the ISSUES_TO_CREATE{PR_NUMBER}.md file to indicate which issues have been created

## 3. Quality Assurance

Before considering the post-PR process complete:

1. Verify that all documentation has been properly created and is accurate
2. Confirm that all issues identified for creation have been created
3. Ensure that the newly created issues have appropriate labels, milestones, and descriptions
4. Review the code changes one final time to ensure they meet all project standards
5. Update any relevant project documentation (README.md, architecture docs, etc.) if necessary

## 4. Knowledge Sharing

1. Share key learnings with the team through appropriate channels
2. Update internal knowledge bases or wikis if applicable
3. Consider writing a blog post or technical article if the work is particularly noteworthy
4. Present the work in team meetings or demos if appropriate

## 5. Follow-up Actions

1. Monitor the created issues to see if they receive community interest
2. Be prepared to provide additional context or clarification on created issues
3. Track the implementation of future work items
4. Gather feedback from users or other developers on the implemented features