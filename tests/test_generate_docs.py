#!/usr/bin/env python3
"""
Unit tests for the generate_docs.py script.
"""

import os
import sys
import tempfile
import pytest
from unittest.mock import Mock, patch, mock_open

# Add the devDOCS directory to the path so we can import the script
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'AGENTIC', 'devDOCS'))

from generate_docs import DocumentationGenerator


class TestDocumentationGenerator:
    """Test cases for the DocumentationGenerator class"""
    
    @patch('generate_docs.openai.OpenAI')
    def test_init(self, mock_openai):
        """Test DocumentationGenerator initialization"""
        generator = DocumentationGenerator("test_api_key")
        
        assert generator.openai_client == mock_openai.return_value
        mock_openai.assert_called_once_with(api_key="test_api_key")
    
    def test_get_changed_files_existing(self):
        """Test getting changed files from an existing file"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("file1.py\nfile2.py\nfile3.py\n")
            temp_file_path = f.name
        
        try:
            generator = DocumentationGenerator("test_api_key")
            changed_files = generator.get_changed_files(temp_file_path)
            
            assert len(changed_files) == 3
            assert "file1.py" in changed_files
            assert "file2.py" in changed_files
            assert "file3.py" in changed_files
        finally:
            os.unlink(temp_file_path)
    
    def test_get_changed_files_nonexistent(self):
        """Test getting changed files from a nonexistent file"""
        generator = DocumentationGenerator("test_api_key")
        changed_files = generator.get_changed_files("/nonexistent/file.txt")
        
        assert changed_files == []
    
    def test_get_changed_files_read_error(self):
        """Test getting changed files with read error"""
        generator = DocumentationGenerator("test_api_key")
        
        # Mock open to raise an exception
        with patch("builtins.open", side_effect=Exception("Read error")):
            changed_files = generator.get_changed_files("/some/file.txt")
            # Should return empty list on error
            assert changed_files == []
    
    def test_categorize_source_file_features(self):
        """Test categorizing a source file with feature-related content"""
        generator = DocumentationGenerator("test_api_key")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("# New feature implementation\nprint('Hello World')")
            temp_file_path = f.name
        
        try:
            category = generator._categorize_source_file(temp_file_path)
            assert category == "features"
        finally:
            os.unlink(temp_file_path)
    
    def test_categorize_source_file_fixes(self):
        """Test categorizing a source file with fix-related content"""
        generator = DocumentationGenerator("test_api_key")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("# Bug fix for issue #123\nprint('Hello World')")
            temp_file_path = f.name
        
        try:
            category = generator._categorize_source_file(temp_file_path)
            assert category == "fixes"
        finally:
            os.unlink(temp_file_path)
    
    def test_categorize_source_file_refactorings(self):
        """Test categorizing a source file with refactoring-related content"""
        generator = DocumentationGenerator("test_api_key")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("# Refactor function for better performance\nprint('Hello World')")
            temp_file_path = f.name
        
        try:
            category = generator._categorize_source_file(temp_file_path)
            assert category == "refactorings"
        finally:
            os.unlink(temp_file_path)
    
    def test_categorize_source_file_other(self):
        """Test categorizing a source file with other content"""
        generator = DocumentationGenerator("test_api_key")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("# Simple print statement\nprint('Hello World')")
            temp_file_path = f.name
        
        try:
            category = generator._categorize_source_file(temp_file_path)
            assert category == "other"
        finally:
            os.unlink(temp_file_path)
    
    def test_categorize_source_file_read_error(self):
        """Test categorizing a source file with read error"""
        generator = DocumentationGenerator("test_api_key")
        
        # Mock open to raise an exception
        with patch("builtins.open", side_effect=Exception("Read error")):
            category = generator._categorize_source_file("/nonexistent/file.py")
            # Should return 'other' on error
            assert category == "other"
    
    def test_analyze_changes(self):
        """Test analyzing changes in files"""
        generator = DocumentationGenerator("test_api_key")
        
        # Create temporary files for testing
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f1, \
             tempfile.NamedTemporaryFile(mode='w', suffix='.test.py', delete=False) as f2, \
             tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f3, \
             tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f4:
            
            f1.write("# New feature implementation")
            f2.write("# Test for new feature")
            f3.write("# Documentation for new feature")
            f4.write("# Just a text file")
            
            temp_files = [f1.name, f2.name, f3.name, f4.name]
        
        try:
            changed_files = temp_files
            analysis = generator.analyze_changes(changed_files)
            
            # Check that files are categorized correctly
            assert "features" in analysis
            assert "tests" in analysis
            assert "documentation" in analysis
            assert "dependencies" in analysis
            
            # Check specific categorizations
            assert any(f1.name in category for category in analysis.values())
            assert any(f2.name in category for category in analysis.values())
            assert any(f3.name in category for category in analysis.values())
            assert any(f4.name in category for category in analysis.values())
        finally:
            for temp_file in temp_files:
                os.unlink(temp_file)
    
    @patch('generate_docs.openai.OpenAI')
    def test_call_openai_success(self, mock_openai):
        """Test calling OpenAI API successfully"""
        mock_choice = Mock()
        mock_choice.message.content = "Generated content"
        mock_response = Mock()
        mock_response.choices = [mock_choice]
        mock_openai.return_value.chat.completions.create.return_value = mock_response
        
        generator = DocumentationGenerator("test_api_key")
        result = generator._call_openai("Test prompt")
        
        assert result == "Generated content"
        mock_openai.return_value.chat.completions.create.assert_called_once()
    
    @patch('generate_docs.openai.OpenAI')
    def test_call_openai_error(self, mock_openai):
        """Test calling OpenAI API with error handling"""
        mock_openai.return_value.chat.completions.create.side_effect = Exception("API Error")
        
        generator = DocumentationGenerator("test_api_key")
        result = generator._call_openai("Test prompt")
        
        # Should return error message on API error
        assert "Error generating content" in result