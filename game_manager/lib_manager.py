
# rent_value = valor de aluguel

from random import randint


class GameManager(object):

    def __init__(self, player, prop):
        self.player = player


    def propriedades(self):
        propriedade = {}

        propriedade['name'] = 'Cacheu'
        propriedade['owner'] = self.player
        propriedade['sell_value'] = 300
        propriedade['rent_value'] = 100
        propriedade['position'] = 2
        return 20


    def start_game_money(self):
        saldo = 300
        return saldo


    def get_player_position(self):
        to_walk = randint(1, 6)
        return to_walk


    def round_completed(self):
        return 100


    def lost_game(self):
        pass
    # saldo negativo


    def game_over(self):
        # 1 jogador com saldo positivo
        pass


    def define_player(self):
        """ 4 types
            Player one is impulsive
            Player two is demanding;
            Player three is cautious;
            Player four is random;
        """
        pass


    def buy_land_property(self):
        pass
