<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/GreyTeamToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/greyteamtoolbox/black-and-white-circle-256.png" alt="GreyTeamToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/baseline-project/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/GreyTeamToolbox/baseline-project/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-project/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/GreyTeamToolbox/baseline-project?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-project">
        <img src="https://img.shields.io/github/created-at/GreyTeamToolbox/baseline-project?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/baseline-project/releases/latest">
        <img src="https://img.shields.io/github/v/release/GreyTeamToolbox/baseline-project?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-project/releases/latest">
        <img src="https://img.shields.io/github/release-date/GreyTeamToolbox/baseline-project?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-project/releases/latest">
        <img src="https://img.shields.io/github/commits-since/GreyTeamToolbox/baseline-project/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/baseline-project/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-project/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-project/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-project/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This is the baseline project template that we use internally when creating new python tools for the [Blue Team Toolbox](https://github.com/BlueTeamToolbox)
and [Red Team Toolbox](https://github.com/RedTeamToolbox). 

It includes features such as argument parsing, configuration management, and a modular structure to facilitate scalable and maintainable code development.

We decided to make this available along with our other tools to allow people to use a well engineered starting point when creating their own tools.

We also have a [baseline package](https://github.com/GreyTeamToolbox/baseline-package) which can be used to create python packages. It comes with
all the same base functionality but also has all of the basic functionality and workflows needed to create, build and publish new package to [PyPI](https://pypi.org/).

## Features

- **Modular Architecture**: Organize your code into modules for better maintainability.
- **Argument Parsing**: Easily handle command-line arguments using `argparse`.
- **Configuration Management**: Generate configuration objects from command-line arguments.
- **Custom Exceptions**: Implement custom exceptions for specific error handling.

## Installation

To install the Baseline Project, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/GreyTeamToolbox/baseline-project.git
cd baseline-project
```

It is recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment using the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the Baseline Project, execute the `run` function from the main script:

```bash
python main.py --required <value>
```

### Command-Line Arguments

The application supports several command-line arguments:

- `-h, --help`: Show help message and exit.
- `-d, --debug`: Enable debug mode for verbose output.
- `-v, --verbose`: Enable verbose output to show scan results as they come in.
- `-V, --version`: Show the program's version number and exit.
- `-i, --optional-integer`: An optional integer argument (default: 2).
- `-s, --optional-string`: An optional string argument (default: "me").
- `-r, --required`: A required string argument.

Example usage:

```bash
python main.py -r "required_value" -i 10 -s "optional_string"
```

## Project Structure

The project is organized as follows:

```
baseline-project/
├── modules/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── exceptions.py
│   └── globals.py
├── main.py
├── requirements.txt
└── README.md
```

- `modules/`: Contains the core modules of the application.
  - `cli.py`: Handles the command-line arguments and main program flow.
  - `config.py`: Handles configuration creation from command-line arguments.
  - `exceptions.py`: Handles custom exceptions.
  - `globals.py`: Defines global constants used across the application.
- `main.py`: The main script that orchestrates argument parsing and program execution.
- `requirements.txt`: Lists the dependencies required for the project.
- `README.md`: The file you are currently reading.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
