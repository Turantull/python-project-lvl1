# -*- coding:utf-8 -*-

"""Brain prime game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_creation():
    random_number = randint(0, 100)
    if is_prime(random_number):
        answer = 'yes'
    else:
        answer = 'no'
    return random_number, answer


def is_prime(num):
    if num < 2:
        return False
    pick = 2
    while pick * pick <= num and num % pick != 0:
        pick += 1
    return pick * pick > num
