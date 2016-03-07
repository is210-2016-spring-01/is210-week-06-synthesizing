#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a module"""

BODY = 'Dear {0},\nI look forward to meeting with you on {1}.\nBest,\nMe'


def prepare_email(appointments):
    """This function returns a new list.

    Args:
        appointments(list): tuple contents that are streamlined for mass emails

    Returns:
        list: Gives new list after format string

    Examples:

        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]['Dear Jen,'
        '\nI look forward to meeting with you on 2015.\nBest,\nMe','
        ''Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """

    mass_email = []

    for candidate in appointments:
        mass_email.append(BODY.format(candidate[0], candidate[1]))
    return mass_email
