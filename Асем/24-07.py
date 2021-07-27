class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self. height = height
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        return self.height * self.width

rect1 = Rectangle(10,5)
print(rect1.width)
print(rect1.height)
print(rect1.getArea())