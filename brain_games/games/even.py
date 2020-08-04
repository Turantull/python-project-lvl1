# -*- coding:utf-8 -*-

"""Brain even game."""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question_and_answer():
    random_number = randint(0, 100)
    if random_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question_for_player = str(random_number)
    return question_for_player, answer
