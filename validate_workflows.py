#!/usr/bin/env python3
"""
Script to validate GitHub Actions workflow files.
"""

import os
import yaml
import sys
from pathlib import Path


def validate_workflow(file_path):
    """
    Validate a GitHub Actions workflow file.
    
    Args:
        file_path (str): Path to the workflow file
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            workflow = yaml.safe_load(f)
        
        # Check required fields
        if 'name' not in workflow:
            print(f"Error: Missing 'name' field in {file_path}")
            return False
            
        if 'on' not in workflow:
            print(f"Error: Missing 'on' field in {file_path}")
            return False
            
        if 'jobs' not in workflow:
            print(f"Error: Missing 'jobs' field in {file_path}")
            return False
            
        print(f"✓ {file_path} is valid")
        return True
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"Error: Failed to validate {file_path}: {e}")
        return False


def main():
    """Main function to validate all workflow files."""
    workflows_dir = Path('.github/workflows')
    
    if not workflows_dir.exists():
        print("Error: .github/workflows directory not found")
        return 1
        
    workflow_files = list(workflows_dir.glob('*.yml')) + list(workflows_dir.glob('*.yaml'))
    
    if not workflow_files:
        print("No workflow files found")
        return 0
        
    all_valid = True
    for workflow_file in workflow_files:
        if not validate_workflow(workflow_file):
            all_valid = False
            
    return 0 if all_valid else 1


if __name__ == '__main__':
    sys.exit(main())