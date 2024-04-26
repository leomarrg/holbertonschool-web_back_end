#!/usr/bin/env python3
"""Takes a string, int or float and returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple, first item string, second element a square"""
    return (k, v * v)
