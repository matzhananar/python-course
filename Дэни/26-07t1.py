class Tomato:
    def __init__(self, index):
        self.index = index
        self.stages = {0:"Отсутствует", 1:"Цветение" , 2: "Зеленый", 3:"Красный"}
    
    def grow(self):
        self.index +=1
        return self.index
    
    def getStage(self):
        return self.stages[self.index]

class koost:
    def __init__(self,kol):
        self.number = (Tomato(kol) for kol in range(0, kol))
    
    def grow(self):
        self.number += 1
    
    def getStage()
        

t1 = Tomato(1)
print(t1.getStage())