#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 6 synthesizing task with a party function"""


def get_party_stats(families, table_size=6):
    """Processes a list of "families" and returns the total attendies and the
       number of tables required to seat all families without sharing a table.

    Args:
        families (list): list of a list of family member names
        table size (int, optional): maximum number of people to be seated at
                                    each table

    Returns:
        tuple: contains the total number of guests and the number of tables
               needed.

    Examples:
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']],
        2)
        (6, 4)
    """

    total_people, tables_needed = 0, 0    # initialize counters

    for group in families:

        fsize = len(group)                # get number of peple in the group
        total_people += fsize             # add group to total people count
        tables_needed += -(-fsize // table_size)  # add number of tables

    return (total_people, tables_needed)
