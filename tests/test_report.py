"""
Unit tests for report module
"""

import unittest
from winflux.modules.report import ReportModule


class TestReportModule(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.reporter = ReportModule()
    
    def test_reporter_init(self):
        """Test ReportModule initialization."""
        self.assertIsInstance(self.reporter, ReportModule)


if __name__ == '__main__':
    unittest.main()
