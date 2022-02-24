import os
from datetime import datetime
from random import randint


def show_info(**kwarg):

    info = f"""
    ---------------------------------------------------------
            GAME ROUND : [ {kwarg['round']} ]
            PLAYER PROFILE --> {kwarg['player']}
    ----------------------------------------------------------
    """
    print_log(info)
    return


def print_log(content):

    log_time = datetime.now()
    log_time = f'[ {str(log_time)[:19]} ] '
    real_content = '| '.join([log_time, content])

    print(f'\n{real_content}')

    return


def define_player_number():
    print_log(f'DEFINING THE PLAYER ORDER ...')
    position = randint(1, 4)
    # print_log(str(position))
    return position
