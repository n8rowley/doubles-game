from Game import Game


game = Game(3)
print("Welcome to the BANK!\n")

game.setUp()
while True:
    game.play()

    userInput = input("\nPlay again? (y/n): ")
    if not userInput == 'n':
        userInput = input("\nSame players? (y/n): ")
        if not userInput == 'n':
            game = Game(players=game.players, rounds=1)
            game.players.gameReset()
        else:
            game = Game(rounds=10)
            game.setUp()
    else:
        break
