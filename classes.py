class point ():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def position(self):
        return (self.x,self.y)


p1 = point(3, 4)
print(p1.position())
