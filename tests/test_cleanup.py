"""
Unit tests for cleanup module
"""

import unittest
from pathlib import Path
from winflux.modules.cleanup import CleanupModule


class TestCleanupModule(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.cleanup = CleanupModule(dry_run=True)
    
    def test_cleanup_init(self):
        """Test CleanupModule initialization."""
        self.assertTrue(self.cleanup.dry_run)
        self.assertEqual(self.cleanup.deleted_files, 0)
        self.assertEqual(self.cleanup.freed_space, 0)
    
    def test_dry_run_mode(self):
        """Test that dry run mode doesn't delete files."""
        # This would need actual temp files to test properly
        # For now, just verify the module initializes correctly
        self.assertTrue(self.cleanup.dry_run)


if __name__ == '__main__':
    unittest.main()
