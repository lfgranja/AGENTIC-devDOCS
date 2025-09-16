#!/usr/bin/env python3
"""
Unit tests for the create_issues.py script.
"""

import os
import sys
import tempfile
from unittest.mock import Mock, patch

# Add the devDOCS directory to the path so we can import the script
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'AGENTIC', 'devDOCS'))

from create_issues import IssueInfo, IssueCreator


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
        creator = IssueCreator("test_token", "test_owner/test_repo")
        
        assert creator.github == mock_github.return_value
        assert creator.repo == mock_repo
        assert creator.created_issues == []
        mock_github.assert_called_once_with("test_token")
        mock_github.return_value.get_repo.assert_called_once_with("test_owner/test_repo")
    
    @patch('create_issues.Github')
    def test_parse_issues_from_file_nonexistent(self, mock_github):
        """Test parsing issues from nonexistent file"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        creator = IssueCreator("test_token", "test_owner/test_repo")
        issues = creator.parse_issues_from_file("/nonexistent/file.md")
        assert issues == []
    
    @patch('create_issues.Github')
    def test_parse_issues_from_file_valid_content(self, mock_github):
        """Test parsing issues from file with valid content"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Create a temporary file with valid issue content
        # Note: Using the exact format expected by the regex patterns
        valid_content = """# Issues to Create

### Issue 1: Test Issue

**Title**: Test Issue Title
**Description**: Test Issue Description
**Labels**: enhancement, documentation
**Milestone**: v1.0
**Priority**: medium
**Complexity**: low
**Context**: Test context for the issue

---
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(valid_content)
            temp_file_path = f.name
        
        try:
            creator = IssueCreator("test_token", "test_owner/test_repo")
            issues = creator.parse_issues_from_file(temp_file_path)
            
            assert len(issues) == 1
            assert issues[0].title == "Test Issue Title"
            assert issues[0].description == "Test Issue Description"
            assert issues[0].labels == ["enhancement", "documentation"]
            assert issues[0].milestone == "v1.0"
            assert issues[0].priority == "medium"
            assert issues[0].complexity == "low"
            assert issues[0].context == "Test context for the issue"
        finally:
            os.unlink(temp_file_path)
    
    @patch('create_issues.Github')
    def test_parse_issues_from_file_malformed_content(self, mock_github):
        """Test parsing issues from file with malformed content"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Create a temporary file with malformed issue content (missing title)
        malformed_content = """# Issues to Create

### Issue 1: Test Issue

**Description**: Test Issue Description
**Labels**: enhancement, documentation

---
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(malformed_content)
            temp_file_path = f.name
        
        try:
            creator = IssueCreator("test_token", "test_owner/test_repo")
            issues = creator.parse_issues_from_file(temp_file_path)
            
            # Should return empty list because title is required
            assert issues == []
        finally:
            os.unlink(temp_file_path)
    
    @patch('create_issues.Github')
    def test_validate_labels_success(self, mock_github):
        """Test label validation with valid labels"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Mock existing labels in the repository
        mock_label1 = Mock()
        mock_label1.name = "bug"
        mock_label2 = Mock()
        mock_label2.name = "enhancement"
        mock_repo.get_labels.return_value = [mock_label1, mock_label2]
        
        creator = IssueCreator("test_token", "test_owner/test_repo")
        valid_labels = creator.validate_labels(["bug", "enhancement", "nonexistent"])
        
        # Should return only valid labels
        assert set(valid_labels) == {"bug", "enhancement"}
    
    @patch('create_issues.Github')
    def test_validate_labels_error_handling(self, mock_github):
        """Test label validation error handling"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Mock get_labels to raise an exception
        mock_repo.get_labels.side_effect = Exception("API Error")
        
        creator = IssueCreator("test_token", "test_owner/test_repo")
        valid_labels = creator.validate_labels(["bug", "enhancement"])
        
        # Should return empty list on error
        assert valid_labels == []
    
    @patch('create_issues.Github')
    def test_get_milestone_number_success(self, mock_github):
        """Test getting milestone number successfully"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Mock milestones
        mock_milestone1 = Mock()
        mock_milestone1.title = "v1.0"
        mock_milestone1.number = 1
        mock_milestone2 = Mock()
        mock_milestone2.title = "v2.0"
        mock_milestone2.number = 2
        
        mock_repo.get_milestones.return_value = [mock_milestone1, mock_milestone2]
        
        creator = IssueCreator("test_token", "test_owner/test_repo")
        milestone_number = creator.get_milestone_number("v1.0")
        
        assert milestone_number == 1
    
    @patch('create_issues.Github')
    def test_get_milestone_number_not_found(self, mock_github):
        """Test getting milestone number when not found"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Mock milestones
        mock_milestone1 = Mock()
        mock_milestone1.title = "v1.0"
        mock_milestone1.number = 1
        
        mock_repo.get_milestones.return_value = [mock_milestone1]
        
        creator = IssueCreator("test_token", "test_owner/test_repo")
        milestone_number = creator.get_milestone_number("v2.0")
        
        assert milestone_number is None
    
    @patch('create_issues.Github')
    def test_get_milestone_number_error_handling(self, mock_github):
        """Test getting milestone number error handling"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Mock get_milestones to raise an exception
        mock_repo.get_milestones.side_effect = Exception("API Error")
        
        creator = IssueCreator("test_token", "test_owner/test_repo")
        milestone_number = creator.get_milestone_number("v1.0")
        
        assert milestone_number is None
    
    @patch('create_issues.Github')
    def test_create_issue_success(self, mock_github):
        """Test creating an issue successfully"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Mock created issue
        mock_created_issue = Mock()
        mock_created_issue.number = 42
        mock_created_issue.title = "Test Issue"
        mock_repo.create_issue.return_value = mock_created_issue
        
        # Mock existing labels
        mock_label = Mock()
        mock_label.name = "bug"
        mock_repo.get_labels.return_value = [mock_label]
        
        creator = IssueCreator("test_token", "test_owner/test_repo")
        issue_info = IssueInfo(
            title="Test Issue",
            description="Test Description",
            labels=["bug"]
        )
        
        created_issue = creator.create_issue(issue_info, 10)
        
        assert created_issue == mock_created_issue
        assert len(creator.created_issues) == 1
        assert creator.created_issues[0] == mock_created_issue
    
    @patch('create_issues.Github')
    def test_create_issue_error_handling(self, mock_github):
        """Test creating an issue with error handling"""
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        
        # Mock create_issue to raise an exception
        mock_repo.create_issue.side_effect = Exception("API Error")
        
        creator = IssueCreator("test_token", "test_owner/test_repo")
        issue_info = IssueInfo(
            title="Test Issue",
            description="Test Description",
            labels=[]
        )
        
        created_issue = creator.create_issue(issue_info, 10)
        
        assert created_issue is None
        assert len(creator.created_issues) == 0