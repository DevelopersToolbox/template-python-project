"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

import argparse
import sys

from types import SimpleNamespace

from modules.cli import setup_arg_parser, process_arguments
from modules.config import create_configuration_from_arguments


def run() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        message (str) -- _description_
    """
    parser: argparse.ArgumentParser = setup_arg_parser()
    try:
        args: argparse.Namespace = process_arguments(parser)
    except argparse.ArgumentTypeError as err:
        parser.print_usage()
        print(err)
        sys.exit(1)
    else:
        config: SimpleNamespace = create_configuration_from_arguments(args)
        print(f"Args: {args}")
        print(f"Config: {config}")
