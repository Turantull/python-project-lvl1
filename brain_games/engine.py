# -*- coding:utf-8 -*-

"""Brain games engine."""


from prompt import string


def ask(question):
    """Ask player."""
    answer = string(question)
    return answer


def play(game):
    number_of_rounds = 3
    print('Welcome to the Brain Games!')
    name = ask('May I have your name? ')
    print('Hello, {0}!'.format(name), end='\n\n')
    while number_of_rounds:
        question, answer = game.make_question_and_answer()
        print('Question: {0}'.format(question))
        answer_player = ask('Your answer: ')
        if answer == answer_player:
            print('Correct!')
        else:
            wrong_answer = "'{0}' is wrong answer ;(. Correct answer was '{1}'"
            print(wrong_answer.format(answer_player, answer))
            print("Let's try again, {}!".format(name))
            break
        number_of_rounds -= 1
        if number_of_rounds == 1:
            print('Congratulations, {0}!'.format(name))
