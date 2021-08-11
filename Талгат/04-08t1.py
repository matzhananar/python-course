class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        print(self.width*self.height)
    
r1 = Rectangle(10,5)
print(r1.width)

r1.area()

r2 = Rectangle(20,3)
r2.area()