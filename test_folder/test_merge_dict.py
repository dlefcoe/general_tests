
from tkinter import Y


d = {'a':1, 'b':10, 'c':20}
e = {'p':1, 'b':1, 'r':3}

# note that for any joint keys, the second dict values take preferance 
d.update(e)

print(d)



d = {'a':1, 'b':10, 'c':20}
e = {'p':1, 'b':1, 'r':3}

# a new dict from the union of d and e
z = d|e

print(z)

