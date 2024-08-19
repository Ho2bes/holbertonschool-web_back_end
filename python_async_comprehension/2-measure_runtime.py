#!/usr/bin/env python3

"""Measure runtime module for Python async comprehension exercise"""

import asyncio
import time
from .async_comprehension import async_comprehension  # import async_comprehension from the previous task

async def measure_runtime():
    """Measure the runtime of async_comprehension called 4 times in parallel"""
    start_time = time.perf_counter()  # mesure the start time
    await asyncio.gather(  # execute async_comprehension 4 times
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()  # Mesure the end time
    return end_time - start_time  # Return the total time taken to execute the 4 async_comprehension calls
