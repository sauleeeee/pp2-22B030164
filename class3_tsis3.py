import math

class point:
    def __init__(self, x = 5  , y = 9 ):
        self.x  = x
        self.y  = y

    def show(self):
        print(f'{self.x}'+ ' '+ f'{self.y}')

    def move(self, x , y):
        self.x = x
        self.y = y
        print('New coor:',self.x,self.y)

    def dist(self,x,y):
        d = math.sqrt(pow((self.x - x),2) + pow((self.y - y),2))
        print(d)

# p = point()
# p.show()

# p.move(7 , 8)

# k = point(1 , 1)

# k.show()
# p.show()

# p.dist(5,9)