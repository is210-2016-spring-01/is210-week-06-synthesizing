#!/usr/bin/env python
# -*- coding: utf-8 -*-
"Let's prepare an email~"


def prepare_email(appointments):
    """Prepares an email when user provides names and times.
    
    There'd be paragraphs of text here should they be needed.
    
    Args:
        appointments(tuple): gives name and date/time of appointment
    
    Returns: 
        email(list): a completed, formatted email
        
    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    
    """

    email = []
    content = 'Dear {0}, \mI look forward to meeting with you on {1}.\nBest,\Me'
    for info in appointments:
        email.append(content.format(info[0], info[1]))
    return email
