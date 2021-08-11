class Tomato:
    states  = {0: "none", 1: "цветение", 2:"зеленый", 3:"красный"}
    def __init__(self, index):
        self.index = index
        self.state = 0
    
    def grow(self):
        if self.state <3:
            self.state+=1
        print(f"Tomato {self.index} is {Tomato.states[self.state]}")
    
    def isRipe(self):
        if self.state == 3:
            return True
        else:
            return False

class TomatoBush:
    def __init__(self,num):
        self.tomatoes = [Tomato(index) for index in range(0,num)]
    
    def growAll(self):
        for tomato in self.tomatoes:
            tomato.grow()
    
    def allRipe(self):
        for tomato in self.tomatoes:
            if tomato.isRipe():
                return True
            else:
                False
        
    def giveAwayAll(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant
    
    def work(self):
        print("gardener is working")
        self.plant.growAll()
    
    def harvest(self):
        if self.plant.allRipe():
            self.plant.harvest()
        else:
            print("your tomatoes aren't ripe")
    
    @staticmethod
    def base():
        print("""It is a garden where gardener
is working on tomatoes""")
    

Gardener.base()
bush1 = TomatoBush(4)
gard1 = Gardener("Ali",bush1)
gard1.work()
gard1.harvest()
