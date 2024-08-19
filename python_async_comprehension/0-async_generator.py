#!/usr/bin/env python3
"""coroutine will collect 10 random numbusing async comprehensing """

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Async generator that yields 10 random numbers between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)  # Wait 1 second
        yield random.uniform(0, 10)  # Produce a random float between 0 and 10
