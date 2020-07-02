# -*- coding:utf-8 -*-

"""Brain prime game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    num = randint(0, 100)
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer


def is_prime(num):
    pick = 2
    while pick * pick <= num and num % pick != 0:
        pick += 1
    return pick * pick > num
