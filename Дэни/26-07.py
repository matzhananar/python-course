class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def getArea(self):
        return self.width *self.length
    
    def getWidth(self):
        return self.width
    def getLength(self):
        return self.length

rect1 = Rectangle(10,5)
print(rect1.getArea())
print(rect1.getLength())
print(rect1.getWidth())