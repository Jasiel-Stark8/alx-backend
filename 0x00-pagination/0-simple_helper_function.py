#!/usr/bin/env python3
"""Helper function"""

def index_range(page, page_size):
    """Funciton"""
    start_idx = page
    end_idx = range(start_idx, page_size)
    return [end_idx, start_idx]
