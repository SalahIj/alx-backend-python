#!/usr/bin/env python3
""" Imported modules """
import asyncio
from typing import List, Union, Awaitable

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ The function definition
    Args:
        n: the first input
        max_delay: the second input
    """
    delaits: List[Awaitable[float]] = []
    delaitsList: List[float] = []

    for i in range(n):
        delaits.append(wait_random(max_delay))

    for o in asyncio.as_completed(delaits):
        result: float = await o
        delaitsList.append(result)

    return delaitsList
