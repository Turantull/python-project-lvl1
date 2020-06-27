# -*- coding:utf-8 -*-

from prompt import string

"""Acquaintance with the user."""


def welcome_and_rules(rules=None):
    """Welcome! And rules of the game."""
    print('Welcome to the Brain Games!')
    if rules:
        print(rules, end='\n\n')
    else:
        print(end='\n')


def welcome_user():
    """Acquaintance."""
    name = string('May I have your name? ')
    print('Hello, {0}!'.format(name), end='\n\n')
    return name


def question(str_question):
    """Out question, in answer."""
    print('Question: {0}'.format(str_question))
    answer_user = string('Your answer: ')
    return answer_user


def correct():
    """Print correct."""
    print('Correct!')


def grac(name):
    """Print congratulation user."""
    print('Congratulation, {0}!'.format(name))


def wrong_answer(answer, answer_user):
    """Print wrong."""
    err = 'is wrong answer ;(. Correct answer was'
    print("'{0}' {2} '{1}'.".format(answer_user, answer, err))
