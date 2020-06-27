# -*- coding:utf-8 -*-

"""Brain games engine."""

from brain_games import cli


NUMBER_OF_ROUNDS = 3

def start(game):
    cli.welcome_and_rules(game.RULES)
    name = cli.welcome_user()
    for _ in range(NUMBER_OF_ROUNDS):
        str_question, answer = game.round()
        answer_user = cli.question(str_question)
        if answer == answer_user:
            cli.correct()
        else:
            cli.wrong_answer(answer, answer_user)
            break
    else:
        cli.grac(name)
