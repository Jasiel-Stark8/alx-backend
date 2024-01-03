#!/usr/bin/env python3
"""Helper function"""


def index_range(page, page_size):
    """
    Calculate the start and end index for the items on a specific page.

    Arguments:
    page -- The current page number (1-indexed).
    page_size -- The number of items on each page.

    Returns:
    A tuple containing the start and end index for the items on the specified page.
    """
    # Calculate the start index
    start_index = (page - 1) * page_size
    # Calculate the end index
    end_index = page * page_size

    return (start_index, end_index)
