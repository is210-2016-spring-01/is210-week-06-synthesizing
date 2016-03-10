#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Email blast module."""


def prepare_email(appointments):
    """Compile emails.

    Args:
        appointments (tuple): Client name, appointment times.

    Returns:
        string: Individual email messages.

    Examples:
        >>> prepare_email([('Mark', '12/12'), ('Sue', 'Jan 2')])
        ['Dear Mark, \nI look forward to meeting with you on 12/12.\nBest,
        \nMe', 'Dear Sue, \nI look forward to meeting with you on Jan 2.
        \nBest, \nMe']

        >>> prepare_email([('Bill', 'Today'), ('C.W.', '3/6 at 2P')])
        ['Dear Bill,\nI look forward to meeting with you on Today.\nBest,
        \nMe', 'Dear C.W.,\nI look forward to meeting with you on 3/6 at 2P.
        \nBest,\nMe']
    """
    mess = 'Dear {0},\nI look forward to meeting with you on {1}.\nBest,\nMe'
    emails = []
    for name, date in appointments:
        emails.append(mess.format(name, date))
    return emails
