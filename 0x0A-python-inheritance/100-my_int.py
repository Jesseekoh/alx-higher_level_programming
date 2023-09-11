#!/usr/bin/python3
"""100-my_int module
"""


class MyInt(int):
    """Defines the MyInt class."""

    def __eq__(self, other):
        """Sets the == behaviour."""
        return int(self) != other

    def __ne__(self, other):
        """Sets the != behaviour."""
        return int(self) == other
