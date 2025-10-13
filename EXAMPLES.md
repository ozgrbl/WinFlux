# WinFlux Examples

This document provides sample outputs and usage examples for WinFlux commands.

## Example 1: System Report

```bash
python winflux.py report
```

**Output:**
```
╦ ╦┬┌┐┌╔═╗┬  ┬ ┬─┐ ┬
║║║││││╠╣ │  │ │┌┴┬┘
╚╩╝┴┘└┘╚  ┴─┘└─┘┴ └─
System Optimizer v1.0.0

📊 Generating system health report...

┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Metric         ┃ Value      ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ CPU Usage      │ 34.5%      │
│ CPU Cores      │ 8          │
│ CPU Frequency  │ 3600.00 MHz│
└────────────────┴────────────┘

┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Metric         ┃ Value      ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Total RAM      │ 16.00 GB   │
│ Available      │ 8.45 GB    │
│ Used           │ 7.55 GB    │
│ Usage          │ 47.2%      │
└────────────────┴────────────┘

┏━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┓
┃ Drive  ┃ Total    ┃ Used     ┃ Free     ┃ Usage ┃
┡━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━┩
│ C:\    │ 476.94 GB│ 234.56 GB│ 242.38 GB│ 49.2% │
│ D:\    │ 931.51 GB│ 567.89 GB│ 363.62 GB│ 61.0% │
└────────┴──────────┴──────────┴──────────┴───────┘

┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric    ┃ Value               ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ Boot Time │ 2025-10-13 08:30:45 │
│ Uptime    │ 1 day, 5:23:12      │
└───────────┴─────────────────────┘

📋 Health Summary:
✓ System health is good!
```

## Example 2: Disk Analysis

```bash
python winflux.py analyze --path "C:\\" --top 15
```

**Output:**
```
🔍 Analyzing disk usage for C:\...

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┓
┃ Path                             ┃      Size ┃ Type   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━┩
│ C:\Program Files                 │ 45.23 GB  │ Folder │
│ C:\Windows                       │ 38.67 GB  │ Folder │
│ C:\Users                         │ 28.45 GB  │ Folder │
│ C:\ProgramData                   │ 12.34 GB  │ Folder │
│ C:\hiberfil.sys                  │  8.00 GB  │ File   │
│ C:\pagefile.sys                  │  6.00 GB  │ File   │
│ C:\swapfile.sys                  │  1.50 GB  │ Folder │
│ C:\Intel                         │  1.23 GB  │ Folder │
│ C:\AMD                           │  856.45 MB│ Folder │
│ C:\Temp                          │  234.56 MB│ Folder │
│ C:\Recovery                      │  123.45 MB│ Folder │
│ C:\PerfLogs                      │   45.23 MB│ Folder │
│ C:\$Recycle.Bin                  │   12.34 MB│ Folder │
│ C:\bootTel.dat                   │    2.45 MB│ File   │
│ C:\DumpStack.log                 │    1.23 MB│ File   │
└──────────────────────────────────┴───────────┴────────┘

Total analyzed: 142.51 GB
```

## Example 3: Cleanup (Dry Run)

```bash
python winflux.py clean --dry-run
```

**Output:**
```
🔍 DRY RUN MODE - No changes will be made

🧹 Cleaning temporary files...
Would free 2.35 GB from 1,247 items

🌐 Cleaning browser cache...
✓ Cleaned Chrome cache (458.67 MB)
✓ Cleaned Edge cache (234.12 MB)

🗑️  Emptying recycle bin...
Would empty recycle bin

🪣 Removing junk files...
✓ Cleaned Logs (123.45 MB)
✓ Cleaned Download (567.89 MB)
✓ Cleaned CrashDumps (45.67 MB)
✓ Cleaned Temp (234.56 MB)

Summary (Dry Run)
Total space that would be freed: 3.04 GB
```

## Example 4: Cleanup (Actual)

```bash
python winflux.py clean
```

**Output:**
```
This will delete files. Continue? [y/N]: y

🧹 Cleaning temporary files...
✓ Freed 2.35 GB from 1,247 items

🌐 Cleaning browser cache...
✓ Cleaned Chrome cache (458.67 MB)
✓ Cleaned Edge cache (234.12 MB)

🗑️  Emptying recycle bin...
✓ Recycle bin emptied successfully

🪣 Removing junk files...
✓ Cleaned Logs (123.45 MB)
✓ Cleaned Download (567.89 MB)
✓ Cleaned CrashDumps (45.67 MB)
✓ Cleaned Temp (234.56 MB)

Cleanup Complete!
Total space freed: 3.04 GB
```

## Example 5: Optimize - Startup Programs

```bash
python winflux.py optimize --startup
```

**Output:**
```
⚙️  Analyzing startup programs...

┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Name              ┃ Path                                      ┃ Location┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ OneDrive          │ C:\Program Files\Microsoft OneDrive\...  │ User   │
│ Discord           │ C:\Users\User\AppData\Local\Discord\...  │ User   │
│ Steam             │ C:\Program Files (x86)\Steam\steam.exe   │ User   │
│ Spotify           │ C:\Users\User\AppData\Roaming\Spotify\...│ User   │
│ Adobe CC          │ C:\Program Files\Adobe\Adobe Creative... │ System │
│ NVIDIA GeForce... │ C:\Program Files\NVIDIA Corporation\...  │ System │
└───────────────────┴───────────────────────────────────────────┴────────┘

ℹ️  Use Task Manager to disable specific startup programs
```

## Example 6: Configuration Management

```bash
python winflux.py config --show
```

**Output:**
```
Current Configuration:

┏━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Option        ┃ Value ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━┩
│ auto_confirm  │ False │
│ show_banner   │ True  │
│ log_level     │ INFO  │
│ backup_enabled│ True  │
└───────────────┴───────┘

Config file: C:\Users\User\.winflux\config.json
```

```bash
python winflux.py config --set auto_confirm=true
```

**Output:**
```
✓ Set auto_confirm = True
```

## Usage Patterns

### Daily Maintenance
```bash
# Quick cleanup with confirmation
python winflux.py clean

# Generate daily health report
python winflux.py report
```

### Deep Cleaning
```bash
# Preview what will be cleaned
python winflux.py clean --dry-run

# If satisfied, run actual cleanup
python winflux.py clean
```

### System Analysis
```bash
# Analyze C: drive
python winflux.py analyze

# Analyze specific drive
python winflux.py analyze --path "D:\\"

# Show more results
python winflux.py analyze --top 20
```

### Scheduled Optimization
```bash
# Disable auto-confirm for scheduled tasks
python winflux.py config --set auto_confirm=true

# Run cleanup without prompts
python winflux.py clean
```
