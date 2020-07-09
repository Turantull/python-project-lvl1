# -*- coding:utf-8 -*-

"""Brain calc game."""

from random import randint, choice
import operator

DESCRIPTION = 'What is the result of the expression?'


def start_the_round():
    question1 = randint(0, 100)
    question2 = randint(0, 100)
    operations = [[operator.add, '+'],
                  [operator.sub, '-'],
                  [operator.mul, '*']]
    operation = choice(operations)
    answer = operation[0](question1, question2)
    question_fo_user = '{0} {1} {2}'.format(question1, operation[1], question2)
    return question_fo_user, str(answer)
