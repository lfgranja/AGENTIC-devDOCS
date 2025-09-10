#!/usr/bin/env python3
"""
Example script demonstrating how to use the configuration support.
"""

import os
import sys
import json

# Add the devDOCS directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'AGENTIC', 'devDOCS'))

from config import ConfigManager


def create_example_config():
    """Create example configuration files"""
    # Create JSON example
    json_config = {
        "changed_files": "example_changed_files.txt",
        "output_dir": "./example_docs",
        "branch": "main",
        "pr_number": "456",
        "openai_api_key": "sk-example-openai-key"
    }
    
    with open('.agentic-config.json', 'w') as f:
        json.dump(json_config, f, indent=2)
    
    print("Created .agentic-config.json")
    
    # Create YAML example
    yaml_config = """# Example configuration for generate_docs.py
changed_files: "example_changed_files.txt"
output_dir: "./example_docs"
branch: "main"
pr_number: "456"
openai_api_key: "sk-example-openai-key"

# Example configuration for create_issues.py
github_token: "ghp_example_github_token"
repo: "owner/example-repo"
pr: 456
issues_file: "example_ISSUES_TO_CREATE456.md"
"""
    
    with open('.agentic-config.yaml', 'w') as f:
        f.write(yaml_config)
    
    print("Created .agentic-config.yaml")


def load_and_display_config():
    """Load and display configuration"""
    # Find and load configuration
    config_file = ConfigManager.find_config_file()
    if config_file:
        print(f"Found configuration file: {config_file}")
        config_manager = ConfigManager(config_file)
        config = config_manager.load_config()
        print("Configuration contents:")
        for key, value in config.items():
            # Mask sensitive information
            if 'key' in key or 'token' in key:
                print(f"  {key}: {'*' * len(str(value)) if value else 'None'}")
            else:
                print(f"  {key}: {value}")
    else:
        print("No configuration file found")


if __name__ == "__main__":
    print("Creating example configuration files...")
    create_example_config()
    
    print("\nLoading and displaying configuration...")
    load_and_display_config()
    
    print("\nTo use these configuration files with the automation tools:")
    print("  python generate_docs.py --config .agentic-config.json")
    print("  python create_issues.py --config .agentic-config.yaml")
    print("\nOr simply place the configuration file in the current directory")
    print("and the tools will automatically detect it.")