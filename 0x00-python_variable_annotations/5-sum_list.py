#!/usr/bin/env python3
"""
    function sum_list which takes list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        return sum of lists as a float
    """

    output: float = 0

    for x in input_list:
        output += x

    return output
