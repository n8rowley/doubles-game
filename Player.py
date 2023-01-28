class Player:
    def __init__(self, name):
        self.name = name.strip().lower().capitalize()
        self.score = 0
        self.cashed = False

    def __len__(self):
        return self.score

    def changeName(self):
        self.name = input("\nEnter new name: ").strip().lower().capitalize()

    def changeScore(self): 
        while True:
            try:
                self.score = int(input('\nNew score: '))
                return
            except:
                print("Input must be a whole number")
                continue
            
    def changeCashedStatus(self):
        print(f"\t{self.name} is {'NOT ' if self.cashed else ''}currently cashed out")
        userInput = input("\t\tChange status? (y/n): ")
        if userInput.strip().lower() == 'y':
            self.cashed = not self.cashed
    
