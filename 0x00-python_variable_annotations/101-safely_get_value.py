#!/usr/bin/env python3
"""
Imported modules
"""
from typing import Sequence, Union, Any, TypeVar, Mapping

R = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[R, None] = None) -> Union[Any, R]:
    """
    Function definition
    Args:
        dct: the first input
        key: the second input
        default: the third input
    """
    if key in dct:
        return dct[key]
    else:
        return default
