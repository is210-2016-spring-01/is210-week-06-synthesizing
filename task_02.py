#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Email Prep"""


def prepare_email(appointments):
    """This function will generate email body.

    This function will prepare some data and generate automated e-mails for
    clients.

    Args:
        appointments(tuple): Tuples that displays client's name.

    Returns:
        email(list): Returns auto generated email body.

    Example:
        >>> prepare_email([('Jennifer', '2015'), ('James', 'March 16')]
        ['Dear Jennifer,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear James,\nI look forward to meeting you on March 16.\nBest\nMe']
    """

    messages = []
    email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for email_body in appointments:
        messages.append(email.format(email_body[0], email_body[1]))
    return messages
