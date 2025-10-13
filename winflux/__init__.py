"""
WinFlux - Windows System Optimizer
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__license__ = "MIT"

from .cleanup import CleanupModule
from .analyze import AnalyzeModule
from .optimize import OptimizeModule
from .report import ReportModule

__all__ = ['CleanupModule', 'AnalyzeModule', 'OptimizeModule', 'ReportModule']
