#!/usr/bin/env python3
"""
Tests for the configuration module.
"""

import os
import json
import tempfile
import pytest
from unittest.mock import patch

# Add the devDOCS directory to the path so we can import the module
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'AGENTIC', 'devDOCS'))

from config import ConfigManager


class TestConfigManager:
    """Test cases for the ConfigManager class"""
    
    def test_init_without_config_path(self):
        """Test ConfigManager initialization without config path"""
        config_manager = ConfigManager()
        assert config_manager.config_path is None
        assert config_manager.config == {}
    
    def test_init_with_config_path(self):
        """Test ConfigManager initialization with config path"""
        config_manager = ConfigManager("/path/to/config.json")
        assert config_manager.config_path == "/path/to/config.json"
        assert config_manager.config == {}
    
    def test_load_config_nonexistent_file(self):
        """Test loading configuration from nonexistent file"""
        config_manager = ConfigManager("/nonexistent/config.json")
        config = config_manager.load_config()
        assert config == {}
    
    def test_load_config_json_file(self):
        """Test loading configuration from JSON file"""
        # Create a temporary JSON file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({"test_key": "test_value"}, f)
            temp_file_path = f.name
        
        try:
            config_manager = ConfigManager(temp_file_path)
            config = config_manager.load_config()
            assert config["test_key"] == "test_value"
        finally:
            os.unlink(temp_file_path)
    
    def test_get_value(self):
        """Test getting a configuration value"""
        config_manager = ConfigManager()
        config_manager.config = {"test_key": "test_value"}
        assert config_manager.get("test_key") == "test_value"
        assert config_manager.get("nonexistent_key", "default") == "default"
    
    def test_get_nested_value(self):
        """Test getting a nested configuration value"""
        config_manager = ConfigManager()
        config_manager.config = {
            "openai": {
                "model": "gpt-3.5-turbo",
                "temperature": 0.7
            }
        }
        assert config_manager.get_nested("openai.model") == "gpt-3.5-turbo"
        assert config_manager.get_nested("openai.temperature") == 0.7
        assert config_manager.get_nested("nonexistent.key", "default") == "default"
    
    @patch('os.path.exists')
    def test_find_config_file(self, mock_exists):
        """Test finding configuration file"""
        # Mock os.path.exists to return True for the first path and False for others
        mock_exists.side_effect = lambda path: path == '.agentic-config.json'
        
        config_file = ConfigManager.find_config_file()
        assert config_file == '.agentic-config.json'