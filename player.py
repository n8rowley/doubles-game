"""Player class"""
class Player:
    def __init__(self, name):
        self.__name = name.lower()
        self.score = 0

    def get_name(self):
        return self.__name.capitalize()

    def __len__(self):
        return self.score

    def __repr__(self):
        return self.get_name()

    def __str__(self):
        return self.get_name()


"""Collection of players class"""
class PlayerCollection:
    def __init__(self):
        self.p = []
        self.i = 0
        self.i_n = 0

    def add(self, player):
        self.p.append(player)
        self.sort()
        self.i_n = len(self.p)

    def remove(self, player):
        self.p.remove(Player(player.get_name()))
        

    def sort(self):
        self.p = sorted(self.p, key=len, reverse=True)





    '''Iterator methods'''

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.i_n:
            self.i = 0
            raise StopIteration()
        else:
            current_i = self.i
            self.i += 1
        return current_i

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "Players: " + ", ".join([str(item) for item in self.p])

if __name__ == "__main__":
    c = PlayerCollection()
    c.add(Player('nate'))
    c.add(Player('molly'))

