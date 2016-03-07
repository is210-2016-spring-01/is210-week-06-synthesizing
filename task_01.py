#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 1 docstring."""


def get_party_stats(families, table_size=6):
    """Fuction that returns total number of guests and total number of tables.

    Args:
        families (list):  List of members of families.
        table_size(int):  Max number of seats at each table, default 6.

    Returns:
        num_of_guests:  Total number of guests
        num_of_tables:  Total number of tables

    Examples:
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']]
        )
        (6, 3)
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']]
        , 2)
        (6, 4)
    """
    num_of_guests = 0
    num_of_tables = 0
    for name in families:
        num_of_guests += len(name)
        num_of_tables += -(-len(name) // table_size)
    return (num_of_guests, num_of_tables)
