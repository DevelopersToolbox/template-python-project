# -*- coding: utf-8 -*-
"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""
from argparse import _ArgumentGroup, ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace

from .constants import ARG_PARSER_DESCRIPTION, ARG_PARSER_EPILOG


def _add_flags_to_parser(parser: ArgumentParser) -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        parser (ArgumentParser) -- _description_
    """
    flags: _ArgumentGroup = parser.add_argument_group(
        title="optional flags",
        description="Description"
    )
    flags.add_argument(
        "-h",
        "--help",
        action="help",
        help="show this help message and exit"
    )
    flags.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False,
        help="Very noisy"
    )
    flags.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Verbose output - show scan results as they come in"
    )


def _add_required_parameters(parser: ArgumentParser) -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        parser (ArgumentParser) -- _description_
    """
    required: _ArgumentGroup = parser.add_argument_group(
        title="required arguments",
        description="stuff"
    )
    required.add_argument(
        "-r",
        "--required",
        type=str,
        required=True,
        help="A required parameter"
    )


def _add_optional_parameters(parser: ArgumentParser) -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Arguments:
        parser (ArgumentParser) -- _description_

    Returns:
        _type_ -- _description_
    """
    optional: _ArgumentGroup = parser.add_argument_group(
        title="optional arguments",
        description="stuff"
    )
    optional.add_argument(
        "-i",
        "--optional-integer",
        type=int,
        default=2,
        help="An optional integer"
    )

    optional.add_argument(
        "-s",
        "--optional-string",
        type=str,
        default="me",
        help="An optional string"
    )


def _setup_arg_parser() -> ArgumentParser:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Returns:
        ArgumentParser -- _description_
    """
    parser: ArgumentParser = ArgumentParser(
        add_help=False,
        formatter_class=ArgumentDefaultsHelpFormatter,
        description=ARG_PARSER_DESCRIPTION,
        epilog=ARG_PARSER_EPILOG,
    )
    _add_flags_to_parser(parser)
    _add_required_parameters(parser)
    _add_optional_parameters(parser)

    return parser


def process_command_line_arguments() -> Namespace:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Returns:
        Namespace -- _description_
    """
    parser: ArgumentParser = _setup_arg_parser()
    args: Namespace = parser.parse_args()

    return args
