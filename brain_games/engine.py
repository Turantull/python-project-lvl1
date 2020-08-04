# -*- coding:utf-8 -*-

"""Brain games engine."""

from brain_games import cli


NUMBER_OF_ROUNDS = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = cli.ask_name_player()
    print('Hello, {0}!'.format(name), end='\n\n')
    for _ in range(NUMBER_OF_ROUNDS):
        question, answer = game.make_question_and_answer()
        print('Question: {0}'.format(question))
        answer_player = cli.ask_player_answer()
        if answer == answer_player:
            print('Correct!')
        else:
            wrong_answer = 'is wrong answer ;(. Correct answer was'
            print("'{0}' {2} '{1}'.".format(answer_player,
                                            answer, wrong_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
