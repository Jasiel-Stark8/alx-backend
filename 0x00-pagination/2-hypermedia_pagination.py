#!/usr/bin/env python3
"""Helper function"""
import csv
import math
from typing import List
import math


def index_range(page, page_size):
    """
        Calculate the start and end index for the items on a specific page.

        Arguments:
        page -- The current page number (1-indexed).
        page_size -- The number of items on each page.

        Returns:
        A tuple containing the start and end index for the
        items on the specified page.
    """

    # Calculating start index
    start_idx = (page - 1) * page_size
    # Calculating end index
    end_idx = page * page_size

    return (start_idx, end_idx)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Find the correct indexes to paginate the dataset  \
            and return the appropriate page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Return empty list if start index is out of range
        if start_index > len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary with pagination metadata."""
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        results = self.get_page(page, page_size)

        # Calculating next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(results),
            'page': page,
            'data': results,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
