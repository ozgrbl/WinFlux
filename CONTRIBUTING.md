# Contributing to WinFlux

First off, thank you for considering contributing to WinFlux! It's people like you that make WinFlux such a great tool.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what is best for the community

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if relevant**
- **Include your environment details:**
  - Windows version
  - Python version
  - WinFlux version

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit a pull request**

## Development Setup

### 1. Clone your fork

```bash
git clone https://github.com/chethanyadav456/WinFlux.git
cd WinFlux
```

### 2. Create a virtual environment

```bash
python -m venv venv
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

### 4. Create a feature branch

```bash
git checkout -b feature/amazing-feature
```

## Coding Standards

### Python Style Guide

- Follow **PEP 8** style guide
- Use **type hints** where appropriate
- Write **docstrings** for all functions and classes
- Keep functions **small and focused**
- Use **meaningful variable names**

### Example:

```python
def clean_temp_files(self) -> None:
    """
    Clean temporary files from system temp directories.
    
    This method scans and removes files from:
    - %TEMP%
    - Windows\Temp
    - Prefetch folder
    
    Raises:
        PermissionError: If admin privileges are required
    """
    # Implementation here
    pass
```

### Documentation

- Update README.md if you change functionality
- Update EXAMPLES.md with usage examples
- Add docstrings to new functions/classes
- Comment complex logic

### Testing

```bash
# Run tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_cleanup.py
```

### Adding New Features

When adding a new feature:

1. **Create a new module** in `winflux/modules/` if needed
2. **Add CLI command** in `winflux/cli.py`
3. **Write tests** in `tests/`
4. **Update documentation**
5. **Add example output** to EXAMPLES.md

### Example: Adding a new module

```python
# winflux/modules/new_feature.py
"""
New Feature Module - Description
"""

from rich.console import Console

console = Console()


class NewFeatureModule:
    """Handle new feature operations."""
    
    def __init__(self):
        pass
    
    def do_something(self):
        """Do something useful."""
        console.print("[cyan]Doing something...[/cyan]")
```

Then add to CLI:

```python
# winflux/cli.py

@cli.command()
def newfeature():
    """Description of new feature."""
    from .modules.new_feature import NewFeatureModule
    module = NewFeatureModule()
    module.do_something()
```

## Commit Message Guidelines

Use clear and meaningful commit messages:

### Format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples:

```
feat(cleanup): add support for cleaning Windows.old folder

- Added detection for Windows.old folder
- Implemented safe deletion with confirmation
- Added size calculation before deletion

Closes #123
```

```
fix(analyze): correct disk usage calculation for symbolic links

The previous implementation counted symbolic links twice,
leading to incorrect disk usage reports.

Fixes #456
```

## Testing Checklist

Before submitting a PR, ensure:

- [ ] Code follows PEP 8 style guide
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Examples are provided
- [ ] Commit messages are clear
- [ ] No debug code or print statements
- [ ] Code works on Windows 10/11

## Review Process

1. **Automated checks** will run on your PR
2. **Maintainers** will review your code
3. **Changes may be requested** - don't take it personally!
4. Once approved, your PR will be **merged**

## Questions?

Feel free to:
- Open an issue with the **question** label
- Join our discussions
- Reach out to maintainers

## Recognition

Contributors will be:
- Listed in README.md
- Credited in release notes
- Given our eternal gratitude! 🎉

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to WinFlux! 💙
