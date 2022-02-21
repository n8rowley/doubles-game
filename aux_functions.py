import sys
import random

players = {}

"""-------------Get input from the user-----------------------"""
def get_int(prompt, lower=0, upper=sys.maxsize):
    while True:
        in_str = input(prompt)
        if in_str.isnumeric():
            in_int = int(in_str)
            if lower <= in_int <= upper:
                return in_int
            else:
                print("\tout of range")
        else:
            print("\tEnter a number")


def get_active_player(prompt):
    while True:
        in_str = input(prompt)
        if in_str in players:
            return in_str
        else:
            print("\tNot an active player")

def get_str(prompt):
    pass


"""-----------------Manage Players---------------------------"""
def sorted_players():
    s = []
    copied_dict = {}
    for i in players:
        copied_dict[i] = players[i]

    while len(copied_dict) > 0:
        top_tup = random.choice(list(copied_dict.items()))
        for i in copied_dict:
            inspect_val = copied_dict[i]
            if inspect_val > top_tup[1]:
                top_tup = (i, copied_dict[i])

        copied_dict.pop(top_tup[0])
        s.append(top_tup[0])
    return s


def add_players():
    adding_players = True
    while adding_players:
        in_put = input("Player name: ").lower()
        if in_put == "":
            break
        else:
            add_player(in_put, 0)

    print(active_players_formatted())


def add_player(add_name, score):
    players[add_name] = score


def remove_players():
    print(active_players_formatted())
    remove_name = get_active_player("\nPlayer to remove: ")

    remove_player(remove_name)
    print(remove_name.capitalize() + " was removed")

    print(active_players_formatted())


def remove_player(remove_name):
    players.pop(remove_name)


def change_player_name(cashed_out):
    print(active_players_formatted())
    change_name = get_active_player("\nPlayer name to change: ")
    new_name = input(f"\nPrevious name: {change_name.capitalize()}\n\tNew name: ")
    score = players[change_name]
    cashed_out_pass = cashed_out[change_name]
    remove_player(change_name)
    add_player(new_name, score)


    cashed_out[new_name] = cashed_out_pass
    cashed_out.pop(change_name)

    print(active_players_formatted())

    return cashed_out


def all_cashed_out(cash_dict):
    for i in cash_dict:
        if not cash_dict[i]:
            return False
    return True

def reset_cashed():
    cashed_out = {}
    for i in players:
        cashed_out[i] = False
    return cashed_out


"""-----------------Error correction-----------------------------"""
def change_total():
    return get_int("\tEnter new total:")


def change_counter():
    return get_int("\tEnter new counter: ", upper=3)


def change_player_score():
    player_to_change = get_active_player("\tEnter player's name: ")
    new_score = get_int(f'\t\tEnter {player_to_change}\'s correct score: ')
    players[player_to_change] = new_score


"""This will allow the round to be set to any number regardless of the max number of rounds.
   The game will end after the round if set to a number greater than the number of rounds selected
   for the game"""
def change_round():
    return get_int("\tEnter current round: ")



"""------------------Display Formatting----------------------------"""

BOX_W = 40
NAME_W = 12
SCORE_W = 12
END_W = 2
DIST_BEHIND_W = BOX_W - NAME_W - SCORE_W - END_W
COUNTER_W = 15
REMAIN_W = BOX_W - COUNTER_W - END_W

def horizontal_line(padding='-'):
    line_str = "|"
    line_str += padding * (BOX_W - 2)
    line_str += "|\n"
    return line_str


def info_line(info):
    line_str = "|"
    line_str += format(info, '^38s')
    line_str += "|\n"
    return line_str


def standing_line(player_name, player_score):
    player_stats = "|"
    player_stats += format(player_name, f'>{NAME_W}s')
    player_stats += format(player_score, f'<{SCORE_W},d')
    distance_back = format(players[sorted_players()[0]] - player_score, ",")
    player_stats += format(f'[-{distance_back}]', f'<{DIST_BEHIND_W}s')
    player_stats += "|\n"
    return player_stats


def standings_formatted(padding="-", track_cashed=False, is_cashed_out=None):
    if track_cashed:
        assert is_cashed_out is not None

    standings_str = horizontal_line(padding)

    for i in sorted_players():
        player_name = ""
        if track_cashed and is_cashed_out[i]:
            player_name += "*"
        player_name += (i.capitalize() + ": ")
        player_stats = standing_line(player_name, players[i])

        standings_str += player_stats

    standings_str += horizontal_line(padding)

    return standings_str


def end_of_round_formatted(r, pad="+"):
    end_round_str = ""
    end_round_str += horizontal_line(pad)
    end_round_str += info_line(f'END OF ROUND {r}')
    end_round_str += info_line(f'STANDINGS')
    end_round_str += standings_formatted(padding=pad)
    return end_round_str


def round_progress_formatted(count, total):
    progress_str = "|"
    progress_str += format("7-COUNTER: ", F'>{COUNTER_W}s')
    progress_str += format(count, f'<{REMAIN_W},d')
    progress_str += "|\n"
    progress_str += "|"
    progress_str += format("ROUND TOTAL: ", f'>{COUNTER_W}s')
    progress_str += format(total, f'<{REMAIN_W},d')
    progress_str += "|\n"
    return progress_str


def round_status_formatted(total, counter, game_round, out_dict):
    status_str = horizontal_line()
    status_str += info_line(f'ROUND {game_round}')
    status_str += standings_formatted(track_cashed=True, is_cashed_out=out_dict)
    status_str += round_progress_formatted(counter, total)
    status_str += horizontal_line()

    return status_str


def game_over_formatted(pad="*"):
    over_str = horizontal_line(padding=pad)
    over_str += info_line("GAME OVER")
    over_str += standings_formatted(padding=pad)
    return over_str


def active_players_formatted(pad="="):
    player_str = ""
    player_str += horizontal_line(padding=pad)
    player_str += info_line("PLAYERS")
    player_str += horizontal_line(padding=pad)
    for i in players:
        player_str += info_line(" " + i.capitalize() + (" " * (BOX_W - END_W - len(i) - 1)))
    player_str += horizontal_line(padding=pad)
    return player_str


def acknowledge():
    print("\tPress enter to continue")
    return input()
