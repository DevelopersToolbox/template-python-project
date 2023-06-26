# -*- coding: utf-8 -*-

"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

from argparse import Namespace

from modules.cli import process_command_line_arguments
from modules.config import create_configuration_from_arguments

def run() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        message (str) -- _description_
    """
    args: Namespace = process_command_line_arguments()
    print(args)
    create_configuration_from_arguments(args)
