#!/usr/bin/env python3
"""A Type-annotated function sum_list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum as a float"""
    return (float(sum(input_list)))
