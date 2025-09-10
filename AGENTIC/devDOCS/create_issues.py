#!/usr/bin/env python3
"""
Script to automatically create GitHub issues from ISSUES_TO_CREATE documentation
after a PR has been merged.
"""

import os
import sys
import re
import argparse
import logging
from typing import List, Dict, Optional
from dataclasses import dataclass
from github import Github, Issue, Repository

# Import the config module
from .config import ConfigManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class IssueInfo:
    """Data class to store issue information"""
    title: str
    description: str
    labels: List[str]
    milestone: Optional[str] = None
    priority: Optional[str] = None
    complexity: Optional[str] = None
    context: Optional[str] = None

class IssueCreator:
    """Class to handle automated issue creation from documentation"""
    
    def __init__(self, github_token: str, repo_name: str):
        """
        Initialize the IssueCreator
        
        Args:
            github_token: GitHub personal access token
            repo_name: Repository name in format 'owner/repo'
        """
        self.github = Github(github_token)
        self.repo = self.github.get_repo(repo_name)
        self.created_issues = []
        
    def parse_issues_from_file(self, file_path: str) -> List[IssueInfo]:
        """
        Parse issues from the ISSUES_TO_CREATE documentation file
        
        Args:
            file_path: Path to the ISSUES_TO_CREATE{PR_NUMBER}.md file
            
        Returns:
            List of IssueInfo objects
        """
        logger.info(f"Parsing issues from {file_path}")
        
        if not os.path.exists(file_path):
            logger.error(f"File {file_path} does not exist")
            return []
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Split content by issue headers (lines starting with ### Issue)
        issue_sections = re.split(r'###\\s+Issue\\s+\\d+:\\s*', content)
        
        # Remove the first section (header text before first issue)
        issue_sections = issue_sections[1:] if issue_sections else []
        
        issues = []
        for section in issue_sections:
            issue = self._parse_issue_section(section)
            if issue:
                issues.append(issue)
                
        logger.info(f"Found {len(issues)} issues in documentation")
        return issues
        
    def _parse_issue_section(self, section: str) -> Optional[IssueInfo]:
        """
        Parse a single issue section from the documentation
        
        Args:
            section: Text content of a single issue section
            
        Returns:
            IssueInfo object or None if parsing fails
        """
        # Extract title
        title_match = re.search(r'^\\s*[*]{2}Title[*]{2}:\\s*(.+?)\\s*$', section, re.MULTILINE)
        if not title_match:
            logger.warning("Could not find title in issue section")
            return None
            
        title = title_match.group(1).strip()
        
        # Extract description
        desc_match = re.search(r'^\\s*[*]{2}Description[*]{2}:\\s*(.+?)\\s*$',
                              section, re.MULTILINE | re.DOTALL)
        if not desc_match:
            logger.warning(f"Could not find description for issue '{title}'")
            return None
            
        description_lines = desc_match.group(1).strip().split('\n')
        # Remove leading whitespace from each line
        description = '\n'.join(line.strip() for line in description_lines)
        
        # Extract labels
        labels_match = re.search(r'^\\s*[*]{2}Labels[*]{2}:\\s*(.+?)\\s*$',
                               section, re.MULTILINE)
        labels = []
        if labels_match:
            labels_text = labels_match.group(1).strip()
            labels = [label.strip() for label in re.split(r'[,;]', labels_text)]
            
        # Extract milestone
        milestone_match = re.search(r'^\\s*[*]{2}Milestone[*]{2}:\\s*(.+?)\\s*$',
                                  section, re.MULTILINE)
        milestone = milestone_match.group(1).strip() if milestone_match else None
        
        # Extract priority
        priority_match = re.search(r'^\\s*[*]{2}Priority[*]{2}:\\s*(.+?)\\s*$',
                                  section, re.MULTILINE)
        priority = priority_match.group(1).strip() if priority_match else None
        
        # Extract complexity
        complexity_match = re.search(r'^\\s*[*]{2}Complexity[*]{2}:\\s*(.+?)\\s*$',
                                    section, re.MULTILINE)
        complexity = complexity_match.group(1).strip() if complexity_match else None
        
        # Extract context
        context_match = re.search(r'^\\s*[*]{2}Context[*]{2}:\\s*(.+?)\\s*$',
                                 section, re.MULTILINE | re.DOTALL)
        context = context_match.group(1).strip() if context_match else None
        
        return IssueInfo(
            title=title,
            description=description,
            labels=labels,
            milestone=milestone,
            priority=priority,
            complexity=complexity,
            context=context
        )
        
    def validate_labels(self, labels: List[str]) -> List[str]:
        """
        Validate labels against repository's existing labels
        
        Args:
            labels: List of label names to validate
            
        Returns:
            List of valid label names
        """
        try:
            existing_labels = [label.name for label in self.repo.get_labels()]
            valid_labels = [label for label in labels if label in existing_labels]
            
            invalid_labels = set(labels) - set(valid_labels)
            if invalid_labels:
                logger.warning(f"Invalid labels will be skipped: {invalid_labels}")
                
            return valid_labels
        except Exception as e:
            logger.error(f"Error validating labels: {e}")
            return []
            
    def get_milestone_number(self, milestone_title: str) -> Optional[int]:
        """
        Get milestone number by title
        
        Args:
            milestone_title: Title of the milestone
            
        Returns:
            Milestone number or None if not found
        """
        if not milestone_title:
            return None
            
        try:
            milestones = self.repo.get_milestones(state='open')
            for milestone in milestones:
                if milestone.title == milestone_title:
                    return milestone.number
            return None
        except Exception as e:
            logger.error(f"Error getting milestone '{milestone_title}': {e}")
            return None
            
    def create_issue(self, issue_info: IssueInfo, pr_number: int) -> Optional[Issue]:
        """
        Create a GitHub issue from IssueInfo
        
        Args:
            issue_info: Issue information
            pr_number: PR number to reference
            
        Returns:
            Created Issue object or None if creation fails
        """
        # Validate and prepare labels
        labels = self.validate_labels(issue_info.labels)
        
        # Add priority and complexity as labels if specified
        if issue_info.priority:
            priority_label = f"priority:{issue_info.priority.lower()}"
            labels.append(priority_label)
            
        if issue_info.complexity:
            complexity_label = f"complexity:{issue_info.complexity.lower()}"
            labels.append(complexity_label)
            
        # Prepare issue description with additional context
        full_description = issue_info.description
        if issue_info.context:
            full_description += f"\n\n**Context:**\n{issue_info.context}"
            
        full_description += f"\n\n**Related to PR:** #{pr_number}"
        
        # Get milestone number if specified
        milestone_number = self.get_milestone_number(issue_info.milestone)
        
        try:
            # Create the issue
            issue = self.repo.create_issue(
                title=issue_info.title,
                body=full_description,
                labels=labels,
                milestone=self.repo.get_milestone(milestone_number) if milestone_number else None
            )
            
            logger.info(f"Created issue #{issue.number}: {issue.title}")
            self.created_issues.append(issue)
            return issue
        except Exception as e:
            logger.error(f"Error creating issue '{issue_info.title}': {e}")
            return None
            
    def create_issues_from_pr(self, pr_number: int, issues_file_path: str) -> List[Issue]:
        """
        Create issues from ISSUES_TO_CREATE documentation after PR merge
        
        Args:
            pr_number: PR number
            issues_file_path: Path to ISSUES_TO_CREATE{PR_NUMBER}.md file
            
        Returns:
            List of created Issue objects
        """
        logger.info(f"Creating issues from PR #{pr_number} documentation")
        
        # Parse issues from documentation
        issues_info = self.parse_issues_from_file(issues_file_path)
        
        if not issues_info:
            logger.warning("No issues found in documentation")
            return []
            
        # Create issues
        created_issues = []
        for issue_info in issues_info:
            issue = self.create_issue(issue_info, pr_number)
            if issue:
                created_issues.append(issue)
                
        logger.info(f"Successfully created {len(created_issues)} issues")
        return created_issues
        
    def update_documentation(self, issues_file_path: str, created_issues: List[Issue]):
        """
        Update the ISSUES_TO_CREATE documentation with links to created issues
        
        Args:
            issues_file_path: Path to the ISSUES_TO_CREATE{PR_NUMBER}.md file
            created_issues: List of created Issue objects
        """
        if not os.path.exists(issues_file_path):
            logger.warning(f"Documentation file {issues_file_path} does not exist")
            return
            
        try:
            with open(issues_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Add a section at the end with links to created issues
            issue_links = "\n\n## Created Issues\n\n"
            issue_links += "The following issues have been automatically created:\n\n"
            
            for issue in created_issues:
                issue_links += f"- [#{issue.number}: {issue.title}]({issue.html_url})\n"
                
            updated_content = content + issue_links
            
            with open(issues_file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
                
            logger.info(f"Updated documentation with links to {len(created_issues)} issues")
        except Exception as e:
            logger.error(f"Error updating documentation: {e}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Automatically create GitHub issues from documentation')
    parser.add_argument('--token', help='GitHub personal access token')
    parser.add_argument('--repo', help='Repository name (owner/repo)')
    parser.add_argument('--pr', type=int, help='PR number')
    parser.add_argument('--issues-file', help='Path to ISSUES_TO_CREATE{PR_NUMBER}.md file')
    parser.add_argument('--config', help='Path to configuration file')
    
    args = parser.parse_args()
    
    # Load configuration
    config_manager = ConfigManager(args.config or ConfigManager.find_config_file())
    config = config_manager.load_config()
    
    # Use command line arguments if provided, otherwise use config file values
    github_token = args.token or config_manager.get('github_token') or os.environ.get('GITHUB_TOKEN')
    repo_name = args.repo or config_manager.get('repo')
    pr_number = args.pr or config_manager.get('pr')
    issues_file_path = args.issues_file or config_manager.get('issues_file')
    
    # Validate required parameters
    if not github_token:
        parser.error("GitHub token is required")
    if not repo_name:
        parser.error("Repository name is required")
    if not pr_number:
        parser.error("PR number is required")
    if not issues_file_path:
        parser.error("Issues file path is required")
    
    # Create issue creator
    creator = IssueCreator(github_token, repo_name)
    
    # Create issues
    created_issues = creator.create_issues_from_pr(pr_number, issues_file_path)
    
    # Update documentation with links to created issues
    creator.update_documentation(issues_file_path, created_issues)
    
    # Print summary
    print(f"Created {len(created_issues)} issues:")
    for issue in created_issues:
        print(f"  - #{issue.number}: {issue.title} ({issue.html_url})")
        
    return len(created_issues)

if __name__ == '__main__':
    sys.exit(main())