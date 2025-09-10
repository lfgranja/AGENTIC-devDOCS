# Developer Documentation (devDOCS)

This directory contains development documentation organized by branch or PR number. Each subdirectory corresponds to a specific branch or PR and contains relevant documentation created during the development process.

## Directory Structure

```
devDOCS/
├── branch-name-or-PR-number/
│   ├── LESSONS_LEARNED{PR_NUMBER}.md
│   ├── FUTURE_WORK_TODO{PR_NUMBER}.md
│   ├── ISSUES_TO_CREATE{PR_NUMBER}.md
│   └── ... (other relevant documentation)
├── another-branch-or-PR-number/
│   ├── LESSONS_LEARNED{PR_NUMBER}.md
│   ├── FUTURE_WORK_TODO{PR_NUMBER}.md
│   ├── ISSUES_TO_CREATE{PR_NUMBER}.md
│   └── ... (other relevant documentation)
└── README.md (this file)
```

## Documentation Files

### LESSONS_LEARNED{PR_NUMBER}.md

This file captures key lessons learned during the development process:

- Technical challenges encountered and how they were solved
- Design decisions made and their rationale
- Unexpected issues or bugs discovered
- Performance considerations
- Testing strategies that proved effective
- Any deviations from the original plan and reasons why

### FUTURE_WORK_TODO{PR_NUMBER}.md

This file documents future work related to the implemented feature or bug fix:

- Identified areas for improvement
- Potential optimizations
- Related features that could be implemented next
- Technical debt introduced (if any) and plans to address it
- Ideas for extending the current implementation

### ISSUES_TO_CREATE{PR_NUMBER}.md

This file contains a list of issues that should be created in the repository based on the work completed and future considerations:

- Detailed descriptions of each issue
- Appropriate labels and milestones
- Priority levels
- Estimated complexity
- Any relevant context or background information

## Process

1. During development, create a subdirectory in devDOCS named after the branch or PR number
2. As you work, continuously update the documentation files with relevant information
3. After a PR is approved but before it's merged, ensure all documentation is complete and accurate
4. After a PR is merged, automatically create the issues documented in ISSUES_TO_CREATE{PR_NUMBER}.md
5. Review and update documentation regularly to keep it current

## Best Practices

- Keep documentation concise but comprehensive
- Use clear, descriptive filenames
- Update documentation regularly as the project evolves
- Cross-reference related documentation when appropriate
- Use markdown formatting for better readability