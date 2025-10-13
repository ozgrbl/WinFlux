# Project Structure

WinFlux follows a modular architecture for easy maintenance and extensibility.

## Directory Structure

```
WinFlux/
│
├── winflux.py                 # Single-file version (standalone)
│
├── winflux/                   # Package version (modular)
│   ├── __init__.py           # Package initialization
│   ├── cli.py                # CLI interface with Click
│   ├── config.py             # Configuration management
│   └── modules/              # Core functionality modules
│       ├── __init__.py       # Module initialization
│       ├── cleanup.py        # Cleanup operations
│       ├── analyze.py        # Disk analysis
│       ├── optimize.py       # System optimization
│       ├── report.py         # Health reporting
│       └── utils.py          # Utility functions
│
├── tests/                     # Unit tests
│   ├── test_cleanup.py
│   ├── test_analyze.py
│   └── test_report.py
│
├── requirements.txt           # Python dependencies
├── setup.py                   # Package installation script
├── LICENSE                    # MIT License
├── README.md                  # Main documentation
├── INSTALL.md                 # Installation guide
├── EXAMPLES.md                # Usage examples
├── CONTRIBUTING.md            # Contribution guidelines
└── .gitignore                 # Git ignore file
```

## Module Descriptions

### winflux.py (Standalone)
Complete single-file implementation with all features. Perfect for quick use without installation.

**Usage:**
```bash
python winflux.py clean
```

### winflux/ (Package)
Modular implementation organized into logical components.

#### cli.py
- Command-line interface using Click
- Command registration and routing
- Input validation and user interaction

#### config.py
- Configuration file management
- Logging setup
- Default settings

#### modules/cleanup.py
**Functions:**
- `clean_temp_files()` - Remove temporary files
- `clean_browser_cache()` - Clear browser caches
- `clean_recycle_bin()` - Empty recycle bin
- `clean_junk_files()` - Remove logs and dumps

#### modules/analyze.py
**Functions:**
- `analyze_disk_usage()` - Analyze disk space usage
- Display top N largest files/folders
- Calculate directory sizes

#### modules/optimize.py
**Functions:**
- `list_startup_programs()` - Show startup applications
- Registry access for startup entries
- System optimization recommendations

#### modules/report.py
**Functions:**
- `generate_report()` - Create system health report
- CPU, RAM, disk metrics
- System uptime and boot time
- Health warnings

#### modules/utils.py
**Utility Functions:**
- `get_dir_size()` - Calculate directory size
- `format_bytes()` - Human-readable byte formatting
- `is_admin()` - Check admin privileges

## Data Flow

```
User Command
     ↓
  cli.py (Click)
     ↓
Module Selection
     ↓
Operation Execution
     ↓
Rich Output
     ↓
Logging
```

## Configuration Structure

**Location:** `~/.winflux/config.json`

```json
{
    "auto_confirm": false,
    "show_banner": true,
    "log_level": "INFO",
    "backup_enabled": true
}
```

## Logging Structure

**Location:** `~/.winflux/logs/winflux_YYYYMMDD.log`

**Format:**
```
2025-10-14 10:30:45 - INFO - Cleanup completed. Freed: 3.04 GB
2025-10-14 10:35:12 - INFO - System report generated
2025-10-14 10:40:22 - WARNING - Could not delete C:\Windows\Temp\file.tmp
```

## Extension Points

### Adding New Commands

1. Create module in `winflux/modules/`
2. Register command in `winflux/cli.py`
3. Add tests in `tests/`
4. Update documentation

### Adding New Cleanup Targets

Edit `winflux/modules/cleanup.py`:

```python
def clean_new_target(self):
    """Clean new target files."""
    console.print("\n[cyan]🧹 Cleaning new target...[/cyan]")
    # Implementation here
```

### Adding New Report Sections

Edit `winflux/modules/report.py`:

```python
def generate_report(self):
    """Generate report with new section."""
    # ... existing sections ...
    
    # New section
    new_table = Table(title="New Metric")
    # Add rows
    console.print(new_table)
```

## Dependencies Explained

- **click** - CLI framework for command handling
- **rich** - Beautiful terminal output with colors and tables
- **psutil** - System and process information
- **colorama** - Cross-platform colored terminal text
- **winshell** - Windows shell operations (recycle bin)
- **pywin32** - Windows API access (registry, etc.)

## Performance Considerations

### Disk Scanning
- Large directories can take time
- Progress indicators keep user informed
- Recursive scanning is optimized

### Memory Usage
- File lists are processed in batches
- Large files aren't loaded into memory
- Efficient directory traversal

### Safety Features
- Dry-run mode for testing
- Confirmation prompts
- Comprehensive logging
- Error handling for locked files

## Future Enhancements

Planned features:
- [ ] Duplicate file finder
- [ ] Registry cleaner
- [ ] Network optimization
- [ ] Scheduled task integration
- [ ] GUI version
- [ ] Plugin system
- [ ] Cloud storage cleanup
- [ ] Performance benchmarking

## Architecture Principles

1. **Modularity** - Each feature in separate module
2. **Testability** - Unit tests for all modules
3. **Extensibility** - Easy to add new features
4. **Safety** - Multiple safeguards against data loss
5. **User-Friendly** - Clear output and confirmations
6. **Cross-Windows** - Works on Windows 10/11

---

**Note:** This structure is designed to be simple yet professional, suitable for both personal use and potential commercial applications.
