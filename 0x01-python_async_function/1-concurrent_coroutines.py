#!/usr/bin/env python3
""" Imported modules """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ The function definition """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
