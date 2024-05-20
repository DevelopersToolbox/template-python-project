"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""
import argparse

from modules.globals import ARG_PARSER_DESCRIPTION, ARG_PARSER_EPILOG, ARG_PARSER_PROG_NAME, VERSION_STRING


def setup_arg_parser() -> argparse.ArgumentParser:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Returns:
        ArgumentParser -- _description_
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
    Process the command line arguments.

    Setup the arguments parser, parser the arguments, validate the input and then action the requested changed.
    """
    args: argparse.Namespace = parser.parse_args()

    return args


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
