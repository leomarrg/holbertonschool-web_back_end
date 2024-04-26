#!/usr/bin/env python3
"""takes a float multiplier and returns a function
    that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(x: float) -> float:
        return x * multiplier
    """returns the multiplication of the input
    and the function"""
    return multiplier_func
