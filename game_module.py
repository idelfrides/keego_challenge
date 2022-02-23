#!src/bin/python
# encoding: utf-8

from utils.libs import (
    print_log, show_info,
    define_player_order
)

from game_manager.lib_manager import GameManager

from random import randint


def run_game(round, player_order):

    show_info(round=round, player=player_order)


    # dado = randint(1, 6)

    return







if __name__ == '__main__':

    ROUNDS = 5

    print_log(f'STARTING THE GAME ...\n')
    player_order = define_player_order()

    for round in range(1, ROUNDS):

        if player_order > 4:
            player_order = 1

        run_game(round, player_order)

        player_order += 1  # next player


    print_log(f'GOME OVER')
