# -*- coding:utf-8 -*-

"""Brain gcd game."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def question_creation():
    random_number_1 = randint(0, 100)
    random_number_2 = randint(0, 100)
    question_fo_player = '{0} {1}'.format(random_number_1, random_number_2)
    answer = gcd(random_number_1, random_number_2)
    return question_fo_player, str(answer)


def gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    return num_1 + num_2
