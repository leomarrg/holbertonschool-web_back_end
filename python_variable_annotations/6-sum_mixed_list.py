#!/usr/bin/env python3
"""Sums a list of integers and floats as floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sums of ints and floats"""
    return sum(mxd_lst)
