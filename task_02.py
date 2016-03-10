#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


def prepare_email(appointments):
    """Sending automated e-mails.

    Args:
        appointments (str):  Name and time.

    Returns:
        new list:  Arguments in the body of the email.

    Example:

        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe', 'D
         ear Max,\nI look forward to meeting with you on March 3.\nBest,\nMe']
    """
    message = 'Dear {0},\nI look forward to meeting with you on {1}.\nBest,\nMe'
    email = []
    for name, time in appointments:
        email.append(message.format(name, time))
    return email
