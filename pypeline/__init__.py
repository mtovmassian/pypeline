#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Pypeline Library: Unix pipes with Python
    ========================================
    Pypeline is a lightweight Python library built with coroutines that allows
    you to chain processes like Unix pipes.

    Usage:
    ------
    Example: Create a pipeline to apply these three string transformations:
    - consonants are in uppercase
    - letters are spaced
    - letters order is reversed
    >>> import pypeline
    >>>
    >>> def to_upppercase_consonants(data):
    ...     vowels = ["a", "e", "i", "o", "u", "y"]
    ...     return "".join(map(lambda x: x.upper() if x not in vowels else x, data))
    ...
    >>> to_spaced(data):
    ...     space = "  "
    ...     return "".join(map(lambda x: x + "  ", data))[:-(len(space))]
    >>>
    >>> def to_reversed(data):
    ...     return data[::-1]
    ...
    >>> pipeline, sink = pypeline.create(
    ...     [to_upppercase_consonants, to_spaced, to_reversed]
    ... )
    >>> pipeline.send("pimp my pipe with pypeline")
    >>>
    >>> print(sink())
    ['e  N  i  L  e  P  y  P     H  T  i  W     e  P  i  P     y  M     P  M  i  P']
    >>>
    >>> pipeline.send("harry tuttle approves pypeline")
    >>>
    >>> print(sink())
    ['e  N  i  L  e  P  y  P     H  T  i  W     e  P  i  P     y  M     P  M  i  P',
    'e  N  i  L  e  P  y  P     S  e  V  o  R  P  P  a     e  L  T  T  u  T     y  R  R  a  H']
"""

__version__ = "0.0.1"

from .pypeline import create

__all__ = ["create"]
