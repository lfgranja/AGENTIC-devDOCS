#!/usr/bin/env python3
"""
Configuration module for AGENTIC-devDOCS automation tools.
"""

import os
import json
import yaml
import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


class ConfigManager:
    """Class to handle configuration loading and management"""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the ConfigManager
        
        Args:
            config_path: Path to configuration file (optional)
        """
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        
    def load_config(self) -> Dict[str, Any]:
        """
        Load configuration from file
        
        Returns:
            Configuration dictionary
        """
        if not self.config_path or not os.path.exists(self.config_path):
            logger.info("No configuration file found, using default settings")
            return {}
            
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                if self.config_path.endswith('.json'):
                    self.config = json.load(f)
                elif self.config_path.endswith(('.yml', '.yaml')):
                    self.config = yaml.safe_load(f)
                else:
                    logger.warning(f"Unsupported configuration file format: {self.config_path}")
                    return {}
                    
            logger.info(f"Configuration loaded from {self.config_path}")
            return self.config
        except Exception as e:
            logger.error(f"Error loading configuration from {self.config_path}: {e}")
            return {}
            
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        return self.config.get(key, default)
        
    def get_nested(self, keys: str, default: Any = None) -> Any:
        """
        Get a nested configuration value using dot notation
        
        Args:
            keys: Dot-separated keys (e.g., 'openai.model')
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        value = self.config
        for key in keys.split('.'):
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value
        
    @staticmethod
    def find_config_file(possible_paths: Optional[List[str]] = None) -> Optional[str]:
        """
        Find configuration file in common locations
        
        Args:
            possible_paths: List of possible paths to check
            
        Returns:
            Path to configuration file or None if not found
        """
        if possible_paths is None:
            possible_paths = [
                '.agentic-config.json',
                '.agentic-config.yaml',
                '.agentic-config.yml',
                'agentic-config.json',
                'agentic-config.yaml',
                'agentic-config.yml',
                os.path.expanduser('~/.agentic-config.json'),
                os.path.expanduser('~/.agentic-config.yaml'),
                os.path.expanduser('~/.agentic-config.yml')
            ]
            
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None