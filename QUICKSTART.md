# 🚀 WinFlux Quick Reference Card

## ⚡ Most Used Commands

```bash
# System Health Check
python winflux.py report

# Find Space Hogs
python winflux.py analyze

# Safe Cleanup Preview
python winflux.py clean --dry-run

# Actual Cleanup
python winflux.py clean

# Show Startup Programs
python winflux.py optimize
```

## 📋 Command Cheat Sheet

| What You Want | Command |
|---------------|---------|
| Check system health | `python winflux.py report` |
| Find largest files | `python winflux.py analyze` |
| Preview cleanup | `python winflux.py clean --dry-run` |
| Clean everything | `python winflux.py clean` |
| Clean temp only | `python winflux.py clean --temp` |
| Clean cache only | `python winflux.py clean --cache` |
| Show startup apps | `python winflux.py optimize` |
| View settings | `python winflux.py config --show` |
| Get help | `python winflux.py --help` |
| Check version | `python winflux.py --version` |

## 🎯 Common Workflows

### Weekly Maintenance
```bash
python winflux.py report        # Check health
python winflux.py analyze       # Find space hogs
python winflux.py clean         # Clean up
```

### Free Up Space Fast
```bash
python winflux.py clean --dry-run    # Preview first
python winflux.py clean              # Clean for real
```

### System Performance Check
```bash
python winflux.py report        # Overall health
python winflux.py optimize      # Startup programs
```

## 💡 Pro Tips

1. **Always preview first**: `--dry-run` is your friend
2. **Run as admin**: For best results
3. **Close browsers**: Before cleaning cache
4. **Check logs**: Located in `~/.winflux/logs/`
5. **Weekly cleanup**: Keep your system fresh

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python not found" | Add Python to PATH or use full path |
| Permission errors | Run Command Prompt as Administrator |
| Module errors | Run `pip install -r requirements.txt` |
| Nothing cleaned | Normal! Only cleans safe temp files |

## 📁 What Gets Cleaned

✅ **Safe to remove:**
- Temp files (%TEMP%)
- Browser cache
- Windows logs
- Crash dumps
- Update leftovers

❌ **Never touched:**
- Your documents
- Installed programs
- System files
- Personal files

## ⚙️ Configuration

```bash
# View current config
python winflux.py config --show

# Skip confirmations
python winflux.py config --set auto_confirm=true

# Hide banner
python winflux.py config --set show_banner=false
```

## 📍 Important Locations

- **Config**: `~/.winflux/config.json`
- **Logs**: `~/.winflux/logs/`
- **Source**: Where you downloaded WinFlux

## 🎓 Learning Path

1. Start → Read [README.md](README.md)
2. Install → Follow [INSTALL.md](INSTALL.md)
3. Practice → Try [EXAMPLES.md](EXAMPLES.md)
4. Deep Dive → Check [STRUCTURE.md](STRUCTURE.md)
5. Contribute → Read [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Keep this handy!** Bookmark or print for quick reference.
