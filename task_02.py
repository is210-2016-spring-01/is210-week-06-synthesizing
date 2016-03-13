#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Appointment Tracker"""


def prepare_email(appointments):
    """lists appointments and client names.

    Args:
        appointments (tuple): two item tuple of client name and appointment time

    Returns:
        list: full client list with appointments

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """

    return 'Dear {}, \nI look forward to meeting with you on {}.\nBest, \nMe'.format(appointments)
