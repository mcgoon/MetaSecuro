# test_metasecuro.py
"""
Tests for MetaSecuro module.
"""

import unittest
from metasecuro import MetaSecuro

class TestMetaSecuro(unittest.TestCase):
    """Test cases for MetaSecuro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaSecuro()
        self.assertIsInstance(instance, MetaSecuro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaSecuro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
