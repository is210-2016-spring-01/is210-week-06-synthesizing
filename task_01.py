#!/usr/bin/env python
# -*- coing: utf-8 -*-
"""Task 01"""


def get_party_stats(table_size=6, *families):
    """``families``, a list of families which are, themselves, lists of
    members, table_size``, the maximum number of seats at each table, defaults
    to six """
    party = sum(len(guests) for guests in families)
    table_seats = sum(-(-len(guests) // table_size) for guests in families)
    return party, table_seats
