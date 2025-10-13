"""
Cleanup Module - Handle system cleanup operations
"""

import os
import shutil
import logging
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from .utils import get_dir_size, format_bytes

console = Console()


class CleanupModule:
    """Handle system cleanup operations."""
    
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.deleted_files = 0
        self.freed_space = 0
    
    def clean_temp_files(self):
        """Clean temporary files."""
        console.print("\n[cyan]🧹 Cleaning temporary files...[/cyan]")
        
        temp_dirs = [
            Path(os.environ.get('TEMP', 'C:\\Windows\\Temp')),
            Path(os.environ.get('TMP', 'C:\\Windows\\Temp')),
            Path('C:\\Windows\\Temp'),
            Path('C:\\Windows\\Prefetch')
        ]
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task("Scanning temp directories...", total=None)
            
            for temp_dir in temp_dirs:
                if not temp_dir.exists():
                    continue
                
                progress.update(task, description=f"Cleaning {temp_dir}...")
                
                try:
                    for item in temp_dir.iterdir():
                        try:
                            size = item.stat().st_size if item.is_file() else get_dir_size(item)
                            
                            if not self.dry_run:
                                if item.is_file():
                                    item.unlink()
                                else:
                                    shutil.rmtree(item, ignore_errors=True)
                            
                            self.deleted_files += 1
                            self.freed_space += size
                            logging.info(f"Deleted: {item}")
                        except Exception as e:
                            logging.warning(f"Could not delete {item}: {e}")
                except Exception as e:
                    logging.error(f"Error accessing {temp_dir}: {e}")
        
        action = "Would free" if self.dry_run else "Freed"
        console.print(f"[green]✓ {action} {format_bytes(self.freed_space)} from {self.deleted_files} items[/green]")
    
    def clean_recycle_bin(self):
        """Empty recycle bin."""
        console.print("\n[cyan]🗑️  Emptying recycle bin...[/cyan]")
        
        if not self.dry_run:
            try:
                import winshell
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                console.print("[green]✓ Recycle bin emptied successfully[/green]")
                logging.info("Recycle bin emptied")
            except ImportError:
                console.print("[yellow]⚠️  winshell module not available. Install with: pip install winshell[/yellow]")
            except Exception as e:
                console.print(f"[red]✗ Error emptying recycle bin: {e}[/red]")
                logging.error(f"Recycle bin error: {e}")
        else:
            console.print("[yellow]Would empty recycle bin[/yellow]")
    
    def clean_browser_cache(self):
        """Clean browser cache files."""
        console.print("\n[cyan]🌐 Cleaning browser cache...[/cyan]")
        
        user_profile = Path(os.environ.get('USERPROFILE', ''))
        browsers = {
            'Chrome': user_profile / 'AppData/Local/Google/Chrome/User Data/Default/Cache',
            'Edge': user_profile / 'AppData/Local/Microsoft/Edge/User Data/Default/Cache',
            'Firefox': user_profile / 'AppData/Local/Mozilla/Firefox/Profiles'
        }
        
        for browser, cache_path in browsers.items():
            if cache_path.exists():
                try:
                    if browser == 'Firefox':
                        # Firefox has multiple profile directories
                        for profile in cache_path.iterdir():
                            cache_dir = profile / 'cache2'
                            if cache_dir.exists():
                                size = get_dir_size(cache_dir)
                                if not self.dry_run:
                                    shutil.rmtree(cache_dir, ignore_errors=True)
                                self.freed_space += size
                                console.print(f"[green]✓ Cleaned {browser} cache ({format_bytes(size)})[/green]")
                    else:
                        size = get_dir_size(cache_path)
                        if not self.dry_run:
                            shutil.rmtree(cache_path, ignore_errors=True)
                            cache_path.mkdir(parents=True, exist_ok=True)
                        self.freed_space += size
                        console.print(f"[green]✓ Cleaned {browser} cache ({format_bytes(size)})[/green]")
                    
                    logging.info(f"Cleaned {browser} cache")
                except Exception as e:
                    console.print(f"[yellow]⚠️  Could not clean {browser} cache: {e}[/yellow]")
                    logging.warning(f"{browser} cache error: {e}")
    
    def clean_junk_files(self):
        """Remove junk files (logs, dumps, etc.)."""
        console.print("\n[cyan]🪣 Removing junk files...[/cyan]")
        
        junk_patterns = [
            'C:\\Windows\\Logs',
            'C:\\Windows\\SoftwareDistribution\\Download',
            str(Path.home() / 'AppData/Local/CrashDumps'),
            str(Path.home() / 'AppData/Local/Temp')
        ]
        
        for pattern in junk_patterns:
            path = Path(pattern)
            if path.exists():
                try:
                    size = get_dir_size(path)
                    if not self.dry_run:
                        for item in path.iterdir():
                            try:
                                if item.is_file():
                                    item.unlink()
                                else:
                                    shutil.rmtree(item, ignore_errors=True)
                            except:
                                pass
                    self.freed_space += size
                    console.print(f"[green]✓ Cleaned {path.name} ({format_bytes(size)})[/green]")
                    logging.info(f"Cleaned junk from {path}")
                except Exception as e:
                    logging.warning(f"Could not clean {path}: {e}")
