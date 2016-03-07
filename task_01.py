#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 1 file."""


def get_party_stats(families, table_size=6):
    """To calculate the number of attendees and tables needed.

    Args:
        families(list): a list of memebers.
        table_size(int): table size of 6.

    Returns:
        mixed: people count & table count.

    Examples:

        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
        'Janis']])
        '(6, 3)'
    """
    for people in families:
        tab_count = -(-len(people) // table_size)
        people_count = len(families)
        return people_count, tab_count
