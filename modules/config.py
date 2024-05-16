"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""
from argparse import Namespace

from types import SimpleNamespace


def create_configuration_from_arguments(args: Namespace) -> SimpleNamespace:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        args (argparse.Namespace) -- _description_
    """
    config: SimpleNamespace = SimpleNamespace()

    config.verbose = args.verbose
    config.debug = args.debug
    config.required = args.required
    config.optional_integer = args.optional_integer
    config.optional_string = args.optional_string

    return config
