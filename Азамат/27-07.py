class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def getWidth(self):
        return self.width

    def getLength(self):
        return self.length
    
    def getArea(self):
        return self.width *self.length

rec1 = Rectangle(5, 15)
print(rec1.getWidth())
print(rec1.getArea())