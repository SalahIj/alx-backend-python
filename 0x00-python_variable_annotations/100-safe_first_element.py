#!/usr/bin/env python3
"""
Imported modules
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function definition
    Args:
        lst: the input of the function
    """
    if lst:
        return lst[0]
    else:
        return None
