#!/usr/bin/env python3
""" async_generator coroutine yielding a random number between 0-10 """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loop 10 times each time asynchronously wait 1sec
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
