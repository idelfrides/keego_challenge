#!src/bin/python
# encoding: utf-8

import time
from utils.libs import (
    print_log, show_info,
    define_player_number,
)

from game_manager.lib_manager import PalyerManager
from random import randint


def run_game(round, player_number, player_game_over, property_board_list, all_player_info):

    player = PalyerManager(player=player_number)
    show_info(round=round, player=player.player)

    print_log(f'{player.player} MUST WALK [{player.position}] POSITION')

    if player_number in player_game_over:
        print_log(f'GAME IS OVER FOR [ {player.player} ] NUMBER {player_number}')
        return

    for walk_ in range(1, player.position + 1):
        print_log(f'{player.player} IN POSITION [{walk_}]...')

        if walk_ == player.position:
            # call play beavior
            print_log(
                f'{player.player} GETS HIS END POSITION [{walk_}]...'
            )

            # find player profile to verify what he going to do
            if player_number == 1:  # implulsive one

                if property_board_list[player.position] == 0:
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] IS AVAILABLE TO BUY')

                    player_full_content = player.buy_land_property_player_1(
                        player_number)

                    print(player_full_content)

                    if player_full_content[str(player_number)]['balance'] < 0:
                        print_log(f'GAME IS OVER FOR [ {player.player} ]...')
                        player_game_over.append(player_number)
                        property_board_list.insert(player.position, 0)
                        continue

                    property_board_list.insert(
                        player.position, player_full_content)

                elif not property_board_list[player.position].get(player_number):
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] HAS AN OWNER')
                    import pdb; pdb.set_trace()

                    player.pay_rent_for_property(
                        player_number, property_board_list)
                else:
                    # property belong to this player
                    pass

            if player_number == 2:  # demanding  player

                if property_board_list[player.position] == 0:
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] IS AVAILABLE TO BUY')

                    player_info, player_full_content = player.buy_land_property_player_2(
                        player_number)

                    all_player_info[str(player_number)] = player_info

                    print_log(f'{player_full_content}')
                    try:
                        if player_full_content[str(player_number)]['balance'] < 0:
                            print_log(f'GAME IS OVER FOR [ {player.player} ]...')
                            player_game_over.append(player_number)
                            # all_player_info.pop(str(player_number))
                            # continue
                    except Exception as err:
                        print_log(f'{player.player} DO NOT BUY THE PROPERTY [ {player.position} ]')

                    property_board_list.insert(
                        player.position, player_full_content
                    )

                elif not property_board_list[player.position].get(str(player_number)):
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] HAS AN OWNER')
                    # import pdb; pdb.set_trace()

                    player_info, other_player_property = (
                        player.pay_rent_for_property(
                        player_number,  all_player_info, property_board_list)
                    )

                    all_player_info[str(player_number)] = player_info
                    property_board_list.insert(
                        player.position, other_player_property
                    )
                else:
                    # property belong to this player
                    pass

            if player_number == 3:  # cautious one

                if property_board_list[player.position] == 0:
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] IS AVAILABLE TO BUY')

                    player_info, player_full_content = player.buy_land_property_player_3(
                        player_number)

                    all_player_info[str(player_number)] = player_info

                    print(player_full_content)

                    try:
                        if player_full_content[str(player_number)]['balance'] < 0:
                            print_log(f'GAME IS OVER FOR [ {player.player} ]...')
                            player_game_over.append(player_number)
                            # property_board_list.insert(player.position, player_full_content)
                            # continue
                    except Exception as err:
                        print_log(f'{player.player} DO NOT BUY THE PROPERTY [ {player.position} ]')

                    property_board_list.insert(
                        player.position, player_full_content
                    )

                elif not property_board_list[player.position].get(str(player_number)):
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] HAS AN OWNER')
                    # import pdb; pdb.set_trace()

                    player_info, other_player_property = (
                        player.pay_rent_for_property(
                        player_number,  all_player_info, property_board_list)
                    )

                    all_player_info[str(player_number)] = player_info
                    property_board_list.insert(
                        player.position, other_player_property
                    )
                else:
                    # property belong to this player
                    pass


            if player_number == 4:  # random one

                if property_board_list[player.position] == 0:
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] IS AVAILABLE TO BUY')

                    player_info, player_full_content = player.buy_land_property_player_4(
                        player_number)

                    print_log(f'{player_full_content}')
                    all_player_info[str(player_number)] = player_info

                    try:
                        if player_full_content[str(player_number)]['balance'] < 0:
                            print_log(f'GAME IS OVER FOR [ {player.player} ]...')
                            player_game_over.append(player_number)
                            #  property_board_list.pop(player.position)
                            # continue
                    except Exception as err:
                        print_log(f'{player.player} DO NOT BUY THE PROPERTY [ {player.position} ]')

                    property_board_list.insert(
                        player.position, player_full_content
                    )

                elif not property_board_list[player.position].get(str(player_number)):
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] HAS AN OWNER')

                    import pdb; pdb.set_trace()

                    player_info, other_player_property = (
                        player.pay_rent_for_property(
                        player_number,  all_player_info, property_board_list)
                    )

                    all_player_info[str(player_number)] = player_info
                    property_board_list.insert(
                        player.position, other_player_property
                    )
                else:
                    # property belong to this player
                    pass

    return


if __name__ == '__main__':

    ROUNDS = 100
    player_game_over = []
    all_player_info = {}
    property_board_list = [0 for v in range(1,21)]

    print_log(f'STARTING THE GAME ...\n')
    player_number = define_player_number()

    for round in range(1, ROUNDS):

        if player_number > 4:
            player_number = 1

        run_game(round, player_number, player_game_over,
            property_board_list, all_player_info)

        print(f'\n\n player game over \n\n {player_game_over}')
        print(f'\n\n property owner list \n\n {property_board_list}')
        print(f'\n\n all player info \n\n {all_player_info}')

        player_number += 1  # next player
        time.sleep(2)


    print_log(f'GOME OVER')
