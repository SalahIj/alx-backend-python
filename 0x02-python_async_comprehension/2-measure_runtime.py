#!/usr/bin/env python3
""" The imported modules """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The function definition
    Args:
        No args
    """
    sect = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    Bilan = time.perf_counter() - sect
    return Bilan
