#!/usr/bin/env python3
"""
Gets page values based on pagination parameter
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Creates a simple pagination in the form of a list
        based on the page number and size"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        idx_range = self.index_range(page, page_size)

        start = idx_range[0]
        end = idx_range[1]

        lst = self.dataset()

        len_lst = len(lst) - 1

        if (start < len_lst) and (end > len_lst):
            end = len_lst

        return lst[start: end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Determines the number of index within a pagination parameters
        Parames:
            page - page
            page_size - number of indexes to contain per page
        Return:
            tuple of size 2 with the start and end index
        """
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)
