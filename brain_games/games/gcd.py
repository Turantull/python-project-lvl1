# -*- coding:utf-8 -*-

"""Brain gcd game."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def round():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    str_question = '{0} {1}'.format(num1, num2)
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    answer = num1 + num2
    return str_question, str(answer)
