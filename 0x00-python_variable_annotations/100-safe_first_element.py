#!/usr/bin/env python3
"""safe first element function
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return first element for list"""
    if lst:
        return lst[0]
    else:
        return None
