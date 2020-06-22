# -*- coding:utf-8 -*-

"""Script game brain-calc."""

from brain_games import cli


def main():
    """Run script."""
    cli.welcome()
    cli.rules_of_game_calc()
    name = cli.welcome_user()
    cli.game_calc(name=name)


if __name__ == '__main__':
    main()
