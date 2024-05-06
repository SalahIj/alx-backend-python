#!/usr/bin/env python3
""" Imported modules """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ The function definition
    Args:
        n: the first input
        max_delay: the second input
    """
    start_timing: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_timing: float = time.perf_counter()
    return (end_timing - start_timing) / n
