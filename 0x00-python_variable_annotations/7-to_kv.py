#!/usr/bin/env python3
"""
    function to_kv that takes a string and and int as arguments
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        return a tuple
    """

    tup: Tuple(str, Union[int, float])
    tup = (k, v**2)

    return tup
