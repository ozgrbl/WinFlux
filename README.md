# 🚀 WinFlux - Windows System Optimizer

> **A simple, powerful, and beginner-friendly CLI tool to clean and optimize your Windows PC**

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Beginner Friendly](https://img.shields.io/badge/beginner-friendly-brightgreen.svg)

---

## 🎯 What is WinFlux?

**WinFlux** is a command-line tool that helps you keep your Windows computer running fast and clean! Think of it as a digital cleaning crew for your PC that:

- 🧹 **Cleans up junk files** that slow down your computer
- 📊 **Shows you what's taking up space** on your hard drive
- ⚡ **Helps optimize your system** for better performance
- 🔍 **Generates health reports** so you know how your PC is doing

**Perfect for:**
- Beginners learning command-line tools
- Anyone wanting to free up disk space
- People who want to understand their system better
- Developers who need a quick system cleanup utility

---

## ✨ Features (In Simple Terms!)

### 🧹 Clean Command
**What it does:** Removes temporary files, browser cache, and junk that accumulates over time

**Why you need it:** These files can take up gigabytes of space and slow down your computer

```bash
python winflux.py clean
```

### 🔍 Analyze Command
**What it does:** Shows you the biggest files and folders on your computer

**Why you need it:** Find out what's eating up all your disk space!

```bash
python winflux.py analyze
```

### 📊 Report Command
**What it does:** Creates a health report with CPU, RAM, and disk usage

**Why you need it:** Know if your computer is running normally or if something's wrong

```bash
python winflux.py report
```

### ⚙️ Optimize Command
**What it does:** Shows programs that start when your computer boots

**Why you need it:** Too many startup programs can make your computer slow to start

```bash
python winflux.py optimize
```

---

## 🎓 Installation (Step-by-Step for Beginners)

### Step 1: Check if you have Python installed

1. Open **Command Prompt** (Search for "cmd" in Windows)
2. Type this and press Enter:
   ```bash
   python --version
   ```
3. You should see something like `Python 3.10.0` or higher
   - ✅ If yes, great! Move to Step 2
   - ❌ If you see an error, [download Python here](https://www.python.org/downloads/)

### Step 2: Download WinFlux

**Option A: Download ZIP (Easiest)**
1. Click the green "Code" button on GitHub
2. Click "Download ZIP"
3. Extract the ZIP file to a folder (like `C:\WinFlux`)

**Option B: Use Git (If you know how)**
```bash
git clone https://github.com/chethanyadav456/WinFlux.git
cd WinFlux
```

### Step 3: Install Required Libraries

1. Open Command Prompt
2. Navigate to the WinFlux folder:
   ```bash
   cd C:\WinFlux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
Wait for it to finish installing. You should see "Successfully installed..." messages.

### Step 4: Run Your First Command!

```bash
python winflux.py --help
```

If you see a menu with commands, **congratulations!** 🎉 You're ready to use WinFlux!

---

## 🎮 How to Use (Quick Start Guide)

### 1️⃣ Check Your System Health

Let's see how your computer is doing:

```bash
python winflux.py report
```

**You'll see:**
- CPU usage (how hard your processor is working)
- RAM usage (how much memory you're using)
- Disk space (how full your hard drive is)
- System uptime (how long your computer has been running)

### 2️⃣ Find Space Hogs

See what's taking up the most space:

```bash
python winflux.py analyze
```

**You'll get a list** of your biggest files and folders, sorted by size!

### 3️⃣ Clean Up Safely (Test Mode)

Before deleting anything, let's do a **dry run** (preview mode):

```bash
python winflux.py clean --dry-run
```

This shows you **what would be deleted** without actually deleting anything. Safe!

### 4️⃣ Actually Clean Your System

When you're ready to clean for real:

```bash
python winflux.py clean
```

**The tool will ask for confirmation** before deleting anything. Just type `y` and press Enter.

---

## 📚 All Commands Explained

### Basic Commands

| Command | What It Does | Example |
|---------|-------------|---------|
| `--help` | Shows all available commands | `python winflux.py --help` |
| `--version` | Shows WinFlux version | `python winflux.py --version` |

### Main Features

#### 🧹 Clean Command

```bash
# Clean everything (temp files, cache, etc.)
python winflux.py clean

# Preview what will be cleaned (doesn't delete)
python winflux.py clean --dry-run

# Clean only temporary files
python winflux.py clean --temp

# Clean only browser cache
python winflux.py clean --cache
```

#### 🔍 Analyze Command

```bash
# Analyze C: drive (default)
python winflux.py analyze

# Analyze a specific drive
python winflux.py analyze --path "D:\\"

# Show more results (default is 10)
python winflux.py analyze --top 20
```

#### 📊 Report Command

```bash
# Generate system health report
python winflux.py report
```

#### ⚙️ Optimize Command

```bash
# Show startup programs
python winflux.py optimize
```

#### ⚙️ Config Command

```bash
# Show current settings
python winflux.py config --show

# Change a setting
python winflux.py config --set auto_confirm=true
```

---

## 🛡️ Safety Features

**Don't worry, WinFlux is designed to be safe!**

✅ **Dry Run Mode** - Preview changes before making them  
✅ **Confirmation Prompts** - Always asks before deleting  
✅ **Detailed Logging** - Keeps a record of everything it does  
✅ **Smart Targeting** - Only cleans safe, temporary files  

---

## ❓ Common Questions (FAQ)

### Q: Will this delete my important files?
**A:** No! WinFlux only targets temporary files, cache, and junk. Your documents, photos, and programs are safe.

### Q: Do I need to run as Administrator?
**A:** Some features work better with admin rights, but you can use most features without it. If needed, right-click Command Prompt and select "Run as administrator".

### Q: How much space can I free up?
**A:** It depends on your system, but typically 1-5 GB. Use `--dry-run` to see beforehand!

### Q: Can I undo what WinFlux does?
**A:** Deleted files go to the Recycle Bin when possible. But it's best to use `--dry-run` first to preview.

### Q: Is this safe to use?
**A:** Yes! The code is open-source (you can review it), and it only cleans standard temporary locations that Windows itself cleans.

### Q: My antivirus flagged it!
**A:** Some antivirus software flags system-level tools. This is a false positive. You can check the code yourself - it's all visible!

---

## 🎯 Real-World Examples

### Example 1: Weekly Cleanup Routine

```bash
# Step 1: Check system health
python winflux.py report

# Step 2: See what's taking up space
python winflux.py analyze

# Step 3: Clean up (with preview first)
python winflux.py clean --dry-run
python winflux.py clean
```

### Example 2: Freeing Space for a Big Game

```bash
# Find the biggest files
python winflux.py analyze --top 20

# Clean everything to free maximum space
python winflux.py clean
```

### Example 3: Speeding Up Boot Time

```bash
# See what's starting with Windows
python winflux.py optimize

# Then use Task Manager to disable unwanted programs
```

---

## 📂 What Gets Cleaned?

### ✅ Safe to Clean (What WinFlux Removes)

- **Temporary Files** - Files in %TEMP% folder
- **Prefetch Files** - Windows performance cache
- **Browser Cache** - Chrome, Edge, Firefox cached web data
- **Windows Logs** - Old Windows log files
- **Crash Dumps** - Error reports
- **Update Leftovers** - Old Windows update files

### ❌ Never Touched (Your Safe Data)

- Documents, Photos, Videos
- Installed Programs
- System Files (critical Windows files)
- User Settings
- Game Saves
- Personal Files

---

## 🔧 Troubleshooting

### Problem: "Python is not recognized"

**Solution:** Python isn't in your PATH. Either:
1. Reinstall Python and check "Add Python to PATH"
2. Use the full path: `C:\Python310\python.exe winflux.py --help`

### Problem: "Permission denied" errors

**Solution:** Run Command Prompt as Administrator
1. Search for "cmd"
2. Right-click "Command Prompt"
3. Select "Run as administrator"

### Problem: "Module not found" errors

**Solution:** Install dependencies again:
```bash
pip install -r requirements.txt
```

### Problem: Tool runs but doesn't clean much

**Solution:** This is normal! It only cleans safe temporary files. For deeper cleaning, you may need specialized tools or manual cleanup.

---

## 🎓 Learning Resources

**New to Command Line?**
- [Command Prompt Basics](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/)
- [Python Beginner Guide](https://www.python.org/about/gettingstarted/)

**Want to Learn More?**
- Check out [EXAMPLES.md](EXAMPLES.md) for detailed examples
- Read [STRUCTURE.md](STRUCTURE.md) to understand how WinFlux works
- See [CONTRIBUTING.md](CONTRIBUTING.md) if you want to help improve WinFlux

---

## 🤝 Contributing

Want to make WinFlux better? We welcome contributions!

- 🐛 Found a bug? [Open an issue](https://github.com/chethanyadav456/WinFlux/issues)
- 💡 Have an idea? [Start a discussion](https://github.com/chethanyadav456/WinFlux/discussions)
- 🔧 Want to code? Check out [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📝 License

This project is licensed under the **MIT License** - which means you can use it, modify it, and share it freely! See [LICENSE](LICENSE) for details.

---

## ⚠️ Important Notes

1. **Always preview before cleaning**: Use `--dry-run` first
2. **Back up important data**: Just good practice!
3. **Close browsers before cleaning cache**: For best results
4. **Run as admin when asked**: Some operations need it
5. **Check logs if something goes wrong**: Located in `~/.winflux/logs/`

---

## 🌟 Show Your Support

If WinFlux helped you:
- ⭐ Star this repository on GitHub
- 📢 Share it with friends
- 🐛 Report bugs to help us improve
- 💖 Consider contributing

---

## 📧 Need Help?

- 📖 Read the [documentation](https://github.com/chethanyadav456/WinFlux/wiki)
- 💬 Ask in [discussions](https://github.com/chethanyadav456/WinFlux/discussions)
- 🐛 Report issues [here](https://github.com/chethanyadav456/WinFlux/issues)

---

<div align="center">

**Made with ❤️ for Windows users who want a cleaner, faster PC**

[⬆ Back to Top](#-winflux---windows-system-optimizer)

</div>
