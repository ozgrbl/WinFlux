#!/usr/bin/env python3
"""
WinFlux - Windows System Optimizer
A powerful CLI tool for cleaning, optimizing, and analyzing Windows systems.

This is the standalone entry point that uses the modular winflux package.
For development, you can also use: python -m winflux.cli
"""

import click
import logging
import ctypes
from rich.console import Console
from rich.table import Table

# Import from modular package
from winflux.config import setup_logging, load_config, save_config, CONFIG_FILE
from winflux.modules import CleanupModule, AnalyzeModule, OptimizeModule, ReportModule
from winflux.modules.utils import format_bytes

# Initialize console
console = Console()

# Version
__version__ = "1.0.0"

# ASCII Banner
BANNER = """
╦ ╦┬┌┐┌╔═╗┬  ┬ ┬─┐ ┬
║║║││││╠╣ │  │ │┌┴┬┘
╚╩╝┴┘└┘╚  ┴─┘└─┘┴ └─
System Optimizer v{version}
"""


def is_admin():
    """Check if the script is running with admin privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def show_banner():
    """Display the WinFlux banner."""
    config = load_config()
    if config.get("show_banner", True):
        console.print(BANNER.format(version=__version__), style="bold cyan")


# ============================================================================
# CLI COMMANDS
# ============================================================================

@click.group()
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx):
    """WinFlux - Windows System Optimizer
    
    A powerful CLI tool for cleaning, optimizing, and analyzing your Windows system.
    """
    setup_logging()
    show_banner()


@cli.command()
@click.option('--dry-run', is_flag=True, help='Preview actions without making changes')
@click.option('--temp', is_flag=True, help='Clean only temporary files')
@click.option('--cache', is_flag=True, help='Clean only browser cache')
@click.option('--all', 'clean_all', is_flag=True, help='Clean everything (default)')
def clean(dry_run, temp, cache, clean_all):
    """Clean temporary files, cache, and junk."""
    
    if dry_run:
        console.print("[yellow]🔍 DRY RUN MODE - No changes will be made[/yellow]\n")
    
    config = load_config()
    
    if not dry_run and not config.get('auto_confirm', False):
        if not click.confirm('This will delete files. Continue?'):
            console.print("[yellow]Operation cancelled.[/yellow]")
            return
    
    cleanup = CleanupModule(dry_run=dry_run)
    
    # If no specific option, clean all
    if not (temp or cache) or clean_all:
        cleanup.clean_temp_files()
        cleanup.clean_browser_cache()
        cleanup.clean_recycle_bin()
        cleanup.clean_junk_files()
    else:
        if temp:
            cleanup.clean_temp_files()
        if cache:
            cleanup.clean_browser_cache()
    
    console.print(f"\n[bold green]{'Summary (Dry Run)' if dry_run else 'Cleanup Complete!'}[/bold green]")
    console.print(f"Total space {'that would be' if dry_run else ''} freed: [bold]{format_bytes(cleanup.freed_space)}[/bold]")
    
    logging.info(f"Cleanup completed. Freed: {format_bytes(cleanup.freed_space)}")


@cli.command()
@click.option('--path', default='C:\\', help='Path to analyze (default: C:\\)')
@click.option('--top', default=10, help='Number of top items to show (default: 10)')
def analyze(path, top):
    """Analyze disk usage and show largest files/folders."""
    analyzer = AnalyzeModule()
    analyzer.analyze_disk_usage(path=path, top_n=top)
    
    logging.info(f"Disk analysis completed for {path}")


@cli.command()
@click.option('--startup', is_flag=True, help='Show startup programs')
def optimize(startup):
    """Optimize system performance."""
    
    if not is_admin():
        console.print("[yellow]⚠️  Some optimizations may require administrator privileges[/yellow]\n")
    
    optimizer = OptimizeModule()
    
    if startup or True:  # Default to showing startup
        optimizer.list_startup_programs()
    
    logging.info("System optimization completed")


@cli.command()
def report():
    """Generate comprehensive system health report."""
    reporter = ReportModule()
    reporter.generate_report()
    
    logging.info("System report generated")


@cli.command()
@click.option('--set', 'set_option', help='Set config option (format: key=value)')
@click.option('--show', is_flag=True, help='Show current configuration')
def config(set_option, show):
    """Manage WinFlux configuration."""
    
    current_config = load_config()
    
    if show or (not set_option):
        console.print("\n[cyan]Current Configuration:[/cyan]\n")
        table = Table(show_header=True)
        table.add_column("Option", style="cyan")
        table.add_column("Value", style="yellow")
        
        for key, value in current_config.items():
            table.add_row(key, str(value))
        
        console.print(table)
        console.print(f"\n[dim]Config file: {CONFIG_FILE}[/dim]")
    
    if set_option:
        try:
            key, value = set_option.split('=')
            key = key.strip()
            value = value.strip()
            
            # Convert value to appropriate type
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            
            current_config[key] = value
            save_config(current_config)
            console.print(f"[green]✓ Set {key} = {value}[/green]")
        except ValueError:
            console.print("[red]Invalid format. Use: key=value[/red]")


if __name__ == '__main__':
    cli()
