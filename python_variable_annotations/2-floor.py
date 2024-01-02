#!/usr/bin/env python3
"""type-annotated function floor which takes a float
n as argument and returns the floor of the float."""


def floor(n: float) -> int:
    """floor function"""
    if (n > 0 and isinstance(n, int)):
        return n
    elif (n > 0 and isinstance(n, float)):
        return int(n)
    elif (n < 0 and isinstance(n, int)):
        return n
    elif (n < 0 and isinstance(n, float)):
        return int(n) - 1
