#!/usr/bin/env python3
"""
write an async routine that takes 2 int arguments
"""
import asyncio
from typing import List
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine
    """
    ls = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    end = [await task for task in asyncio.as_completed(ls)]

    return end
