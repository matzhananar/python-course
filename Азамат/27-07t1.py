class Tomato:
    states = {
        0: "Отсутствует",
        1: "Цветение",
        2: "Зеленый",
        3: "Красный"
    }

    def __init__(self, index):
        self.index = index
        self.state = 0
    
    def grow(self):
        if self.state<3:
            self.state +=1
        print(self.state)
    
    def isRipe(self):
        if self.state == 3:
            return True
        return False

class TomatoBush:
    def __init__(self,num):
        self.tomatoes = [Tomato(index) for index in range(0, num-1)]
    
    def growAll(self):
        for x in self.tomatoes:
            x.grow()
    
    def ripeAll(self):
        for x in self.tomatoes:
            if x.isRipe() == True:
                return True
        return False
    
    def giveAway(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant
    
    def work(self):
        self.plant.growAll()

    def harvest(self):
        if self.plant.ripeAll():
            self.plant.giveAway()
        else:
            self.plant.growAll()
    @staticmethod
    def knowledge_base():
        print("Это сад здесь есть томаты и садовник должен собрать урожай")

tomat1 = Tomato(1)
tomat2 = Tomato(0)
bush1 = TomatoBush(2)
gard1 = Gardener("Asyl", tomat1)

print(gard1.harvest())
print(tomat1.isRipe())
print(gard1.harvest())
print(tomat1.isRipe())