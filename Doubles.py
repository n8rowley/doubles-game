from aux_functions import *
import sys


def curate_players():
    curating = True
    add_players()
    while curating:
        in_str = input("\nPress enter to continue OR,\n"
                       "(+) to add players,\n"
                       "(-) to remove players"
                       # ",\n(=) to change players"
                       ": ")
        print()
        if in_str == "+":
            add_players()
        elif in_str == "-":
            remove_players()
        elif in_str == "":
            break
        else:
            print("\tnot recognized")




def cash_out(player_name, total, cashed_out_bool):
    if not cashed_out_bool[player_name]:
        players[player_name] += total
        cashed_out_bool[player_name] = True
        print(f'\t*{player_name.capitalize()} cashed out*')
    else:
        print(f'\n\t***{player_name.capitalize()} already cashed out this round***')
        acknowledge()

    return cashed_out_bool


CORRECTION_CODES = ["-change total",
                    "-change player score",
                    "-change current round",
                    "-change counter",
                    "-change player name",
                    "-end game"]


def error_correction(user_input, total, counter, game_round, cashed_out):
    if user_input == "-change total":
        total = change_total()
    if user_input == "-change counter":
        counter = change_counter()
    if user_input == "-change player score":
        change_player_score()
    if user_input == "-change current round":
        game_round = change_round()

    """change_player_score() isn't currently working"""
    # if user_input == "-change player name":
    #     cashed_out = change_player_name(cashed_out)

    if user_input == "-end game":
        game_round = sys.maxsize
        counter = sys.maxsize

    return total, counter, game_round, cashed_out


"""main loop"""
def play_game(low=10, high=10):
    still_playing = True
    while still_playing:
        curate_players()

        game_round = 1
        number_rounds = random.randint(low, high)
        while game_round <= number_rounds:
            total = 0
            counter = 0
            cashed_out = reset_cashed()

            while counter < 4 and not all_cashed_out(cashed_out):

                print(round_status_formatted(total, counter, game_round, cashed_out))

                in_put = input("roll result: ").lower()

                if in_put in CORRECTION_CODES:
                    total, counter, game_round, cashed_out = error_correction(in_put, total, counter, game_round, cashed_out)

                elif in_put.isalpha():
                    if in_put in players:
                        if counter == 3:
                            cashed_out = cash_out(in_put, total, cashed_out)
                        else:
                            print("\t***Not enough 7's***")
                            acknowledge()
                    elif in_put == "*":
                        total *= 2
                    else:
                        print("\tNot recognized")
                        acknowledge()

                elif in_put == '*':
                    total *= 2

                elif in_put.isnumeric():
                    in_put = int(in_put)
                    if in_put == 7:
                        total += 75
                        counter += 1
                    elif 2 <= in_put <= 12:
                        total += in_put
                    else:
                        print("\tOut of range")
                        acknowledge()

            if game_round < number_rounds:
                end_round_str = end_of_round_formatted(game_round)
                print(end_round_str)

                err_in = acknowledge()
                if err_in == "-add player":
                    add_players()
            game_round += 1

        print(game_over_formatted())

        while True:
            in_str = input("Play again? [y/n]: ").lower()
            if in_str == 'y':
                players.clear()
                print("\n" * 3)
                break
            elif in_str == 'n':
                still_playing = False
                break
            else:
                print("\tnot recognized")

    print("Good-bye")


if __name__ == "__main__":
    play_game()
