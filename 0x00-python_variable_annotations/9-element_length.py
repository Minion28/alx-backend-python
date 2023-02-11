#!/usr/bin/env python3
"""
    annotate function parameters
"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
        return variables with appropriate types
    """

    return [(i, len(i)) for i in lst]
