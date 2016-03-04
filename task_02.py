#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating an email template for appointments."""

EMAIL_BODY = 'Dear {0},\nI look forward to meeting with you on {1}st,\nMe'


def prepare_email(appointments):
    """Function to create new list with client's email body.

    Args:
        appointments (list): Contains list of tuples client name and time.

    Returns:
        list: For looped list of custom email bodies.

    Examples:
        >>>prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']

        >>>prepare_email([('Howard', '2015'), ('Stern', '1.9.06')])
        ['Dear Howard,\nI look forward to meeting with you on 2015st,\nMe',
        'Dear Stern,\nI look forward to meeting with you on 1.9.06st,\nMe']
    """
    composed_mail = []
    for client in appointments:
        composed_mail.append(EMAIL_BODY.format(client[0], client[1]))
    return composed_mail
