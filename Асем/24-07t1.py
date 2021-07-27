class Tomato:
    def __init__(self, index, level):
        self.index = index
        self.level = level

    def grow(self):
        self.index += 1
        return self.index
    
    def getLevel(self):
        if self.index == 0:
            return "Отсуствует"
        elif self.index ==1:
            return "Цветение"
        elif self.index == 2:
            return "Зеленый"
        else:
            return "Красный"

tom1 = Tomato(2, "Зеленый")
print(tom1.getLevel())

print(tom1.grow())
print(tom1.getLevel())
