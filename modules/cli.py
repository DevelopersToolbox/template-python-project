"""
This module provides a command-line interface for a specific application.

The module defines the argument parser, processes the command-line arguments,
and executes the main functionality of the program based on those arguments.

Functions:
    setup_arg_parser: Configures the argument parser with flags, optional, and required arguments.
    process_arguments: Processes and validates the command-line arguments.
    run: The main function that orchestrates the argument parsing and program execution.
"""

import argparse
import sys

from types import SimpleNamespace

from modules.config import create_configuration_from_arguments
from modules.globals import ARG_PARSER_DESCRIPTION, ARG_PARSER_EPILOG, ARG_PARSER_PROG_NAME, VERSION_STRING


def setup_arg_parser() -> argparse.ArgumentParser:
    """
    Configure the argument parser with flags, optional, and required arguments.

    This function sets up the argument parser with various groups of arguments:
    flags, optional arguments, and required arguments. Each group is configured
    with relevant command-line options.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(prog=ARG_PARSER_PROG_NAME,
                                     add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=ARG_PARSER_DESCRIPTION,
                                     epilog=ARG_PARSER_EPILOG)

    flags: argparse._ArgumentGroup = parser.add_argument_group(title='flags')
    optional: argparse._ArgumentGroup = parser.add_argument_group(title='optional')
    required: argparse._ArgumentGroup = parser.add_argument_group(title='required')

    flags.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="show this help message and exit")
    flags.add_argument("-d", "--debug", action="store_true", default=False, help="Very noisy")
    flags.add_argument("-v", "--verbose", action="store_true", default=False, help="Verbose output - show scan results as they come in")
    flags.add_argument('-V', '--version', action='version', version=VERSION_STRING, help="Show program's version number and exit.")

    optional.add_argument("-i", "--optional-integer", type=int, default=2, help="An optional integer")
    optional.add_argument("-s", "--optional-string", type=str, default="me", help="An optional string")

    required.add_argument("-r", "--required", type=str, required=True, help="A required parameter")

    return parser


def process_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    Process and validate the command line arguments.

    This function parses the command-line arguments using the provided argument
    parser and returns a namespace object containing the parsed arguments.

    Args:
        parser (argparse.ArgumentParser): The argument parser configured with the necessary arguments.

    Returns:
        argparse.Namespace: The namespace object containing the parsed arguments.
    """
    args: argparse.Namespace = parser.parse_args()

    return args


def run() -> None:
    """
    Master controller function.

    This function sets up the argument parser, processes the command-line arguments,
    validates the input, and performs the main program logic based on the arguments.

    Raises:
        SystemExit: If there is an error in argument parsing or validation.
    """
    parser: argparse.ArgumentParser = setup_arg_parser()
    try:
        args: argparse.Namespace = process_arguments(parser)
        config: SimpleNamespace = create_configuration_from_arguments(args)
        print(f"Args: {args}")
        print(f"Config: {config}")
    except argparse.ArgumentTypeError as err:
        parser.print_usage()
        print(err)
        sys.exit(1)
