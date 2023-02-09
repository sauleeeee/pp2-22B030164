class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0 ):
        self.length  = length
    
    def area (self) :
        print(self.length * self.length)        


class Rectangle(Shape):

    def __init__(self,  width):
        self.width = width

    def area (self, w):
        print( self.length  * w) 

sq = Square
sh =Shape
r = Rectangle
len = 8
w = 5
t = sq(len)
sh.area(t)
r.area(t,w)