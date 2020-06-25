# -*- coding:utf-8 -*-

"""Script game brain-even."""

from brain_games import cli


def main():
    """Run script."""
    cli.welcome_and_rules('Answer "yes" if number even otherwise answer "no".')
    name = cli.welcome_user()
    cli.game(name=name)


if __name__ == '__main__':
    main()
