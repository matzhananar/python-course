class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}
    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        self.changeState()

    def isRipe(self):
        if self.state == 3:
            return True
        return False
    
    def changeState(self):
        if self.state<3:
            self.state+=1
        self.getState()

    def getState(self):
        print(f'Tomato {self.index} is {Tomato.states[self.state]}')
    

class TomatoBush:
    def __init__(self,num):
        self.tomatoes = [Tomato(index) for index in range(0,num-1)]
    
    def allgrow(self):
        for tomato in self.tomatoes:
            tomato.grow()
    
    def allRipe(self):
        return all([tomato.isRipe for tomato in self.tomatoes])
    
    def getAll(self):
        self.tomatoes =[]

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant
    
    def work(self):
        print("Gardener is working...")
        self.plant.getAll
