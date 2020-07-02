# -*- coding:utf-8 -*-

"""Brain calc game."""

from random import randint

DESCRIPTION = 'What is the result of the expression?'


def round():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operation = randint(1, 3)
    if operation == 1:
        answer = num1 + num2
        str_operation = '+'
    elif operation == 2:
        answer = num1 - num2
        str_operation = '-'
    else:
        answer = num1 * num2
        str_operation = '*'
    str_question = '{0} {1} {2}'.format(num1, str_operation, num2)
    return str_question, str(answer)
