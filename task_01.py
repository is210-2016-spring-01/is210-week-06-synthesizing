#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Module"""


def get_party_stats(families, table_size=6):
    """Defines a function that generates a headcount and table count

    Args:
        families (list): a list of families, which are lists of
        family members
        table_size (int): the max number of seats per table with
        a default of 6

    Returns:
        tuple: total number of guests, total number of tables

    Examples:
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
        'Janis']], 2)
        (6, 4)
        """

    tablecount = 0
    headcount = 0

    for members in families:
        tablecount += -(-len(members) // table_size)
        headcount += len(members)
    return (headcount, tablecount)
