#!/usr/bin/env python3
"""Simple helper function module for Python async comprehension exercise"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)


def get_page(page: int = 1, page_size = 10) -> tuple:
    """Return a tuple of the list of items and the range of the page"""
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0
    start, end = index_range(page, page_size)
    return (list(range(start, end)), (start, end))
