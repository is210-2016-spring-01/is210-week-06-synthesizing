#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Table seating lists"""


def get_party_stats(families, table_size=6):
    """Sorts and places families for party.

    Args:
        families (list): list of names
        table_size (int, optional): amount of people at table. Default: 6

    Returns:
        tuple: total number of guests and total number of tables
        
    Examples:
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

    """

    return (len([families]), -(-len([families])//table_size))
