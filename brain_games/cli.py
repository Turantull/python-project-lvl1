# -*- coding:utf-8 -*-

"""Acquaintance with the user."""

from prompt import string
from random import randint


def welcome():
    """Welcome!."""
    print('Welcome to the Brain Games!')


def rules_of_game_even():
    """Rules of the game even."""
    print('Answer "yes" if number even othewise answer "no".', end='\n\n')


def welcome_user():
    """Acquaintance."""
    global name
    name = string('May I have your name? ')
    print('Hello, {0}!'.format(name), end='\n\n')


def even(num):
    """Parity check."""
    if num % 2 == 0:
        return True
    else:
        return False


def question():
    """Question to the user."""
    num = randint(1, 100)
    global correct
    correct = 'Correct!'
    print('Question: {0}'.format(num))
    answer = string('Your answer: ')
    even_num = even(num)
    if even_num and answer == 'yes':
        return correct
    elif even_num is False and answer == 'no':
        return correct
    elif even_num is False and answer == 'yes':
        return "'yes' is wrong answer ;(. Correct answer was 'no'."
    elif even_num and answer == 'no':
        return "'no' is wrong answer ;(. Correct answer was 'yes'."
    else:
        pass


def game():
    """Game."""
    rounds = 3
    for step in range(rounds):
        result = question()
        if result == correct:
            print(correct)
        else:
            if result is not None:
                print(result)
            print("Let\'s try again, {0}!".format(name))
            return
    print('Congratulation, {0}!'.format(name))
