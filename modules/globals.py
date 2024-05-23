"""
This module defines global constants used across the application.

The module provides several constants including version information, program name,
description, and epilog for the argument parser.

Constants:
    VERSION: The current version of the application.
    ARG_PARSER_PROG_NAME: The name of the program used in the argument parser.
    ARG_PARSER_DESCRIPTION: The description of the program used in the argument parser.
    ARG_PARSER_EPILOG: The epilog text used in the argument parser.
    VERSION_STRING: A formatted string that includes the current version and program name.
"""

VERSION: str = '0.0.1'

ARG_PARSER_PROG_NAME: str = "baseline-project"
ARG_PARSER_DESCRIPTION: str = "A description goes here"
ARG_PARSER_EPILOG: str = "The Epilog goes here"

VERSION_STRING: str = "Current version of " + ARG_PARSER_PROG_NAME + " is v" + VERSION
