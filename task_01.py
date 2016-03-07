#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Organizing parties today!"""


def get_party_stats(families, table_size=6):
    """How many tables, how many people?

    Returns a tuple of how many guests are coming to the party
    and how many tables will be required to seat them.

    Args:
        families (list): list of families and their members
        table_size (int): maximum number of guests per table, default is 6

    Returns:
        Tuple of how many guests are there, how many tables required.

    Examples:

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']], 2)
        (6, 4)
    """

    guests = 0
    tables = 0
    
    for family in families:
        guests += len(family) #how many guests
        tables  += -(-len(family)//table_size)
    return guests, tables

