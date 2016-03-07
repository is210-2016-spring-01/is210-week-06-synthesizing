#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring prepares an e-mail."""


def prepare_email(appointments=('name', 'appointment_time')):
    """Function creates a list of two-item tiples.

    Args:
        appointments(tuple): client's names and appointment time.

    Returns:
        client's name
        appointment time

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """
    for client in appointments:
        print 'Dear{},\nI look forward to meeting witth you on{}.\nBest,\nMe'
