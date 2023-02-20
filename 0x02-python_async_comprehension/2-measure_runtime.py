#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute async comprehension 4 times
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time


async def measure_runtime() -> float:
    """
    measure total runtime and return it
    """
    begin = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end = time.perf_counter()
    return (end - begin)
