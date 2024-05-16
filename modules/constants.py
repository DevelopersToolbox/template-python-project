"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

import colorama

colorama.init()

SUCCESS: str = colorama.Fore.GREEN
WARN: str = colorama.Fore.YELLOW
ERROR: str = colorama.Fore.RED
INFO: str = colorama.Fore.CYAN
BOLD: str = colorama.Style.BRIGHT
SYSTEM: str = colorama.Fore.LIGHTBLACK_EX
RESET: str = colorama.Style.RESET_ALL
