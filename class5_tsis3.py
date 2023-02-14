class Account:
    def __init__(self, name  , balance = 0 ):
        self.name  = name
        self.balance  = balance

    def plus(self,add):
        self.balance = self.balance+add
        print('balance of',self.name,':',self.balance)

    def denote(self,min):
        if min > self.balance:
            print("nehvatka")
        else:
            self.balance = self.balance - min
            print('balance of',self.name,':',self.balance)



f = Account('Saule',200)
f.plus(50)
f.denote(251)
s = Account('Aisha', 50)
s.plus(1000)
s.denote(500)