"""
This module provides a function to create a configuration object from command-line arguments.

The module defines a function that takes parsed command-line arguments and
converts them into a configuration object using SimpleNamespace.

Functions:
    create_configuration_from_arguments: Converts command-line arguments into a configuration object.
"""

from argparse import Namespace
from types import SimpleNamespace


def create_configuration_from_arguments(args: Namespace) -> SimpleNamespace:
    """
    Convert command-line arguments into a configuration object.

    This function takes the parsed command-line arguments and creates a SimpleNamespace
    object containing the configuration settings derived from those arguments.

    Args:
        args (Namespace): The parsed command-line arguments.

    Returns:
        SimpleNamespace: A configuration object containing settings derived from the arguments.
    """
    config: SimpleNamespace = SimpleNamespace()

    config.verbose = args.verbose
    config.debug = args.debug
    config.required = args.required
    config.optional_integer = args.optional_integer
    config.optional_string = args.optional_string

    return config
