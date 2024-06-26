#!/usr/bin/env python3
"""async coroutine that takes an int as arg
    waits for random delay and returns it"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns int arg eventually"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
