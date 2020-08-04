# -*- coding:utf-8 -*-

"""Brain calc game."""

from random import randint, choice
import operator

DESCRIPTION = 'What is the result of the expression?'


def make_question_and_answer():
    random_number_1 = randint(0, 100)
    random_number_2 = randint(0, 100)
    operations = [(operator.add, '+'),
                  (operator.sub, '-'),
                  (operator.mul, '*')]
    operation, sign = choice(operations)
    answer = operation(random_number_1, random_number_2)
    question_for_player = '{0} {1} {2}'.format(random_number_1,
                                               sign, random_number_2)
    return question_for_player, str(answer)
