#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""
import sys

from argparse import Namespace

from modules.cli import process_command_line_arguments
from modules.config import create_configuration_from_arguments
from modules.exceptions import InvalidParameters
from modules.notify import error, system


def main() -> None:
    """Control the main flow of the program.

    It does stuff.
    """
    args: Namespace = process_command_line_arguments()
    create_configuration_from_arguments(args)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        system("\n[*] Exiting Program\n")
    except InvalidParameters as e:
        error(str(e))
