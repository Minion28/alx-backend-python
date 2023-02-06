#!/usr/bin/env python3
"""
create a function and arguments that measure the total
execution time and return a float
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function measure_time
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()
    total_time = stop - start

    return total_time / n
