#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculating family members and tables needed for a party."""


def get_party_stats(families, table_size=6):
    """Loop to count attendees and calculcate tables needed.

    Args:
        families (list): List of families which are lists of members.
        table_size (int): Number of seats at each table. Default = 6.

    Returns:
        tuple: Contains total number of guests, total number of tables.

    Examples:
        >>>get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>>get_party_stats([['Sal'], ['Richard', 'Fred'], ['Gary', 'Robin']], 1)
        (5, 5)
    """
    tables = 0

    attendees = 0
    for members in families:
        family = len(members)
        attendees += family
        tables += -(-family // table_size)

    tables = (attendees, tables)
    return tables
