#!/usr/bin/env python3
"""
    function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        return function that multiplies float
    """

    def x(f: float) -> float:
        """ multiply float by multiplier """
        return float(f * multiplier)

    return x
