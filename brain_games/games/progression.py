# -*- coding:utf-8 -*-

"""Brain progression game."""

from random import randint

DESCRIPTION = "What number is missing in the progression?"


def question_creation():
    length_progression = 10
    step = randint(1, length_progression)
    secret_elem = randint(0, length_progression - 1)
    start_num = randint(0, 100)
    finish = start_num + (step * length_progression)
    progression = list(range(start_num, finish, step))
    answer = progression[secret_elem]
    progression[secret_elem] = '..'
    question_fo_player = ' '.join(map(str, progressiya))
    return question_fo_player, str(answer)
