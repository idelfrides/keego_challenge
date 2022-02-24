#!src/bin/python
# encoding: utf-8

import time
from utils.libs import (
    print_log, show_info,
    define_player_number,
    make_sound
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

            print_log(
                f'{player.player} GETS HIS END POSITION [{walk_}]...'
            )

            # find player profile to verify what he going to do
            if player_number == 1:  # implulsive one
                # continue

                if property_board_list[player.position-1] == 0:
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] IS AVAILABLE TO BUY')

                    player_info, player_board_content = player.buy_land_property_player_1(
                        player_number, all_player_info
                    )

                    all_player_info[str(player_number)] = player_info

                    if all_player_info[str(player_number)]['balance'] < 0:
                        print_log(f'GAME IS OVER FOR [ {player.player} ]...')
                        player_game_over.append(player_number)
                        all_player_info.pop(str(player_number))
                        print(player_game_over)

                    else:
                        property_board_list[player.position-1] = (
                            player_board_content)

                # property belong to other plyer
                elif not property_board_list[player.position-1].get(str(player_number)):
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] HAS AN OWNER')

                    player_info, other_player_property = (
                        player.pay_rent_for_property(
                        player_number,  all_player_info, property_board_list)
                    )

                    all_player_info[str(player_number)] = player_info
                    property_board_list[player.position-1] = (
                        other_player_property
                    )

                else:
                    # property belong to this player
                    pass

            if player_number == 2:  # demanding  player
                # continue
                if property_board_list[player.position-1] == 0:
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] IS AVAILABLE TO BUY')

                    player_info, player_board_content = player.buy_land_property_player_2(
                        player_number, all_player_info
                    )

                    if player_board_content == 0:
                        break

                    all_player_info[str(player_number)] = player_info

                    print_log(f'{player_board_content}')

                    if all_player_info[str(player_number)]['balance'] < 0:
                        print_log(f'GAME IS OVER FOR [ {player.player} ]...')
                        player_game_over.append(player_number)
                        all_player_info.pop(str(player_number))
                        # continue
                    else:
                        property_board_list[player.position-1] = (
                            player_board_content
                        )

                # property belong to other plyer
                elif not property_board_list[player.position-1].get(str(player_number)):
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] HAS AN OWNER')

                    player_info, other_player_property = (
                        player.pay_rent_for_property(
                        player_number, all_player_info, property_board_list)
                    )

                    all_player_info[str(player_number)] = player_info
                    property_board_list[player.position-1] = (
                        other_player_property
                    )
                else:
                    # property belong to this player
                    pass

            if player_number == 3:  # cautious one
                # import pdb; pdb.set_trace()
                try:
                    player.money = all_player_info[str(player_number)]['balance']
                except Exception as err:
                    print_log(f'EXCEPTION: {err}')

                if property_board_list[player.position-1] == 0:
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] IS AVAILABLE TO BUY')

                    player_info, player_board_content = player.buy_land_property_player_3(
                        player_number)

                    if player_board_content == 0:   # não comprou
                        continue

                    all_player_info[str(player_number)] = player_info

                    if all_player_info[str(player_number)]['balance'] < 0:
                        print_log(f'GAME IS OVER FOR [ {player.player} ]...')
                        player_game_over.append(player_number)
                        all_player_info.pop(str(player_number))
                    else:
                        # on the game
                        property_board_list[player.position-1] = (
                            player_board_content
                        )

                # property belong to other plyer
                elif not property_board_list[player.position-1].get(str(player_number)):
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] HAS AN OWNER')

                    player_info, other_player_property = (
                        player.pay_rent_for_property(
                        player_number, all_player_info, property_board_list)
                    )

                    all_player_info[str(player_number)] = player_info
                    property_board_list[player.position-1] = (
                        other_player_property
                    )
                else:
                    pass

            if player_number == 4:  # random one
                if property_board_list[player.position-1] == 0:
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] IS AVAILABLE TO BUY')

                    player_info, player_board_content = player.buy_land_property_player_4(
                        player_number, all_player_info
                    )

                    if player_board_content == 0:
                        continue

                    # print_log(f'{player_board_content}')
                    all_player_info[str(player_number)] = player_info

                    if all_player_info[str(player_number)]['balance'] < 0:
                        print_log(f'GAME IS OVER FOR [ {player.player} ]...')
                        player_game_over.append(player_number)
                        all_player_info.pop(str(player_number))
                    else:
                        property_board_list[player.position-1] = (
                            player_board_content
                        )

                # property belong to other plyer
                elif not property_board_list[player.position-1].get(str(player_number)):
                    print_log(f'PROPERTY IN POSITION [ {player.position} ] HAS AN OWNER')

                    player_info, other_player_property = (
                        player.pay_rent_for_property(
                        player_number, all_player_info, property_board_list)
                    )

                    all_player_info[str(player_number)] = player_info
                    property_board_list[player.position-1] = (
                        other_player_property
                    )
                else:
                    pass

    return


