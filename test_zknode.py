# test_zknode.py
"""
Tests for ZKNode module.
"""

import unittest
from zknode import ZKNode

class TestZKNode(unittest.TestCase):
    """Test cases for ZKNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZKNode()
        self.assertIsInstance(instance, ZKNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZKNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
