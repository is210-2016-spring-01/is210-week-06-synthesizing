#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Six  Synthesizing Lists And Tuples."""


def get_party_stats(families, table_size=6):
    """Does some comparaison and returns a tuple in return.

    Args:
        families (strg): Argument with names of family members.

    Returns:
        tuple: the number of famlies with number of tables accordingly.

    Examples:

        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
        'Janis']])
        (6, 3)

        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
        'Janis']], 2)
        (6, 4)
    """
    table_count = 0
    tbc = 0
    for i in range(len(families)):
        family_count = 0
        for i in range(len(families[i])):
            table_count = table_count + 1
            family_count = family_count + 1

        if family_count > table_size:
            tbc = tbc + family_count / table_size + family_count % table_size
        else:
            tbc = tbc + 1
    return (table_count, tbc)
