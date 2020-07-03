# -*- coding:utf-8 -*-

"""Brain even game."""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def start_the_round():
    num = randint(0, 100)
    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer
