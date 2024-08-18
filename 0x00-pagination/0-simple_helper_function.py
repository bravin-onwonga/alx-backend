#!/usr/bin/env python3
"""
Contains a function that determines the range
of indexes returned within particular pagination parameters
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Determines the number of index within a pagination parameters
    Parames:
        page - page
        page_size - number of indexes to contain per page
    Return:
        tuple of size 2 with the start and end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return(start, end)
