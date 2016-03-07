#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a module"""


def get_party_stats(families, table_size=6):
    """This function returns the total number of guests and total number of
    people

    Args:
        families (list): Uses a list to count the number of guests,
        table_size(int): Number of tables for each family. Default value = 6

    Returns:
        int: Gives the total number guests and the total number of tables

    Example:

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
            (6, 3)
    """

    total_guests = 0
    total_tables = 0

    for guests in families:
        total_tables += -(-len(guests)//table_size)
        total_guests += len(guests)
        total = (total_guests, total_tables)
    return total
