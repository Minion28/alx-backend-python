#!/usr/bin/env python3
"""
    function sum_mixed_list taking a list mxd_lst
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        return sum of list as a float
    """

    output: float = 0

    for x in mxd_lst:
        output += x

    return output
