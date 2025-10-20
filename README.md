# readme-gen

A small CLI tool that generates clean, basic README.md files.

## Features

- Interactive CLI interface
- Generates professional README.md files
- Uses Jinja2 templates for customization
- Configurable default values
- Easy to install and use

## Installation

```bash
pip install .
```

For development installation:

```bash
pip install -e .
```

## Usage

Run the interactive CLI:

```bash
readme-gen
```

The tool will prompt you for:
- Project name
- Short description
- Installation instructions
- Usage examples
- Tech stack/dependencies
- Author information
- License type

### Example Output

The generated README will include all essential sections organized in a clean, professional format.

## Requirements

- Python >= 3.8
- Jinja2

## Development

To contribute to the project:

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
3. Run tests:
   ```bash
   pytest
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

8bitDevStudios (8Bit)
