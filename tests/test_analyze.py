"""
Unit tests for analyze module
"""

import unittest
from winflux.modules.analyze import AnalyzeModule


class TestAnalyzeModule(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = AnalyzeModule()
    
    def test_analyzer_init(self):
        """Test AnalyzeModule initialization."""
        self.assertIsInstance(self.analyzer, AnalyzeModule)


if __name__ == '__main__':
    unittest.main()
