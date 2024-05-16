# -*- coding: utf-8 -*-

"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

from .constants import BOLD, ERROR, INFO, RESET, SUCCESS, SYSTEM, WARN


def success(message: str) -> None:
    """
    Display a success messages to the user.

    Arguments:
        message (str): The message to display.
    """
    print(f'[ {BOLD}{SUCCESS}Success{RESET} ] {message}')


def warn(message: str) -> None:
    """
    Display a warning messages to the user.

    Arguments:
        message (str): The message to display.
    """
    print(f'[ {BOLD}{WARN}Warning{RESET} ] {message}')


def error(message: str) -> None:
    """
    Display an error messages to the user.

    Arguments:
        message (str): The message to display.
    """
    print(f'[ {BOLD}{ERROR}Error{RESET} ] {message}')


def info(message: str) -> None:
    """
    Display an informational messages to the user.

    Arguments:
        message (str): The message to display.
    """
    print(f'[ {BOLD}{INFO}Info{RESET} ] {message}')


def system(message: str) -> None:
    """
    Display a system messages to the user.

    Arguments:
        message (str): The message to display.
    """
    print(f'{BOLD}{SYSTEM}{message}{RESET}')
