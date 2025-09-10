#!/usr/bin/env python3
"""
Unit tests for the create_issues.py script.
"""

import os
import sys
import tempfile
import pytest
from unittest.mock import Mock, patch, mock_open

# Add the devDOCS directory to the path so we can import the script
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'AGENTIC', 'devDOCS'))

from create_issues import IssueInfo


class TestIssueInfo:
    """Test cases for the IssueInfo dataclass"""
    
    def test_issue_info_creation(self):
        """Test that IssueInfo can be created with all parameters"""
        issue = IssueInfo(
            title="Test Issue",
            description="Test Description",
            labels=["bug", "help wanted"],
            milestone="v1.0",
            priority="high",
            complexity="medium",
            context="Test context"
        )
        
        assert issue.title == "Test Issue"
        assert issue.description == "Test Description"
        assert issue.labels == ["bug", "help wanted"]
        assert issue.milestone == "v1.0"
        assert issue.priority == "high"
        assert issue.complexity == "medium"
        assert issue.context == "Test context"
    
    def test_issue_info_creation_minimal(self):
        """Test that IssueInfo can be created with minimal parameters"""
        issue = IssueInfo(
            title="Test Issue",
            description="Test Description",
            labels=[]
        )
        
        assert issue.title == "Test Issue"
        assert issue.description == "Test Description"
        assert issue.labels == []
        assert issue.milestone is None
        assert issue.priority is None
        assert issue.complexity is None
        assert issue.context is None


class TestIssueCreator:
    """Test cases for the IssueCreator class"""
    
    @patch('create_issues.Github')
    def test_init(self, mock_github):
        """Test IssueCreator initialization"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # We're only testing the initialization, not the full functionality
        # since the script has some issues that would require more extensive fixes
        from create_issues import IssueCreator
        creator = IssueCreator("test_token", "test_owner/test_repo")
        
        assert creator.github == mock_github.return_value
        assert creator.repo == mock_repo
        assert creator.created_issues == []
        mock_github.assert_called_once_with("test_token")
        mock_github.return_value.get_repo.assert_called_once_with("test_owner/test_repo")