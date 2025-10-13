"""
Report Module - System health reporting
"""

import psutil
from datetime import datetime
from rich.console import Console
from rich.table import Table
from .utils import format_bytes

console = Console()


class ReportModule:
    """Generate system health reports."""
    
    def generate_report(self):
        """Generate comprehensive system health report."""
        console.print("\n[cyan]📊 Generating system health report...[/cyan]\n")
        
        # CPU Information
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        
        cpu_table = Table(title="🖥️  CPU Information", show_header=True)
        cpu_table.add_column("Metric", style="cyan")
        cpu_table.add_column("Value", style="yellow")
        
        cpu_table.add_row("CPU Usage", f"{cpu_percent}%")
        cpu_table.add_row("CPU Cores", str(cpu_count))
        if cpu_freq:
            cpu_table.add_row("CPU Frequency", f"{cpu_freq.current:.2f} MHz")
        
        console.print(cpu_table)
        
        # Memory Information
        memory = psutil.virtual_memory()
        
        memory_table = Table(title="🧠 Memory Information", show_header=True)
        memory_table.add_column("Metric", style="cyan")
        memory_table.add_column("Value", style="yellow")
        
        memory_table.add_row("Total RAM", format_bytes(memory.total))
        memory_table.add_row("Available", format_bytes(memory.available))
        memory_table.add_row("Used", format_bytes(memory.used))
        memory_table.add_row("Usage", f"{memory.percent}%")
        
        console.print(memory_table)
        
        # Disk Information
        disk_table = Table(title="💾 Disk Information", show_header=True)
        disk_table.add_column("Drive", style="cyan")
        disk_table.add_column("Total", style="yellow")
        disk_table.add_column("Used", style="red")
        disk_table.add_column("Free", style="green")
        disk_table.add_column("Usage", style="magenta")
        
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_table.add_row(
                    partition.device,
                    format_bytes(usage.total),
                    format_bytes(usage.used),
                    format_bytes(usage.free),
                    f"{usage.percent}%"
                )
            except:
                pass
        
        console.print(disk_table)
        
        # System Uptime
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        
        system_table = Table(title="⚙️  System Information", show_header=True)
        system_table.add_column("Metric", style="cyan")
        system_table.add_column("Value", style="yellow")
        
        system_table.add_row("Boot Time", boot_time.strftime("%Y-%m-%d %H:%M:%S"))
        system_table.add_row("Uptime", str(uptime).split('.')[0])
        
        console.print(system_table)
        
        # Health Summary
        console.print("\n[bold cyan]📋 Health Summary:[/bold cyan]")
        
        issues = []
        if cpu_percent > 80:
            issues.append("⚠️  High CPU usage detected")
        if memory.percent > 85:
            issues.append("⚠️  High memory usage detected")
        
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                if usage.percent > 90:
                    issues.append(f"⚠️  Low disk space on {partition.device}")
            except:
                pass
        
        if issues:
            for issue in issues:
                console.print(f"[yellow]{issue}[/yellow]")
        else:
            console.print("[green]✓ System health is good![/green]")
