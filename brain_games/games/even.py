# -*- coding:utf-8 -*-

"""Brain even game."""

from random import randint

RULES = 'Answer "yes" if number even otherwise answer "no".'

def round():
    num = randint(0, 100)
    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer
