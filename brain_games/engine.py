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
    name = cli.welcome_user()
    for _ in range(NUMBER_OF_ROUNDS):
        str_question, answer = game.start_the_round()
        answer_user = cli.question(str_question)
        if answer == answer_user:
            print('Correct!')
        else:
            err = 'is wrong answer ;(. Correct answer was'
            print("'{0}' {2} '{1}'.".format(answer_user, answer, err))
            break
    else:
        print('Congratulation, {0}!'.format(name))
