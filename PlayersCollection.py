from Player import Player
from formatting import formattedContent


class PlayersCollection:
    def __init__(self):
        self.all = []

    def curate(self):
        print("\nEnter the names of the players")
        while True:
            userInput = input("Name: ")
            if userInput == "":
                break
            else:
                # Check that each name is unique
                self.all.append(Player(userInput))

        print(formattedContent('Player List', self.nameOnlyContent()))


    def nameOnlyContent(self):
        self.all.sort(key=len, reverse=True)
        return [format(p.name, '<38s') for p in self.all]    

    def nameScoreContent(self):
        self.all.sort(key=len, reverse=True)
        return [format(f"{'*' if p.cashed else ''}{p.name}: ", '>19s') + format(p.score, '<10,d') + format(f"[-{format(self.all[0].score - p.score, ',d')}]", '>9s') for p in self.all]

    def nameSelectionContent(self):
        self.all.sort(key=len, reverse=True)
        return [format(f"{index}. {p.name}", '<38s') for index, p in enumerate(self.all)]
        

    def formatPlayerList(self, withIndex=False):
        for index, player in enumerate(self.all):
            s = f"{index}. " if withIndex else ""
            s += f"{format(player.name, '.<20')}{format(player.score,'>10d')}"
            print(s)


    def modify(self):
        while True:
            modifyOptions = ['Finished', 'Add players', 'Change name', 'Change score', 'Change cashed out', 'Remove from game']
            print(formattedContent(
                label=f"Modify Players",
                content=[format(f"{index}. {option}", '<38s') for index, option in enumerate(modifyOptions)]
            ))

            userInput = input(f'Select an option (0 - {len(modifyOptions) - 1}): ')

            if userInput == '0':
                return
            elif userInput == '1' or userInput == '-a':
                self.curate()
            elif userInput == '2' or userInput == "-n":
                self.changePlayerName()
            elif userInput == '3' or userInput == "-s":
                self.changePlayerScore()
            elif userInput == '4':
                self.changePlayerCashed()
            elif userInput == '5' or userInput == "-r":
                self.removePlayer()
            else:
                input('\n*** Incorrect Key, try again ***')
                continue

            print(formattedContent(
                label="Player List",
                content=self.nameOnlyContent()
            ))
            break


    def getPlayer(self):
        while True:
            print(formattedContent(
                label="Get Player",
                content= self.nameSelectionContent()
            ))

            userInput = input(f'Select an option (0 - {len(self.nameSelectionContent()) - 1}): ')
            try:
                index = int(userInput)
                player = self.all[index]
            except:
                input('\n*** Incorrect Key, try again ***')
                continue

            return player


    def changePlayerName(self):
        player = self.getPlayer()
        player.changeName()

    def changePlayerScore(self):
        player = self.getPlayer()
        player.changeScore()

    def changePlayerCashed(self):
        player = self.getPlayer()
        player.changeCashedStatus()

    def removePlayer(self):
        player = self.getPlayer()
        for i, game_player in enumerate(self.all):
            if game_player.name == player.name:
                del self.all[i]
                return


    def roundReset(self):
        for p in self.all:
            p.cashed = False

    def gameReset(self):
        for p in self.all:
            p.cashed = False
            p.score = 0

    def allCashed(self):
        for p in self.all:
            if not p.cashed:
                return False
        return True

    def cashOut(self, name, amount):
        cashed = False
        for p in self.all:
            if p.name == name.capitalize():
                if p.cashed:
                    input(f"\n*** {p.name} has already cashed out ***")
                    return
                else:
                    p.score += amount
                    p.cashed = True
                    cashed = True
                    break

        if not cashed:
            input("Player not recognized")

        print(f"\t\t{p.name}: {p.score}")


