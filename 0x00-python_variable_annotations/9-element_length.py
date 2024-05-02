#!/usr/bin/env python3
"""
Imported modules
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function definition
    Args:
        lst: the input of the function
    """
    return [(i, len(i)) for i in lst]
