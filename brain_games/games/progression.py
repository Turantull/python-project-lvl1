# -*- coding:utf-8 -*-

"""Brain progression game."""

from random import randint

RULES = "What number is missing in the progression?"


def round():
    length_progression = 10
    step = randint(1, 10)
    secret_elem = randint(0, 9)
    start_num = randint(0, 100)
    finish = start_num + (step * length_progression)
    progressiya = list(range(start_num, finish, step))
    answer = progressiya[secret_elem]
    progressiya[secret_elem] = '..'
    str_question = ' '.join(map(str, progressiya))
    return str_question, str(answer)
