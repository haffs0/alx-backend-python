#!/usr/bin/env python3
"""safely get value function
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
Ret = Union[Any, T]
Default = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Default = None) -> Ret:
    """return first element for dict"""
    if key in dict:
        return dict[key]
    else:
        return default
