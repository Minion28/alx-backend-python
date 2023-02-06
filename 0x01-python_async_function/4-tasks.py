#!/usr/bin/env python3
"""
alter function wait_n to task_wait_n
"""
import asyncio
from typing import List

get = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    call task_wait_n
    """
    ls = [get(max_delay) for i in range(n)]
    stop = [await task for task in asyncio.as_completed(ls)]

    return stop
