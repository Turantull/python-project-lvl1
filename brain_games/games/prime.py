# -*- coding:utf-8 -*-

"""Brain prime game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_creation():
    question = randint(0, 100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(question):
    if question < 2:
        return False
    pick = 2
    while pick * pick <= question and question % pick != 0:
        pick += 1
    return pick * pick > question
