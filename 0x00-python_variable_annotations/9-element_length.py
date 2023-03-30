#!/usr/bin/env python3
"""element length function
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Compute the length of a list"""
    return [(i, len(i)) for i in lst]
