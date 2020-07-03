# -*- coding:utf-8 -*-

from prompt import string

"""Acquaintance with the user."""


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

