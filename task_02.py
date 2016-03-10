#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Module"""


def prepare_email(appointments):
    """Defines a function that a list of email messages.

    Args:
        appointments (list): client's name and appointment time

    Returns:
        list: body of the client's email

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen, \nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max, \nI look forward to meeting you on March 3. \nBest\nMe']
    """

    body = 'Dear {0},\nI look forward to meeting with you on {1}.\nBest,\nMe'
    email = []

    for info in appointments:
        email.append(body.format(info[0], info[1]))
    return email
