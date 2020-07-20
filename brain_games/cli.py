# -*- coding:utf-8 -*-

from prompt import string

"""Acquaintance with the user."""


def ask_name_player():
    """Acquaintance."""
    name = string('May I have your name? ')
    return name


def ask_player_answer():
    """Ask player answer."""
    answer_player = string('Your answer: ')
    return answer_player
