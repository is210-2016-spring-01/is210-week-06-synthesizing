#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring prepares an e-mail."""

CONTENT = 'Dear {0},\nI look forward to meeting with you on {1}.\nBest,\nMe'


def prepare_email(appointments):
    """Function creates a list of two-item tiples.

    Args:
        appointments(list): client's names and appointment time.

    Returns:
        client's name
        appointment time

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """
    for client in appointments:
         appointments.append(CONTENT.format(candidate[0], candidate[1]))
    return appointments
