#!/usr/bin/env python3
"""function returns appropiates types of parameters"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns types"""
    return [(i, len(i)) for i in lst]
