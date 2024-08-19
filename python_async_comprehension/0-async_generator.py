#!/usr/bin/env python3

"""Async generator module for Python async comprehension exercise"""

import asyncio
import random

async def async_generator():
    """Async generator that yields 10 random numbers between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)  # Wait 1 second
        yield random.uniform(0, 10)  # Produce a random float between 0 and 10
