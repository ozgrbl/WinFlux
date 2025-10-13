"""
Optimize Module - System optimization operations
"""

import logging
from rich.console import Console
from rich.table import Table

console = Console()


class OptimizeModule:
    """System optimization operations."""
    
    def list_startup_programs(self):
        """List startup programs."""
        console.print("\n[cyan]⚙️  Analyzing startup programs...[/cyan]")
        
        try:
            import winreg
            
            startup_locations = [
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
                (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
            ]
            
            table = Table(title="Startup Programs", show_header=True)
            table.add_column("Name", style="cyan")
            table.add_column("Path", style="yellow", no_wrap=False)
            table.add_column("Location", style="green")
            
            for hkey, subkey in startup_locations:
                try:
                    key = winreg.OpenKey(hkey, subkey)
                    i = 0
                    while True:
                        try:
                            name, value, _ = winreg.EnumValue(key, i)
                            location = "User" if hkey == winreg.HKEY_CURRENT_USER else "System"
                            table.add_row(name, value, location)
                            i += 1
                        except WindowsError:
                            break
                    winreg.CloseKey(key)
                except Exception as e:
                    logging.warning(f"Could not access registry: {e}")
            
            console.print(table)
            console.print("\n[yellow]ℹ️  Use Task Manager to disable specific startup programs[/yellow]")
        except ImportError:
            console.print("[red]Registry access not available on this platform[/red]")
