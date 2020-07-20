# -*- coding:utf-8 -*-

"""Brain calc game."""

from random import randint, choice
import operator

DESCRIPTION = 'What is the result of the expression?'


def question_creation():
    random_number_1 = randint(0, 100)
    random_number_2 = randint(0, 100)
    operations = [[operator.add, '+'],
                  [operator.sub, '-'],
                  [operator.mul, '*']]
    operation = choice(operations)
    answer = operation[0](random_number_1, random_number_2)
    question_fo_player = '{0} {1} {2}'.format(random_number_1, operation[1], random_number_2)
    return question_fo_player, str(answer)
