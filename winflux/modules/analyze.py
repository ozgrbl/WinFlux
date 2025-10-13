"""
Analyze Module - Disk usage analysis
"""

from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from .utils import get_dir_size, format_bytes

console = Console()


class AnalyzeModule:
    """Analyze disk usage and system state."""
    
    def analyze_disk_usage(self, path='C:\\', top_n=10):
        """Analyze disk usage and show largest folders/files."""
        console.print(f"\n[cyan]🔍 Analyzing disk usage for {path}...[/cyan]")
        
        items = []
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task("Scanning directories...", total=None)
            
            try:
                for item in Path(path).iterdir():
                    try:
                        if item.is_file():
                            size = item.stat().st_size
                        else:
                            size = get_dir_size(item)
                        
                        items.append((str(item), size, 'File' if item.is_file() else 'Folder'))
                    except:
                        pass
            except Exception as e:
                console.print(f"[red]Error analyzing {path}: {e}[/red]")
                return
        
        # Sort by size
        items.sort(key=lambda x: x[1], reverse=True)
        
        # Display top N
        table = Table(title=f"Top {top_n} Largest Items in {path}", show_header=True)
        table.add_column("Path", style="cyan", no_wrap=False)
        table.add_column("Size", style="magenta", justify="right")
        table.add_column("Type", style="green")
        
        for path, size, item_type in items[:top_n]:
            table.add_row(path, format_bytes(size), item_type)
        
        console.print(table)
        
        # Show total
        total_size = sum(item[1] for item in items)
        console.print(f"\n[bold]Total analyzed: {format_bytes(total_size)}[/bold]")
