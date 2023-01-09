# -*- coding: utf-8 -*-
"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""
from argparse import Namespace

from .globals import global_configuration


def create_configuration_from_arguments(args: Namespace) -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        args (argparse.Namespace) -- _description_
    """
    global_configuration.verbose = args.verbose
    global_configuration.debug = args.debug
    global_configuration.required = args.required
    global_configuration.optional = args.optional
