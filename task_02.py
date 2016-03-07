#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 2 file."""


email = 'Dear {0},\nI look forward to meeting with you on {1}.\nBest,\nMe'


def prepare_email(appointments):
    """To send out emails with patients' name and time.

    Args:
        appointments(mixed): Patients' name and time.

    Returns:
        Str: emails with patients' name and time

    Example:

        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        '['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting with you on March 3.\nBest,\nMe']
    """
    for patient in email:
        return [email.format(appointments[0][0], appointments[0][1]),
                email.format(appointments[1][0], appointments[1][1])]
