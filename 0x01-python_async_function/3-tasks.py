#!/usr/bin/env python3
""" Imported modules """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ The function definition
    Args:
        max_delay: the input of the function
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
