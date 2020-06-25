# -*- coding:utf-8 -*-

"""Brain games engine."""

from random import randint
from brain_games import cli


NUMBER_OF_ROUNDS = 3

def start(game):
    cli.welcome_and_rules(game.RULES)
    name = cli.welcome_user()
