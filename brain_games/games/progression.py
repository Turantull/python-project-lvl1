# -*- coding:utf-8 -*-

"""Brain progression game."""

from random import randint

DESCRIPTION = "What number is missing in the progression?"


def make_question_and_answer():
    length_progression = 10
    step = randint(1, 10)
    index_secret_elem = randint(0, length_progression - 1)
    start_num = randint(0, 100)
    finish = start_num + (step * length_progression)
    progression = list(range(start_num, finish, step))
    answer = progression[index_secret_elem]
    progression[index_secret_elem] = '..'
    question_for_player = ' '.join(map(str, progression))
    return question_for_player, str(answer)
