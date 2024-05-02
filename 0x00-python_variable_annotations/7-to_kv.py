#!/usr/bin/env python3
"""
Imported modules
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function definition
    Args:
        k: the first input
        v: the second input
    """
    return (k, v**2)
