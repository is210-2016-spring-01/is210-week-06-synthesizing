#!/usr/bin/env python
# -*- coing: utf-8 -*-
"""Task 02"""


def prepare_email(*appointments):
    """appointments, A list of two-item tuples with the client's name
        and their appointment time as members"""    
    email ='Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

    Name1 = body[0][0]
    Time1 = body[0][1]

    Name2 = body[1][0]
    Time2 = body[1][1]
    for body in appointments:
    
        body1 = email.format(Name1, Time1)
        body2 = email.format(Name2, Time2)

        return body1, body2

