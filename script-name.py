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

from modules.exceptions import InvalidParameters
from modules.main import run
from modules.notify import error, system


def main() -> None:
    """Control the main flow of the program.

    It does stuff.
    """
    run()
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        system("\n[*] Exiting Program\n")
    except InvalidParameters as e:
        error(str(e))
