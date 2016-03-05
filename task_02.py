#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Six  Synthesizing Lists And Tuples."""


def prepare_email(appointments):
    """ Does use 'for' loop to create new lists.

    Args:
        appointments (tuple): include client's names and appoitment time.

    Return:
        return a new list.

    Examples:

        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting with you on March 3.\nBest,\nMe']
    """
    res = []
    for i in range(len(appointments)):
        write = "Dear {},\nI look forward to meeting with you on {}."
        "\nBest,\nMe".format(appointments[i][0], appointments[i][1])
        res.append(write)
    return res
