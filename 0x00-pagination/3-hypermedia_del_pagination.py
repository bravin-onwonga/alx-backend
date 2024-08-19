#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Makes sure the user gets the correct amount of data in case
        a record is deleted
        Params:
            index: index to begin at
            page_size: size of data to serve
        Return:
            a dict
        """
        assert type(index) is int and index >= 0
        assert type(page_size) is int and page_size > 0

        indexed_dict = self.indexed_dataset()

        data = []

        count = 0

        for i in range(index, (index + page_size)):
            if indexed_dict.get(i):
                data.append(indexed_dict[i])
                count += 1

        if (count < page_size):
            while (count < page_size):
                i += 1
                if indexed_dict.get(i):
                    data.append(indexed_dict[i])
                    count += 1
                if (i >= len(indexed_dict)):
                    i = 0

        while (i >= 0):
            i += 1
            if indexed_dict.get(i):
                next_index = i
                break
            if (i >= len(indexed_dict)):
                i = 0

        dct = {}

        dct['index'] = index
        dct['data'] = data
        dct['page_size'] = page_size
        dct['next_index'] = next_index

        return dct
