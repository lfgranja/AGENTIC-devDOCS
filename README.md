# AGENTIC-devDOCS

Comprehensive guidelines and workflows for AI-powered software development agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains comprehensive guidelines for AI-powered software development agents, including behavioral directives, workflow processes, and best practices.

## Main Documents

- [`AGENTIC/AGENTIC.md`](AGENTIC/AGENTIC.md) - Behavioral guidelines for agents
- [`AGENTIC/WORKFLOW.md`](AGENTIC/WORKFLOW.md) - Development workflow for open source projects
- [`AGENTIC/POSTPR.md`](AGENTIC/POSTPR.md) - Post-PR approval process documentation
- [`AGENTIC/QWEN.md`](AGENTIC/QWEN.md) - Qwen-specific directives
- [`AGENTIC/GEMINI.md`](AGENTIC/GEMINI.md) - Gemini-specific guidelines

## Testing

This project includes unit tests for the automation scripts. To run the tests:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the tests:
   ```bash
   python run_tests.py
   ```

   Or run directly with pytest:
   ```bash
   python -m pytest tests/ -v
   ```

## Configuration

The automation tools support configuration files for easier usage. Configuration files can be in JSON or YAML format and support all the command-line options. See [`AGENTIC/devDOCS/README.md`](AGENTIC/devDOCS/README.md) for more details.

## Attribution

The initial content for `AGENTIC/AGENTIC.md` was derived from the [Google Gemini CLI system prompt](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/Open%20Source%20prompts/Gemini%20CLI/google-gemini-cli-system-prompt.txt).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
