#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the second week 6 synthesizing task with a function to create a
   basic reminder email text string for each - Retry 1"""

REMINDER_EMAIL = "Dear {0},\nI look forward to meeting with you on " \
                 "{1}.\nBest,\nMe"


def prepare_email(appointments):
    """Processes a list of tuples with appointment information and return a
       text sring for a simple reminder email.
    Args:
        appointments (list): list of tuple items each have a name and the
                             appointment day, date, and time.

    Returns:
        list: the list of formated email texts

    Examples:
        >>> prepare_email([('Jen', 'January 12, 2016'), ('Max', 'March 3'),
        ('Alisa', Monday, June 20')]
    ['Dear Jen,\nI look forward to meeting with you on January 12, 2016.\nBest,
    \nMe', 'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe',
    'Dear Alisa,\nI look forward to meeting you on Monday, June 20.\nBest\nMe']
    """

    email_texts = []

    for appt_info in appointments:

        email_texts.append(REMINDER_EMAIL.format(appt_info[0],
                                                 appt_info[1]))

    return email_texts
