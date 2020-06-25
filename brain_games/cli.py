# -*- coding:utf-8 -*-

"""Acquaintance with the user."""

from prompt import string, integer
from random import randint


def welcome_and_rules(rules):
    """Welcome! And rules of the game."""
    print('Welcome to the Brain Games!')
    print(rules, end='\n\n')


def welcome_user():
    """Acquaintance."""
    name = string('May I have your name? ')
    print('Hello, {0}!'.format(name), end='\n\n')
    return name


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


def game(name):
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


def answer_calc(num1, num2, operation):
    if operation == 1:
        answer = num1 + num2
        operation_str = '+'
        return answer, operation_str
    elif operation == 2:
        answer = num1 - num2
        operation_str = '-'
        return answer, operation_str
    else:
        answer = num1 * num2
        operation_str = '*'
        return answer, operation_str


def question_calc():
    """Question to the user in game calc."""
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operation = randint(1, 3)
    answer, operation_str = answer_calc(num1, num2, operation)
    print('Question: {0} {1} {2}'.format(num1, operation_str, num2))
    answer_user = integer('Your answer: ')
    return answer, answer_user


def game_calc(name):
    """Game calc."""
    rounds = 3
    err = 'is wrong answer;(. Correct answer'
    for step in range(rounds):
        answer, answer_user = question_calc()
        if answer == answer_user:
            print('Correct!')
        else:
            print("'{0}' {2} '{1}'.".format(answer_user, answer, err))
            print("Let\'s try again, {0}!".format(name))
            return
    print('Congratulation, {0}'.format(name))
