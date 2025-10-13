"""
Utility functions for WinFlux
"""

from pathlib import Path


def get_dir_size(path: Path) -> int:
    """Calculate directory size recursively."""
    total = 0
    try:
        for entry in path.rglob('*'):
            if entry.is_file():
                try:
                    total += entry.stat().st_size
                except:
                    pass
    except:
        pass
    return total


def format_bytes(bytes: int) -> str:
    """Format bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} PB"
