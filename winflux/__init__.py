"""
WinFlux - Windows System Optimizer
"""

__version__ = "1.0.0"
__author__ = "Chethan Yadav"
__license__ = "MIT"

from .modules.cleanup import CleanupModule
from .modules.analyze import AnalyzeModule
from .modules.optimize import OptimizeModule
from .modules.report import ReportModule

__all__ = ['CleanupModule', 'AnalyzeModule', 'OptimizeModule', 'ReportModule']
