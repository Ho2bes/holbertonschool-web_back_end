#!/usr/bin/env python3

"""Async comprehension module for Python async comprehension exercise"""

import typing
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> typing.List[float]:
    """Collect 10 random numbers using async comprehensin gasync_generator"""
    random_numbers = [number async for number in async_generator()]
    return [number async for number in async_generator()]
