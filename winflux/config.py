"""
Configuration management for WinFlux
"""

import json
import logging
from pathlib import Path
from datetime import datetime

# Configuration paths
HOME_DIR = Path.home()
CONFIG_DIR = HOME_DIR / ".winflux"
CONFIG_FILE = CONFIG_DIR / "config.json"
LOG_DIR = CONFIG_DIR / "logs"
LOG_FILE = LOG_DIR / f"winflux_{datetime.now().strftime('%Y%m%d')}.log"

# Default configuration
DEFAULT_CONFIG = {
    "auto_confirm": False,
    "show_banner": True,
    "log_level": "INFO",
    "backup_enabled": True
}


def setup_logging():
    """Setup logging configuration."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )


def load_config():
    """Load configuration from file."""
    if not CONFIG_FILE.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG
    
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)


def save_config(config):
    """Save configuration to file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
