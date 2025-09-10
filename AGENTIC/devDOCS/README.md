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

## Automation Tools

This directory contains automation tools for generating documentation and creating GitHub issues:

### generate_docs.py

Automatically generates development documentation based on code changes.

Usage:
```bash
python generate_docs.py --changed-files CHANGED_FILES --output-dir OUTPUT_DIR --branch BRANCH [--pr-number PR_NUMBER] [--openai-api-key OPENAI_API_KEY] [--config CONFIG_FILE]
```

### create_issues.py

Automatically creates GitHub issues from ISSUES_TO_CREATE documentation after a PR has been merged.

Usage:
```bash
python create_issues.py --token GITHUB_TOKEN --repo REPO --pr PR_NUMBER --issues-file ISSUES_FILE [--config CONFIG_FILE]
```

### Configuration Support

Both automation tools support configuration files to avoid passing parameters through command line arguments. 
Configuration files can be in JSON or YAML format.

Example JSON configuration (`.agentic-config.json`):
```json
{
  "changed_files": "changed_files.txt",
  "output_dir": "./docs",
  "branch": "main",
  "pr_number": "123",
  "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",
  "github_token": "YOUR_GITHUB_TOKEN_HERE",
  "repo": "owner/repo",
  "pr": 123,
  "issues_file": "ISSUES_TO_CREATE123.md"
}
```

Example YAML configuration (`.agentic-config.yaml`):
```yaml
# Configuration for generate_docs.py
changed_files: "changed_files.txt"
output_dir: "./docs"
branch: "main"
pr_number: "123"
openai_api_key: "YOUR_OPENAI_API_KEY_HERE"

# Configuration for create_issues.py
github_token: "YOUR_GITHUB_TOKEN_HERE"
repo: "owner/repo"
pr: 123
issues_file: "ISSUES_TO_CREATE123.md"
```

Configuration files are automatically detected in the following locations:
1. `.agentic-config.json` or `.agentic-config.yaml` in the current directory
2. `agentic-config.json` or `agentic-config.yaml` in the current directory
3. `.agentic-config.json` or `.agentic-config.yaml` in the user's home directory

Environment variables can also be used:
- `OPENAI_API_KEY` for OpenAI API key
- `GITHUB_TOKEN` for GitHub personal access token

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