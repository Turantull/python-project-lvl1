# -*- coding:utf-8 -*-

"""Brain gcd game."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def start_the_round():
    question1 = randint(0, 100)
    question2 = randint(0, 100)
    question_fo_user = '{0} {1}'.format(question1, question2)
    answer = gcd(question1, question2)
    return question_fo_user, str(answer)


def gcd(question1, question2):
    while question1 != 0 and question2 != 0:
        if question1 > question2:
            question1 %= question2
        else:
            question2 %= question1
    return question1 + question2
