# -*- coding:utf-8 -*-

from prompt import string

"""Acquaintance with the user."""


def greet_player():
    """Acquaintance."""
    name = string('May I have your name? ')
    print('Hello, {0}!'.format(name), end='\n\n')
    return name


def ask_player(question):
    """Out question, in answer."""
    print('Question: {0}'.format(question))
    answer_player = string('Your answer: ')
    return answer_player
