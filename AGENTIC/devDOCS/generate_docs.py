#!/usr/bin/env python3
"""
Script to automatically generate development documentation based on code changes.
"""

import os
import sys
import argparse
import logging
from typing import List, Dict
from pathlib import Path
import git
import openai

# Import the config module
from .config import ConfigManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DocumentationGenerator:
    """Class to handle automated documentation generation"""
    
    def __init__(self, openai_api_key: str):
        """
        Initialize the DocumentationGenerator
        
        Args:
            openai_api_key: OpenAI API key for generating documentation content
        """
        self.openai_client = openai.OpenAI(api_key=openai_api_key)
        
    def get_changed_files(self, changed_files_path: str) -> List[str]:
        """
        Get list of changed files from a file
        
        Args:
            changed_files_path: Path to file containing list of changed files
            
        Returns:
            List of changed file paths
        """
        if not os.path.exists(changed_files_path):
            logger.warning(f"Changed files list {changed_files_path} does not exist")
            return []
            
        with open(changed_files_path, 'r') as f:
            changed_files = [line.strip() for line in f.readlines() if line.strip()]
            
        return changed_files
        
    def analyze_changes(self, changed_files: List[str]) -> Dict[str, any]:
        """
        Analyze code changes to identify key information for documentation
        
        Args:
            changed_files: List of changed file paths
            
        Returns:
            Dictionary with analysis results
        """
        analysis = {
            'features': [],
            'fixes': [],
            'refactorings': [],
            'tests': [],
            'documentation': [],
            'dependencies': []
        }
        
        for file_path in changed_files:
            # Categorize files by type
            if file_path.endswith(('.py', '.js', '.ts', '.java', '.cpp', '.rs', '.go')):
                # Source code files
                if 'test' in file_path.lower() or file_path.endswith(('.test.py', '.spec.js', '_test.go')):
                    analysis['tests'].append(file_path)
                else:
                    # Analyze the file content to categorize changes
                    category = self._categorize_source_file(file_path)
                    analysis[category].append(file_path)
            elif file_path.endswith(('.md', '.rst', '.txt')):
                # Documentation files
                analysis['documentation'].append(file_path)
            elif file_path.endswith(('requirements.txt', 'package.json', 'Cargo.toml', 'go.mod')):
                # Dependency files
                analysis['dependencies'].append(file_path)
                
        return analysis
        
    def _categorize_source_file(self, file_path: str) -> str:
        """
        Categorize a source file based on its content
        
        Args:
            file_path: Path to the source file
            
        Returns:
            Category: 'features', 'fixes', 'refactorings', or 'other'
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Simple heuristics based on keywords
            if any(keyword in content.lower() for keyword in ['new feature', 'implement', 'add']):
                return 'features'
            elif any(keyword in content.lower() for keyword in ['fix', 'bug', 'error', 'exception']):
                return 'fixes'
            elif any(keyword in content.lower() for keyword in ['refactor', 'restructure', 'simplify']):
                return 'refactorings'
            else:
                return 'other'
        except Exception as e:
            logger.warning(f"Could not analyze file {file_path}: {e}")
            return 'other'
            
    def generate_lessons_learned(self, analysis: Dict[str, any], branch_name: str, pr_number: str) -> str:
        """
        Generate LESSONS_LEARNED documentation
        
        Args:
            analysis: Analysis results from analyze_changes
            branch_name: Name of the branch
            pr_number: PR number (if applicable)
            
        Returns:
            Generated documentation content
        """
        prompt = f"""
        Generate a "Lessons Learned" documentation for a software development project based on the following analysis:
        
        Branch: {branch_name}
        PR Number: {pr_number if pr_number else 'N/A'}
        
        Analysis:
        - New Features: {', '.join(analysis['features']) if analysis['features'] else 'None'}
        - Bug Fixes: {', '.join(analysis['fixes']) if analysis['fixes'] else 'None'}
        - Refactorings: {', '.join(analysis['refactorings']) if analysis['refactorings'] else 'None'}
        - Tests: {', '.join(analysis['tests']) if analysis['tests'] else 'None'}
        - Documentation: {', '.join(analysis['documentation']) if analysis['documentation'] else 'None'}
        - Dependencies: {', '.join(analysis['dependencies']) if analysis['dependencies'] else 'None'}
        
        Please create a comprehensive "Lessons Learned" document with the following sections:
        1. Technical Challenges and Solutions
        2. Design Decisions
        3. Unexpected Issues
        4. Performance Considerations
        5. Testing Strategies
        6. Deviations from Original Plan
        
        Each section should have 1-3 bullet points with specific details. Use markdown formatting.
        """
        
        response = self._call_openai(prompt)
        return response
        
    def generate_future_work(self, analysis: Dict[str, any], branch_name: str, pr_number: str) -> str:
        """
        Generate FUTURE_WORK_TODO documentation
        
        Args:
            analysis: Analysis results from analyze_changes
            branch_name: Name of the branch
            pr_number: PR number (if applicable)
            
        Returns:
            Generated documentation content
        """
        prompt = f"""
        Generate a "Future Work" documentation for a software development project based on the following analysis:
        
        Branch: {branch_name}
        PR Number: {pr_number if pr_number else 'N/A'}
        
        Analysis:
        - New Features: {', '.join(analysis['features']) if analysis['features'] else 'None'}
        - Bug Fixes: {', '.join(analysis['fixes']) if analysis['fixes'] else 'None'}
        - Refactorings: {', '.join(analysis['refactorings']) if analysis['refactorings'] else 'None'}
        - Tests: {', '.join(analysis['tests']) if analysis['tests'] else 'None'}
        - Documentation: {', '.join(analysis['documentation']) if analysis['documentation'] else 'None'}
        - Dependencies: {', '.join(analysis['dependencies']) if analysis['dependencies'] else 'None'}
        
        Please create a comprehensive "Future Work" document with the following sections:
        1. Areas for Improvement
        2. Potential Optimizations
        3. Related Features
        4. Technical Debt
        5. Ideas for Extension
        
        Each section should have 2-5 bullet points with specific details. Use markdown formatting.
        """
        
        response = self._call_openai(prompt)
        return response
        
    def generate_issues_to_create(self, analysis: Dict[str, any], branch_name: str, pr_number: str) -> str:
        """
        Generate ISSUES_TO_CREATE documentation
        
        Args:
            analysis: Analysis results from analyze_changes
            branch_name: Name of the branch
            pr_number: PR number (if applicable)
            
        Returns:
            Generated documentation content
        """
        prompt = f"""
        Generate an "Issues to Create" documentation for a software development project based on the following analysis:
        
        Branch: {branch_name}
        PR Number: {pr_number if pr_number else 'N/A'}
        
        Analysis:
        - New Features: {', '.join(analysis['features']) if analysis['features'] else 'None'}
        - Bug Fixes: {', '.join(analysis['fixes']) if analysis['fixes'] else 'None'}
        - Refactorings: {', '.join(analysis['refactorings']) if analysis['refactorings'] else 'None'}
        - Tests: {', '.join(analysis['tests']) if analysis['tests'] else 'None'}
        - Documentation: {', '.join(analysis['documentation']) if analysis['documentation'] else 'None'}
        - Dependencies: {', '.join(analysis['dependencies']) if analysis['dependencies'] else 'None'}
        
        Please create a comprehensive "Issues to Create" document with 3-5 issues that should be created based on this work.
        For each issue, include:
        - Title
        - Description
        - Labels (use standard GitHub labels like enhancement, bug, documentation, etc.)
        - Milestone (if applicable)
        - Priority (high, medium, low)
        - Complexity (low, medium, high)
        - Context
        
        Format each issue with markdown headers and bullet points. Use the following format:
        
        ### Issue 1: [Title]
        
        **Title:** [Title]
        **Description:** [Detailed description]
        **Labels:** [comma-separated labels]
        **Milestone:** [milestone name or N/A]
        **Priority:** [high/medium/low]
        **Complexity:** [low/medium/high]
        **Context:** [background information]
        
        ---
        """
        
        response = self._call_openai(prompt)
        return response
        
    def _call_openai(self, prompt: str) -> str:
        """
        Call OpenAI API to generate content
        
        Args:
            prompt: Prompt to send to OpenAI
            
        Returns:
            Generated content
        """
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a technical documentation writer for software development projects."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Error calling OpenAI API: {e}")
            return f"Error generating content: {e}"
            
    def generate_all_documentation(self, changed_files_path: str, output_dir: str, branch_name: str, pr_number: str = None):
        """
        Generate all documentation files
        
        Args:
            changed_files_path: Path to file containing list of changed files
            output_dir: Directory to save documentation files
            branch_name: Name of the branch
            pr_number: PR number (if applicable)
        """
        # Create output directory
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Get changed files
        changed_files = self.get_changed_files(changed_files_path)
        logger.info(f"Found {len(changed_files)} changed files")
        
        # Analyze changes
        analysis = self.analyze_changes(changed_files)
        logger.info("Analyzed changes")
        
        # Generate documentation files
        pr_suffix = pr_number if pr_number else branch_name
        
        # Generate LESSONS_LEARNED
        lessons_learned_content = self.generate_lessons_learned(analysis, branch_name, pr_number)
        lessons_learned_path = os.path.join(output_dir, f"LESSONS_LEARNED{pr_suffix}.md")
        with open(lessons_learned_path, 'w', encoding='utf-8') as f:
            f.write(lessons_learned_content)
        logger.info(f"Generated {lessons_learned_path}")
        
        # Generate FUTURE_WORK_TODO
        future_work_content = self.generate_future_work(analysis, branch_name, pr_number)
        future_work_path = os.path.join(output_dir, f"FUTURE_WORK_TODO{pr_suffix}.md")
        with open(future_work_path, 'w', encoding='utf-8') as f:
            f.write(future_work_content)
        logger.info(f"Generated {future_work_path}")
        
        # Generate ISSUES_TO_CREATE
        issues_to_create_content = self.generate_issues_to_create(analysis, branch_name, pr_number)
        issues_to_create_path = os.path.join(output_dir, f"ISSUES_TO_CREATE{pr_suffix}.md")
        with open(issues_to_create_path, 'w', encoding='utf-8') as f:
            f.write(issues_to_create_content)
        logger.info(f"Generated {issues_to_create_path}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Automatically generate development documentation')
    parser.add_argument('--changed-files', help='Path to file containing list of changed files')
    parser.add_argument('--output-dir', help='Directory to save documentation files')
    parser.add_argument('--branch', help='Branch name')
    parser.add_argument('--pr-number', help='PR number (if applicable)')
    parser.add_argument('--openai-api-key', help='OpenAI API key')
    parser.add_argument('--config', help='Path to configuration file')
    
    args = parser.parse_args()
    
    # Load configuration
    config_manager = ConfigManager(args.config or ConfigManager.find_config_file())
    config = config_manager.load_config()
    
    # Use command line arguments if provided, otherwise use config file values
    changed_files_path = args.changed_files or config_manager.get('changed_files')
    output_dir = args.output_dir or config_manager.get('output_dir')
    branch_name = args.branch or config_manager.get('branch')
    pr_number = args.pr_number or config_manager.get('pr_number')
    openai_api_key = args.openai_api_key or config_manager.get('openai_api_key') or os.environ.get('OPENAI_API_KEY')
    
    # Validate required parameters
    if not changed_files_path:
        parser.error("changed-files path is required")
    if not output_dir:
        parser.error("output-dir is required")
    if not branch_name:
        parser.error("branch name is required")
    if not openai_api_key:
        parser.error("OpenAI API key is required")
    
    # Create documentation generator
    generator = DocumentationGenerator(openai_api_key)
    
    # Generate documentation
    generator.generate_all_documentation(
        changed_files_path,
        output_dir,
        branch_name,
        pr_number
    )
    
    print(f"Documentation generated in {args.output_dir}")
    return 0

if __name__ == '__main__':
    sys.exit(main())