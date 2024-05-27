"""
This module defines a custom exception class.

The module provides a custom exception class that can be used throughout the application
to handle specific error conditions.

Classes:
    CustomException: A custom exception class for application-specific errors.
"""


class CustomException(Exception):
    """
    A custom exception class for application-specific errors.

    This class is used to raise custom exceptions with a specific error message
    that can be handled separately from built-in exceptions.

    Args:
        Exception (BaseException): The base exception class that this class extends.
    """

    pass
