#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module to determine table seating."""


def get_party_stats(families, table_size=6):
    """Function to distribute guests.

    Args:
        families (list): Lists of families.
        table_size (int): Number per table, defaults to 6 max.

    Returns:
        tuple: Total number of guests, total number of tables.

    Examples:
        >>> get_party_stats([['V', 'B', 'K', 'LA', 'Joe', 'M', 'Sx'],
            ['Sue']],5)
        (8, 3)

        get_party_stats([['Mike', 'Moe', 'Curly'], ['Be', 'Jay', 'Blue'],
        ['Jack', 'Diane']], 3)
        (8, 3)
    """
    count = 0
    tabnum = 0
    for members in families:
        tablect = -(-len(members) // table_size)
        tabnum += tablect
        for _ in members:
            count += 1
    return (count, tabnum)
