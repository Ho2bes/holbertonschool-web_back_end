#!/usr/bin/env python3
"""Measure runtime module for Python async comprehension exercise"""


import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension called 4 times in parallel"""
    start_time = asyncio.get_event_loop().time()  # Mesure the start time
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = asyncio.get_event_loop().time()  # Mesure the end time
    return end_time - start_time  # Return the total runtime
