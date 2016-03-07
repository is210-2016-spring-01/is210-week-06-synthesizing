#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring creates seating charts."""

def get_party_stats(families, table_size=6):
    """This function organizes seating.

    Arg:
        families (list): A list of names.
        table_size (integer): The maximum number of seats at each table.

    Returns:
        mxed: Families and the tables they sit at.

    Examples:
    >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
    (6, 3)

    >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']], 2)
    (6, 4)

    """
    for person in families:
        person += len(families)

    for table in table_size:
        tables = -len(families) // table_size
    Return (people_per_table, number_of_tables)





