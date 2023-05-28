from PlayersCollection import PlayersCollection
from formatting import formattedContent

class Game:
    def __init__(self, rounds=10, players=None):
        self.rounds = rounds
        self.currentRound = 1
        self.players = PlayersCollection() if players == None else players
        self.total = 0
        self.sevens = 0

    def setUp(self):
        print(formattedContent('Setup'))

        self.players.curate()

        self.settingsMenu(True)
            
    def play(self):
        while self.roundOpen():
            print(formattedContent(
                f"Round {self.currentRound}", 
                self.players.nameScoreContent(), 
                [
                    format("7's Count: ", '>19s') + format(self.sevens, '<19d'), 
                    format("Round Total: ", '>19s') + format(self.total, '<19,d'),
                ]
            ), end='')
            
            userInput = input(f"Roll result{' (-c to cash out)' if self.sevens == 3 else ''}: ")
            if userInput.isnumeric():
                roll = int(userInput)
                if roll == 7:
                    self.total += 75
                    self.sevens += 1
                elif 2 <= roll <= 12:
                    self.total += roll
                else:
                    input('Out of range')
            elif userInput == 'd' or userInput == '*':
                if self.total == 0:
                    while True:
                        try:
                            newVal = int(input('\tInput the number showing on each die (1-6): '))
                            if not (1 <= newVal <= 6):
                                raise Exception
                            self.total = newVal * 100
                            break
                        except:
                            input("*** Must be between 1 and 6 ***")
                            continue
                else:
                    self.total *= 2
            elif userInput == "-c" or userInput == '$':
                if self.sevens < 3:
                    input("\n*** Not enought 7's ***")
                    continue
                self.cashOut()
            elif userInput == '--settings' or userInput == '-t':
                self.settingsMenu()
            elif userInput == '-h':
                input("This is the help message")
            else:
                input("\n*** Incorrect key, try again ***")
                continue

        self.advanceRound()


    def advanceRound(self):
        
        self.currentRound += 1
        if self.currentRound > self.rounds:
            input(formattedContent(
                label=f"GAME OVER",
                content=self.players.nameScoreContent()
            ))
            
            self.endGame()
        else:
            input(formattedContent(
                label=f"End of Round {self.currentRound - 1}",
                content=self.players.nameScoreContent()
            ))
            self.total = 0
            self.sevens = 0
            self.players.roundReset()
            self.play()

    def endGame(self):
        pass


    def cashOut(self):
        print()
        while not self.players.allCashed():
            userInput = input("\tEnter player's name to cash them out: ")
            if userInput == "":
                return
            
            self.players.cashOut(userInput, self.total)


    def roundOpen(self):
        return self.sevens < 4 and not self.players.allCashed()


    def settingsMenu(self, start=False):
        while True:
            settingOptions = ['Begin Game' if start else 'Back to Game', 'Modify Players', 'Modify Game Settings']
            print(formattedContent(
                label = "Settings",
                content= [format(f"{index}. {option}", '<38s') for index, option in enumerate(settingOptions)]
            ))

            userInput = input(f"Select and option (0 - {len(settingOptions) - 1}): ")
            if userInput == '0' or (userInput == '' and start):
                break
            elif userInput == '1' or userInput == '-p':
                self.players.modify()
            elif userInput == '2' or userInput == '-g':
                self.modifyGame()
            else:
                input('\n*** Incorrect key, try again ***')
                continue
    
    def modifyGame(self):
        gameOptions = [
            "Finished",
            f"Modify 7's Count ({self.sevens})", 
            f"Modify Round Total ({self.total})", 
            f"Modify Number of Rounds ({self.rounds})" , 
            f"Modify Current Round ({self.currentRound})"
        ]
        print(formattedContent(
            label="Game Options",
            content=[format(f"{index}. {option}", '<38s') for index, option in enumerate(gameOptions)]
        ))
        
        userInput = input(f"Select an option (0 - {len(gameOptions) -1}): ")
        if userInput == '0':
            return
        elif userInput == '1' or userInput == '-7':
            while True:
                try: 
                    newVal = int(input("\tNew count: "))
                    if not (0 <= newVal <= 3):
                        raise Exception
                    self.sevens = newVal
                    break
                except:
                    input("\n*** Invalid input, try again ***")
        elif userInput == '2':
            while True:
                try:
                    self.total = int(input("\tNew total: "))
                    break
                except:
                    input("\n*** Invalid input, try again ***")
        elif userInput == '3':
            print(f"\nCurrent total number of rounds: {self.rounds}")
            while True:
                try:
                    newVal = int(input("\tNew number of rounds: "))
                    if newVal < self.currentRound:
                        raise Exception
                    self.rounds = newVal
                    break
                except:
                    input("\n*** Total number of rounds must be more than the number of rounds played ***")
                    continue
        elif userInput == '4':
            print(f"\nCurrent round: {self.currentRound}")
            while True:
                try:
                    newVal = int(input("\tNew current round: "))
                    if newVal > self.rounds:
                        raise Exception
                    self.currentRound = newVal
                    break
                except: 
                    input("\n*** Current round must not be greater than the total number of rounds ***")
                    continue
                
