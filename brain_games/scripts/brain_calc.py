# -*- coding:utf-8 -*-

"""Script game brain-calc."""

from brain_games import cli


def main():
    """Run script."""
    cli.welcome_and_rules('What is the result of the expression?')
    name = cli.welcome_user()
    cli.game_calc(name=name)


if __name__ == '__main__':
    main()
