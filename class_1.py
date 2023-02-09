class stringer:
    def __init__(self, string):
       self.string = string
    def getString(self):
        self.string = str(input())
    def printString(self):
        print(self.string.upper())
s=stringer
s.getString(s)
s.printString(s)