#!/usr/bin/env python3
""" Imported modules """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function definition
    Args:
        multiplier: the input of the function
    """
    return lambda mult: mult * multiplier
