# WinFlux Installation & Setup Guide

## Prerequisites

- **Python 3.10 or higher**
- **Windows 10/11** (Required)
- **pip** (Python package installer)
- **Administrator privileges** (for some operations)

## Installation Methods

### Method 1: Quick Install (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chethanyadav456/WinFlux.git
   cd WinFlux
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run WinFlux:**
   ```bash
   python winflux.py --help
   ```

### Method 2: Install as Package

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chethanyadav456/WinFlux.git
   cd WinFlux
   ```

2. **Install the package:**
   ```bash
   pip install -e .
   ```

3. **Use the `winflux` command globally:**
   ```bash
   winflux --help
   winflux clean
   winflux report
   ```

### Method 3: Create Standalone Executable (PyInstaller)

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Build executable:**
   ```bash
   pyinstaller --onefile --name winflux winflux.py
   ```

3. **Executable will be in `dist/` folder:**
   ```bash
   dist\winflux.exe --help
   ```

## First Run

After installation, run your first command:

```bash
# View help
python winflux.py --help

# Generate system report
python winflux.py report

# Test with dry-run mode
python winflux.py clean --dry-run
```

## Configuration

WinFlux automatically creates a configuration directory on first run:

- **Config location:** `C:\Users\YourName\.winflux\`
- **Config file:** `C:\Users\YourName\.winflux\config.json`
- **Logs:** `C:\Users\YourName\.winflux\logs\`

### View Configuration

```bash
python winflux.py config --show
```

### Modify Configuration

```bash
# Disable confirmation prompts
python winflux.py config --set auto_confirm=true

# Hide banner
python winflux.py config --set show_banner=false
```

## Running as Administrator

Some operations require administrator privileges:

1. **Right-click Command Prompt or PowerShell**
2. **Select "Run as administrator"**
3. **Navigate to WinFlux directory**
4. **Run commands normally**

```powershell
cd C:\path\to\WinFlux
python winflux.py clean
```

## Troubleshooting

### Issue: Module not found errors

**Solution:** Ensure all dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Permission denied errors

**Solution:** Run as administrator or check file permissions

### Issue: winshell module errors

**Solution:** Install manually
```bash
pip install winshell pywin32
```

### Issue: Python not recognized

**Solution:** Add Python to PATH or use full path
```bash
C:\Python310\python.exe winflux.py --help
```

## Updating WinFlux

```bash
cd WinFlux
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstallation

```bash
# If installed as package
pip uninstall winflux

# Remove configuration (optional)
rmdir /s C:\Users\YourName\.winflux
```

## Scheduled Tasks (Automation)

### Create a scheduled cleanup task:

1. Open **Task Scheduler**
2. Create **Basic Task**
3. Set trigger (e.g., daily at 2 AM)
4. Action: **Start a program**
5. Program: `C:\Python310\python.exe`
6. Arguments: `C:\path\to\WinFlux\winflux.py clean`
7. Check **Run with highest privileges**

Or use this PowerShell script:

```powershell
$action = New-ScheduledTaskAction -Execute 'python' -Argument 'C:\path\to\WinFlux\winflux.py clean'
$trigger = New-ScheduledTaskTrigger -Daily -At 2am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "WinFlux Cleanup" -Description "Daily system cleanup"
```

## Next Steps

1. Read [EXAMPLES.md](EXAMPLES.md) for usage examples
2. Check [README.md](README.md) for feature documentation
3. Review logs in `~/.winflux/logs/` after operations

## Support

For issues or questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review documentation

---

**Happy Optimizing! 🚀**
