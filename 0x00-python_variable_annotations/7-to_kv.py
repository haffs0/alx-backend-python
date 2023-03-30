#!/usr/bin/env python3
"""A Type-annotated function to_kv.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple"""
    return (k, float(v**2))
