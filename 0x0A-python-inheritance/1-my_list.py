#!/usr/bin/python3
"""Define an inherited list class MyList."""

class MyList(list):
    """Type class MyList with print_sorted function"""

    def print_sorted(self):
	"""Print a list in sorted ascending order."""
        print(sorted(self))
