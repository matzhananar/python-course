class Tomato:
    states = {0:"Отсутствует", 1: "Цветение", 2:" Зеленый", 3:"Красный"}
    def __init__(self, index, state):
        self.index = index
        self.state = 0
    
    def grow(self):
        if self.state<3:
            self.state += 1
        print("tomotoes are growing")

    def isRipe(self):
        if self.state ==3:
            return True
        else:
            return False

class TomatoBush:
    def __init__(self, nums):
        self.tomatoes = [Tomato(index) for index in range(0,nums-1)]
    
    def growAll(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def allRipe(self):
        for tomato in self.tomatoes:
            if tomato.isRipe == False:
                return False
            else:
                return True
    def giveAway(self):
        self.tomatoes = []

class Gardener:
    def __init__(self,name, plant):
        self.name = name
        self.plant = plant

    def work(self):
        print("Gardener is working")
        self.plant.growAll()

    def harvest(self):
        if self.plant.allRipe():
            self.plant.giveAway()
    
    @staticmethod
    def base():
        print("Это сад из томатов и здесь есть садовник")

Gardener.base()       

bush1 = TomatoBush(4)
gard1 = Gardener("Asyl",bush1)
gard1.work()
