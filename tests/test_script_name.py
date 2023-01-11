# -*- coding: utf-8 -*-

"""This is the main test script.

This script is handles all of the testing for the functionality supplied
by the modules used in the tool.

There will not be 100% code coverage.
"""

from argparse import _StoreTrueAction, ArgumentParser, Namespace
from typing import Any

import sys

from unittest.mock import patch

from _pytest.logging import LogCaptureFixture

from modules.cli import _add_flags_to_parser, _add_optional_parameters, _add_required_parameters, _setup_arg_parser, process_command_line_arguments
from modules.config import create_configuration_from_arguments
from modules.constants import ERROR, INFO, SUCCESS, SYSTEM, WARN, RESET
from modules.exceptions import CustomException, InvalidParameters
from modules.globals import global_configuration
from modules.notify import error, error_msg, info, info_msg, success, success_msg, system, system_msg, warn, warn_msg


def output_errors(errors: list) -> str:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    Arguments:
        errors (list) -- _description_
    Keyword Arguments:
        header (str) -- _description_ (default: "Errors occurred:")
    Returns:
        str -- _description_
    """
    error_string: str = "\n"
    for err in errors:
        error_string += f"{err}\n"
    return error_string


def test_notify(capsys: LogCaptureFixture) -> None:
    """Test all of the notification functions.

    Test all screen based notifications, ensuring correct handling for coloured output.

    Arguments:
        capfd (LogCaptureFixture) -- Builtin fixture for accessing stdout/stderr output.
    """
    test_cases: dict = {
        success: SUCCESS,
        warn: WARN,
        error: ERROR,
        info: INFO,
        system: SYSTEM,
    }
    errors: list = []
    count: int = 0
    clean_string: str = "hello world"
    result_string: str = ''

    for test_function, color_code in test_cases.items():
        count += 1
        test_string: str = f"{color_code}{clean_string}{RESET}"
        test_function(clean_string)
        captured: Any = capsys.readouterr()
        result_string = captured.out.strip()

        if test_string != result_string:
            errors.append(f"Test {count} failed: {test_string} vs {result_string}")

    assert not errors, output_errors(errors)  # nosec: assert_used


def test_notify_messages() -> None:
    """Test all of the notification message creation functions.

    Test all of the functions that generate notification messages and return them as a string,
    ensuring correct handling for coloured output.
    """
    test_cases: dict = {
        success_msg: SUCCESS,
        warn_msg: WARN,
        error_msg: ERROR,
        info_msg: INFO,
        system_msg: SYSTEM,
    }
    errors: list = []
    count: int = 0
    clean_string: str = "hello world"
    result_string: str = ''

    for test_function, color_code in test_cases.items():
        count += 1
        test_string: str = f"{color_code}{clean_string}{RESET}"
        result_string = test_function(clean_string)

        if test_string != result_string:
            errors.append(f"Test {count} failed: {test_string} vs {result_string}")

    assert not errors, output_errors(errors)  # nosec: assert_used


def test_setup_arg_parser() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    assert isinstance(_setup_arg_parser(), ArgumentParser)  # nosec: assert_used


def test_process_command_line_arguments() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    testargs: list[str] = ["prog", "-r", "required parameter"]
    with patch.object(sys, 'argv', testargs):
        assert isinstance(process_command_line_arguments(), Namespace)  # nosec: assert_used


def test_add_flags_to_parser_help_flag() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    parser: ArgumentParser = ArgumentParser(add_help=False)
    _add_flags_to_parser(parser)

    # pylint: disable=protected-access
    assert "-h" in parser._option_string_actions  # nosec: assert_used

    assert parser._option_string_actions["-h"].dest == "help"  # nosec: assert_used
    # pylint: enable=protected-access


def test_add_flags_to_parser_debug_flag() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    errors: list = []
    parser: ArgumentParser = ArgumentParser(add_help=False)
    _add_flags_to_parser(parser)

    # pylint: disable=protected-access
    if "-d" not in parser._option_string_actions:
        errors.append("-d option doesn't exist")

    if "--debug" not in parser._option_string_actions:
        errors.append("--debug option doesn't exist")

    if not isinstance(parser._option_string_actions["-d"], _StoreTrueAction):
        errors.append("Does not use store_true")

    if parser._option_string_actions["-d"].dest != "debug":
        errors.append("Debug destination incorrectly set")

    if parser._option_string_actions["-d"].default is not False:
        errors.append("Default value not set to False")
    # pylint: enable=protected-access

    assert not errors, output_errors(errors)  # nosec: assert_used


def test_add_flags_to_parser_verbose_flag() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    errors: list = []
    parser: ArgumentParser = ArgumentParser(add_help=False)
    _add_flags_to_parser(parser)

    # pylint: disable=protected-access
    if "-v" not in parser._option_string_actions:
        errors.append("-v option doesn't exist")

    if "--verbose" not in parser._option_string_actions:
        errors.append("--verbose option doesn't exist")

    if not isinstance(parser._option_string_actions["-v"], _StoreTrueAction):
        errors.append("Does not not use store_true")

    if parser._option_string_actions["-v"].dest != "verbose":
        errors.append("Destination incorrectly set")

    if parser._option_string_actions["-v"].default is not False:
        errors.append("Default value not set to False")
    # pylint: enable=protected-access

    assert not errors, output_errors(errors)  # nosec: assert_used


def test_add_required_flags_to_parser() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    errors: list = []
    parser: ArgumentParser = ArgumentParser(add_help=False)
    _add_required_parameters(parser)

    # pylint: disable=protected-access
    if "-r" not in parser._option_string_actions:
        errors.append("-r option doesn't exist")

    if "--required" not in parser._option_string_actions:
        errors.append("--required option doesn't exist")

    if parser._option_string_actions["-r"].dest != "required":
        errors.append("Destination incorrectly set")

    if parser._option_string_actions["-r"].required is not True:
        errors.append("Required not set to true")
    # pylint: enable=protected-access

    assert not errors, output_errors(errors)  # nosec: assert_used


def test_add_optional_flags_to_parser() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    errors: list = []
    parser: ArgumentParser = ArgumentParser()
    _add_optional_parameters(parser)

    # pylint: disable=protected-access
    if "-o" not in parser._option_string_actions:
        errors.append("Verbose: -v options doesn't exist")

    if "--optional" not in parser._option_string_actions:
        errors.append("Verbose: -v options doesn't exist")

    if parser._option_string_actions["-o"].dest != "optional":
        errors.append("Verbose destination incorrectly set")

    if parser._option_string_actions["-o"].required is True:
        errors.append(f"Should not be set to required=True ({parser._option_string_actions['-o'].required})")

    if parser._option_string_actions["-o"].type != int:
        errors.append("Incorrect type set")

    if parser._option_string_actions["-o"].default == "2":
        errors.append("Incorrect default value set")
    # pylint: enable=protected-access

    assert not errors, output_errors(errors)  # nosec: assert_used


def test_create_configuration_from_arguments_verbose() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    args: Namespace = Namespace(verbose=True, debug=False, required=None, optional=None)
    create_configuration_from_arguments(args)
    assert global_configuration.verbose is True  # nosec: assert_used


def test_create_configuration_from_arguments_debug() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    args: Namespace = Namespace(verbose=False, debug=True, required=None, optional=None)
    create_configuration_from_arguments(args)
    assert global_configuration.debug is True  # nosec: assert_used


def test_create_configuration_from_arguments_required() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    args: Namespace = Namespace(verbose=False, debug=False, required="value", optional=None)
    create_configuration_from_arguments(args)
    assert global_configuration.required == "value"  # nosec: assert_used


def test_create_configuration_from_arguments_optional() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    args: Namespace = Namespace(verbose=False, debug=False, required=None, optional="value")
    create_configuration_from_arguments(args)
    assert global_configuration.optional == "value"  # nosec: assert_used


def test_custom_exception() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Raises:
        CustomException: _description_
    """
    assertion: bool = False
    try:
        raise CustomException()
    except CustomException:
        assertion = True

    assert assertion  # nosec: assert_used


def test_invalid_parameters_exception() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Raises:
        InvalidParameters: _description_
    """
    assertion: bool = False
    try:
        raise InvalidParameters()
    except InvalidParameters:
        assertion = True

    assert assertion  # nosec: assert_used


def test_invalid_parameters_exception_inheritance() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.
    """
    assert issubclass(InvalidParameters, CustomException)  # nosec: assert_used


def test_custom_exception_with_message() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Raises:
        CustomException: _description_
    """
    assertion: bool = False
    test_message: str = "test message"
    try:
        raise CustomException(test_message)
    except CustomException as err:
        assertion = True
        assert str(err) == test_message  # nosec: assert_used
    assert assertion  # nosec: assert_used


def test_invalid_parameters_exception_with_message() -> None:
    """Define a summary.

    This is the extended summary from the template and needs to be replaced.

    Raises:
        InvalidParameters: _description_
    """
    assertion: bool = False
    test_message: str = "test message"
    try:
        raise InvalidParameters(test_message)
    except InvalidParameters as err:
        assertion = True
        assert str(err) == test_message  # nosec: assert_used
    assert assertion  # nosec: assert_used
