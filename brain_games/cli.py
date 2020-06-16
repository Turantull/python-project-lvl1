# -*- coding:utf-8 -*-

"""Acquaintance with the user."""

from prompt import string


def welcome_user():
    """Acquaintance."""
    name = string('May I have your name? ')
    print('Hello, {0}'.format(name))
