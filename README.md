# PyCheckout

A fast, intuitive Git branch management CLI with an interactive terminal UI. Checkout and delete branches effortlessly with autocomplete and beautiful TUI navigation.

## ✨ Features

- 🎯 **Interactive Branch Selection** - Beautiful terminal UI for browsing and selecting branches
- ⚡ **Fast Switching** - Quickly checkout any local branch
- 🗑️ **Branch Deletion** - Delete branches with confirmation
- 🖥️ **Dual Mode** - Use interactive TUI or command-line arguments
- 🎨 **Rich Output** - Color-coded errors and status messages with `rich`
- 📦 **Type Safe** - Full type hints with `py` type checking
- 🧪 **Well Tested** - Comprehensive test suite with `pytest`

## 🎬 Demo

<!-- DEMO VIDEO PLACEHOLDER -->
> Demo video coming soon! Check back for an interactive walkthrough of PyCheckout's features.
<!-- END DEMO VIDEO PLACEHOLDER -->

## 🚀 Quick Start

### Installation

```bash
pip install pycheckout
```

Or with `uv`:
```bash
uv add pycheckout
```

### Basic Usage

Navigate to your git repository and run:

```bash
pycheckout
```

This opens the interactive TUI where you can:
- Use arrow keys to navigate branches
- Press Enter to checkout a branch
- See the currently checked out branch highlighted in green

## 📖 Usage Examples

### Interactive Mode (Default)

```bash
# Open interactive branch selector
pycheckout

# Delete a branch interactively
pycheckout --delete
# or
pycheckout -d
```

### Command-Line Mode

```bash
# Checkout a specific branch
pycheckout feature/my-feature

# Delete a specific branch
pycheckout feature/old-feature --delete
pycheckout feature/old-feature -d
```

### Programmatic Usage

```python
from pycheckout import PyCheckout

# Create instance
pychkt = PyCheckout(repo_path="/path/to/repo", use_tui=False)

# Checkout a branch
pychkt.checkout("main")

# Delete a branch
pychkt.delete_branch("feature/done")

# Get current branch
current = pychkt.checked_out_branch
print(f"Currently on: {current}")

# List all local branches
branches = pychkt.local_branches
print(f"Available branches: {branches}")
```

## 🛠️ Installation for Development

### Prerequisites

- Python 3.14+
- `uv` package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/pycheckout.git
cd pycheckout

# Install with dev dependencies
uv sync --group dev

# Run tests
uv run pytest

# Run linters
uv run ruff check .
uv run ty check
```

## 📋 API Reference

### PyCheckout Class

#### `__init__(repo_path: str | Path | None = None, use_tui: bool = True)`

Initialize a PyCheckout instance.

**Parameters:**
- `repo_path`: Path to git repository (defaults to current directory)
- `use_tui`: Enable/disable interactive TUI mode

**Example:**
```python
pychkt = PyCheckout(repo_path=".", use_tui=True)
```

#### `checkout(branch_name: str | None = None)`

Checkout to a branch.

**Parameters:**
- `branch_name`: Branch to checkout to. If `None` and TUI is enabled, opens interactive selector.

**Raises:**
- `PyCheckoutError`: If branch not found or repository not initialized

#### `delete_branch(branch_name: str | None = None)`

Delete a local branch.

**Parameters:**
- `branch_name`: Branch to delete. If `None` and TUI is enabled, opens interactive selector.

**Raises:**
- `PyCheckoutError`: If branch not found, currently checked out, or repository not initialized

#### Properties

- `repository: str | None` - Path to the git repository
- `local_branches: list[str]` - List of all local branch names
- `checked_out_branch: str` - Name of currently checked out branch

### PyCheckoutError Exception

Custom exception raised by PyCheckout for all error conditions.

```python
from pycheckout import PyCheckoutError

try:
    pychkt.checkout("nonexistent-branch")
except PyCheckoutError as e:
    print(f"Error: {e}")
```

## 🔧 Configuration

PyCheckout respects your Git configuration and requires a valid git repository.

### Environment Variables

None currently required.

### Git Requirements

- Must be run inside a git repository
- Requires local branches to switch/delete

## 🧪 Testing

Run the test suite:

```bash
uv run pytest
```

Run specific tests:

```bash
uv run pytest tests/test_pycheckout.py::TestPyCheckout::test_checkout_branch
```

Run with coverage:

```bash
uv run pytest --cov=pycheckout
```

## 🔍 Code Quality

### Linting

```bash
# Check code style with Ruff
uv run ruff check .

# Fix formatting
uv run ruff format .
```

### Type Checking

```bash
# Check types with py
uv run ty check
```

### Automated Checks

The project uses GitHub Actions to automatically run linters and type checks on every push and pull request. See `.github/workflows/linters.yml` for details.

## 📚 Project Structure

```
pycheckout/
├── pycheckout/
│   ├── __init__.py           # Package exports
│   └── pycheckout.py         # Main implementation
├── tests/
│   ├── __init__.py
│   └── test_pycheckout.py    # Test suite
├── .github/
│   └── workflows/
│       └── linters.yml       # CI/CD linters
├── pyproject.toml            # Project configuration
├── uv.lock                   # Locked dependencies
└── README.md                 # This file
```

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Write tests for new features
- Ensure all tests pass: `uv run pytest`
- Run linters: `uv run ruff check .` and `uv run ty check`
- Follow PEP 8 and type hints
- Add docstrings to functions and classes

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋 Support

Having issues? Check out:

1. **Existing Issues** - Search GitHub Issues for similar problems
2. **Documentation** - Review the API Reference section above
3. **Examples** - Check the Usage Examples section

## 🗺️ Roadmap

- [ ] Remote branch support
- [ ] Branch creation
- [ ] Branch renaming
- [ ] Fuzzy search in TUI
- [ ] Configuration file support
- [ ] Shell completion (bash, zsh, fish)
- [ ] Branch history
- [ ] Git stash integration

## 🎓 Learn More

- [pygit2 Documentation](https://www.pygit2.org/)
- [Typer Documentation](https://typer.tiangolo.com/)
- [prompt_toolkit Documentation](https://python-prompt-toolkit.readthedocs.io/)
- [Rich Documentation](https://rich.readthedocs.io/)

---

Made with ❤️ by the PyCheckout team
