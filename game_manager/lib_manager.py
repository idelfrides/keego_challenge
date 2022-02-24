
# rent_value = valor de aluguel

from random import randint

# ---------------------------------------
# importing modules
# ---------------------------------------
from ijpypostgresql.Crud_oper import CrudOperations
from ijpypostgresql.ModulePostgreSQLdb import ModulePostgreSQLdb
from utils.libs import print_log

class PalyerManager(object):

    def __init__(self, player, money=300):
        self.player = self.define_player(player)
        self.money = money
        self.position = self.get_player_position()


    def get_land_property(self):
        manx_rent = 200

        land_property = {}
        land_property['name'] = ''
        land_property['owner'] = self.player
        land_property['sell_value'] = randint(manx_rent, 500)
        land_property['rent_value'] = randint(50, manx_rent)
        land_property['position'] = randint(1, 20)

        return  land_property


    def start_game_money(self):
        saldo = 300
        return saldo


    def get_player_position(self):
        to_walk = randint(1, 6)
        return to_walk


    def get_player_info(self):

        player_info= {
            'name': self.player,
            'current_property': {},
            'balance': self.money,
            'position': self.position
        }

        return player_info


    def round_completed(self):
        return 100


    def lost_game(self):
        pass
        # saldo negativo


    def game_over(self):
        # 1 jogador com saldo positivo
        pass


    def define_player(self, player_numer):
        """ 4 types
            Player one is impulsive
            Player two is demanding;
            Player three is cautious;
            Player four is random;
        """

        player_dict = {}

        player_dict['1'] = 'Inpulsive Player'
        player_dict['2'] = 'Demanding Player'
        player_dict['3'] = 'Cautious Player'
        player_dict['4'] = 'Random Player'

        return player_dict[str(player_numer)]


    def buy_land_property_player_1(self, player_number):
        print_log(f'IMPULSIVE PALYER BUYS ANY PROPERTY WHEREEVER HE STAND ON')

        property_dict = self.get_land_property()

        property_dict['name'] = 'IRAQUE'
        property_dict['position'] = self.position
        balance = self.money - property_dict['sell_value']

        player_content = {
            'name': self.player,
            'current_property': property_dict,
            'balance': balance,
            'position': self.position
        }
        player_full_content = {
            str(player_number): player_content
        }

        return player_full_content


    def buy_land_property_player_2(self, player_number):
        print_log(f'DEMANDING PALYER BUYS ANY PROPERTY AS LONG AS ITS RENT IS GREATER THAN 50.')

        property_dict = self.get_land_property()

        if property_dict['rent_value'] > 50:

            property_dict['name'] = 'USA'
            property_dict['position'] = self.position
            balance = self.money - property_dict['sell_value']

            player_info = self.get_player_info()

            player_info['current_property'] = property_dict
            player_info['balance'] = balance

            player_full_content = {
                str(player_number): player_info
            }

        else:
            player_info = self.get_player_info()
            player_full_content = 0

        return player_info, player_full_content


    def buy_land_property_player_3(self, player_number):
        print_log(f'CAUTIOUS PALYER BUYS ANY PROPERTY AS LONG AS HE HAS A \n   RESERVE OF 80 BALANCE LEFT AFTER THE PURCHASE IS MADE. ')

        property_dict = self.get_land_property()
        balance = self.money - property_dict['sell_value']

        if balance == 80:
            property_dict['name'] = 'FRANCE'
            property_dict['position'] = self.position

            player_info = self.get_player_info()

            player_info['current_property'] = property_dict
            player_info['balance'] = balance

            player_full_content = {
                str(player_number): player_info
            }

        else:
            player_info = self.get_player_info()
            player_full_content = 0

        return player_info, player_full_content


    def buy_land_property_player_4(self, player_number):
        print_log(f'RANDOM PALYER BUYS BUYS THE PROPERTY HE LANDS ON WITH A 50% PROBABILITY')

        buy = randint(1, 100)

        if buy == 50:      # 50%
            property_dict = self.get_land_property()
            balance = self.money - property_dict['sell_value']

            property_dict['name'] = 'FRANCE'
            property_dict['position'] = self.position

            player_info = self.get_player_info()

            player_info['current_property'] = property_dict
            player_info['balance'] = balance

            player_full_content = {
                str(player_number): player_info
            }

        else:
            player_info = self.get_player_info()
            player_full_content = 0

        return player_info, player_full_content


    def pay_rent_for_property(self, player_number, all_player_info, property_board_list):

        # import pdb; pdb.set_trace()
        other_player_property = property_board_list[self.position]
        player_info = all_player_info.get(str(player_number))

        balance = player_info['balance']
        # pay for property
        pay = balance - other_player_property[str(player_number)]['rent_value']
        other_player_property[str(player_number)]['balance'] += (
            other_player_property[str(player_number)]['balance']
        )

        player_info['balance'] = pay
        # all_player_info[str(player_number)] = player_info

        print(other_player_property)
        print(all_player_info)

        return player_info, other_player_property
