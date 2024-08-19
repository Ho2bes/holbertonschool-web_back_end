#!/usr/bin/env python3

"""Async comprehension module for Python async comprehension exercise"""

import asyncio
from .async_generator import async_generator  # Import async_generator from the previous task

async def async_comprehension():
    """Collect 10 random numbers using an async comprehensing over async_generator"""
    return [number async for number in async_generator()]
