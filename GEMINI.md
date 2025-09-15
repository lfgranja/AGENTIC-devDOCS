# Project Overview

This repository, `AGENTIC-devDOCS`, serves as a comprehensive set of guidelines and workflows for AI-powered software development agents. It is a non-code project, focusing on establishing best practices, development processes, and documentation standards for AI agents. The core of the project is the `AGENTIC` directory, which contains detailed markdown files outlining the expected behavior, workflows, and operational guidelines for an AI agent named "AGENTIC".

The project emphasizes a structured and documentation-driven development process. A key feature is the post-pull request workflow, which involves generating detailed documentation about lessons learned, future work, and issues to be created. This process is facilitated by the `devDOCS` directory, which stores this documentation on a per-pull-request basis.

## Key Files

*   **`README.md`**: Provides a high-level overview of the repository, its purpose, and links to the main documents.
*   **`AGENTIC/AGENTIC.md`**: The core document defining the AI agent's persona, core mandates, operational guidelines, and interaction style. It sets the foundation for the agent's behavior.
*   **`AGENTIC/WORKFLOW.md`**: Outlines a complete development workflow for open source projects, from repository setup and issue selection to coding standards, commit guidelines, and pull request processes.
*   **`AGENTIC/POSTPR.md`**: Details the process to be followed after a pull request is approved. This includes the creation of `LESSONS_LEARNED`, `FUTURE_WORK_TODO`, and `ISSUES_TO_CREATE` documents.
*   **`AGENTIC/devDOCS/README.md`**: Explains the structure and purpose of the `devDOCS` directory, which is used to store development-related documentation for each pull request.
*   **`AGENTIC/GEMINI.md`**: Gemini-specific guidelines.
*   **`AGENTIC/QWEN.md`**: Qwen-specific directives.

## Usage

The contents of this repository are intended to be used as a set of instructions and guidelines for an AI agent. The markdown files in the `AGENTIC` directory should be used as context for the AI agent to understand its role, responsibilities, and the processes it should follow.

The `devDOCS` directory is a living part of the development process. For each pull request, a new subdirectory should be created, and the corresponding documentation (`LESSONS_LEARNED`, `FUTURE_WORK_TODO`, `ISSUES_TO_CREATE`) should be generated and stored there. This ensures that knowledge is captured and a clear path for future development is established.
