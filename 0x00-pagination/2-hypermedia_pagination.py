#!/usr/bin/env python3
"""
Gets page values based on pagination parameter
"""

import csv
import math
from typing import List, Tuple, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Instantiates an instance with this variable"""
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

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List]]:
        """Returns a dictionary representation of a hypermedia
        pagination"""
        import math

        dct = {}

        total_size = self.dataset()
        total_pages = math.ceil(len(total_size) // page_size)

        if page > total_pages:
            data = []
            prev_page = page - 1
            next_page = None
        else:
            data = self.get_page(page, page_size)
            if (self.get_page(page + 1, page_size)):
                next_page = page + 1
            else:
                next_page = None
            if page == 1:
                prev_page = None
            else:
                prev_page = page - 1
        page_size = len(data)

        dct = self.populate(dct, page_size, page, data,
                            next_page, prev_page, total_pages)

        return dct

    def populate(self, dct: dict, page_size: int, page: int, data: int,
                 next_page: int, prev_page: int,
                 total_pages: int) -> Dict[str, Union[int, List]]:
        """Populates the dict with hyper values"""
        dct['page_size'] = page_size
        dct['page'] = page
        dct['data'] = data
        dct['next_page'] = next_page
        dct['prev_page'] = prev_page
        dct['total_pages'] = total_pages

        return dct
