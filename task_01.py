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
    table_num = 0
    people_num = 0

    for people in families:
        table_num += -(-len(people)//table_size)
        people_num += len(people)
    return people_num, table_num
