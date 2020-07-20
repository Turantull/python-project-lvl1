# -*- coding:utf-8 -*-

"""Brain games engine."""

from brain_games import cli


NUMBER_OF_ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    if game.DESCRIPTION:
        print(game.DESCRIPTION, end='\n\n')
    else:
        print(end='\n')
    name = cli.greet_player()
    for _ in range(NUMBER_OF_ROUNDS):
        question, answer = game.question_creation()
        answer_player = cli.ask_player(question)
        if answer == answer_player:
            print('Correct!')
        else:
            err = 'is wrong answer ;(. Correct answer was'
            print("'{0}' {2} '{1}'.".format(answer_player, answer, err))
            break
    else:
        print('Congratulation, {0}!'.format(name))
