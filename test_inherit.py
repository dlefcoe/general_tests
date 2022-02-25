

class FirstClass:
    x = 1

    def __init__(self) -> None:
        ''' conctructor'''
        print('constructed')
        pass
    
    def grow_x(self):
        self.x = self.x + 1

    
class SecondClass(FirstClass):

    def double_grow_x(self):
        self.x = self.x + 2


# instantiate firstclass
f = FirstClass()
print(f.x)
f.grow_x()
print(f.x)

# instantiate second class
g = SecondClass()
print(g.x)
g.grow_x() # method from the first class (inherited)
print(g.x)
g.double_grow_x() # method from the second class
print(g.x)