def calculate_winner(all_player_info):
    greatest_balance = 0
    balance = 0
    winner_behavior_list = []
    winner_dict= {}

    for one_player_info in all_player_info:
        for id_player, info in one_player_info.items():
            greatest_balance = info['balance']

            if balance > greatest_balance:
                hold_balace = greatest_balance
                greatest_balance = balance
                winner_player_number = int(id_player)
            else:
                balance = greatest_balance
                winner_player_number = int(id_player)

        winner_behavior_list.append(winner_player_number)

    count_1 = winner_behavior_list.count(1)
    count_2 = winner_behavior_list.count(2)
    count_3 = winner_behavior_list.count(3)
    count_4 = winner_behavior_list.count(4)

    winner_dict[str(count_1)] = 1
    winner_dict[str(count_2)] = 2
    winner_dict[str(count_3)] = 3
    winner_dict[str(count_4)] = 4

    winner_behavior_counter = [count_1, count_2, count_3, count_4]
    winner_behavior_list.clear()
    winner_behavior_list = [count_1, count_2, count_3, count_4]

    winner_behavior_counter.sort(reverse=True)
    most_win = winner_behavior_counter[0]

    winner_by_bahavior = winner_dict[str(most_win)]

    return winner_by_bahavior, winner_behavior_list


if __name__ == '__main__':

    simulations = 1
    winner_behavior = []

    simulations = 50
    simul = 1

    while simul < simulations:

        print_log(f'\n\n\n SIMULATION/PARTIDA --> {simulations}\n\n\n')

        ROUNDS = 50
        player_game_over = []
        round_by_simulation = []
        all_player_info = {}
        players_dict_info = {}
        property_board_list = [0 for v in range(1,21)]

        print_log(f'STARTING THE GAME ...\n')
        player_number = define_player_number()
        game_over_by_complete_round = 0

        for round in range(1, ROUNDS + 1):

            if player_number > 4:
                player_number = 1

            run_game(round, player_number, player_game_over,
                property_board_list, all_player_info)

            # print(f'\n\n player game over \n\n {player_game_over}')
            # print(f'\n\n property owner list \n\n {property_board_list}')
            print(f'\n\n all player info \n\n {all_player_info}')

            player_number += 1  # next player
            time.sleep(0)

            print_log(f'GOME OVER BY ROUND {round}')

        for key, value_ in all_player_info.items():
            players_dict_info[key] = value_

        winner_behavior.append(players_dict_info)

        game_over_by_complete_round += 1
        round_by_simulation.append(round)

        simul += 1

    winner_by_bahavior, winner_behavior_counter = (
        calculate_winner(winner_behavior)
    )
    wb_counter = winner_behavior_counter

    percentual_vitoria_1 = (wb_counter[0]/simulations) *100
    percentual_vitoria_2 = (wb_counter[1]/simulations) *100
    percentual_vitoria_3 = (wb_counter[2]/simulations) *100
    percentual_vitoria_4 = (wb_counter[3]/simulations) *100

    # round_mean = sum(round_by_simulation)/len(round_by_simulation)
    round_mean = sum(round_by_simulation)/simulations

    print('-'*80)
    print('\n GAME RESULTS \n')
    print('-'*40)

    print(f'\n PARTIDAS POR TIME OUT: {game_over_by_complete_round}')    # 1
    print(f'\n MÉDIA DE RODADAS POR PARTIDA : {round_mean}')           # 2
    print(f'\n TAXA DE VITORIAS DO IMPULSIVO: {percentual_vitoria_1}')   # 3
    print(f'\n TAXA DE VITORIAS DO EXIGENTE: {percentual_vitoria_2}')
    print(f'\n TAXA DE VITORIAS DO CAUTELOSO: {percentual_vitoria_3}')
    print(f'\n TAXA DE VITORIAS DO ALEATÓRIO: {percentual_vitoria_4}')
    print(f'\n COMPORTAMENTO MAIS VENCEDOR: {winner_by_bahavior}')        # 4

    print('-'*80)
