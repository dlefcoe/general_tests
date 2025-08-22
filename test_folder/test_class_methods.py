class MyClass:
    ''' description of the class '''
    
    def __init__(self, a:int, b:int|None = None):
        '''
        initialise the class:

        args:
            a: the first number
            b: the second number 
        
        '''
        self.a = a
        self.b = b
        return
    
    def __add__(self, other=10):
        ''' add number '''
        r = self.a + other.b
        return r

    def __sub__(self, other=10):
        ''' add number '''
        r = self.a - other.a
        return r

    def __mul__(self, other=10):
        ''' multiply components and return a tuple '''
        r = (self.a * other.b, -self.b * other.a)
        return r
    
    # def __del__(self):
    #     print('we have deleted an instance')

    def __repr__(self) -> str:
        return f'MyClass(a={self.a}, b={self.b})'

    def __str__(self) -> str:
        return f'MyClass(a={self.a}, b={self.b}) - string'

    def my_print(self)->str:
        return f'MyClass(a={self.a}, b={self.b})'

    def __len__(self)->int:
        my_length = 0
        if self.a != None: my_length += 1
        if self.b != None: my_length += 1

        return my_length

    def __iter__(self):
        return iter([self.a, self.b])

a = MyClass(10, 20)

# %%   math operations
result = a + a
print('addition:', result)

result = a - a
print('subtraction:', result)

result = a * a
print('multiplication:', result)

# %% repr & len
print(a.__repr__())

print('the most pythonic way:')
print(a)

print(a.my_print())

# %% len
a = MyClass(100, 200)
b = MyClass(100)
print('the length of a:', len(a))
print('the length of b:', len(b))

# magic methods
# dunder methods  (double underscore)
# special methods / hidden methods / built-in methods
# representative of private functions 

# public, __private

# %%
x = 10
y = 20
print(type(x))

result = x + y    # Int(self=x, other=y)  __add__():
print(result)

# %% for loop

my_iterable = MyClass(100, 200)
for i in my_iterable:
    print(i)


'''
here is a useful link:
    https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html


Method | Description                                                                        used
------- | ------------------------------------------------------------------------------
commonly used
__new__ | Called to create a new instance of the class.
__init__ | Called after the instance is created.                                            yes
__del__ | Called when the instance is deleted.                                              yes
__repr__ | Called to get a string representation of the instance.                           yes
__str__ | Called to get a human-readable string representation of the instance.             yes
__getitem__ | Called to get an item from the instance.
__setitem__ | Called to set an item in the instance.
__delitem__ | Called to delete an item from the instance.
__len__ | Called to get the length of the instance.                                         yes
__iter__ | Called to get an iterator for the instance.                                      yes
__contains__ | Called to check if an item is in the instance.

math operators:
__add__ | Called to add two instances together.                                             math
__sub__ | Called to subtract two instances.                                                 math
__mul__ | Called to multiply two instances.                                                 math
__truediv__ | Called to divide two instances.                                               math
__floordiv__ | Called to divide two instances and return the floor of the result.           math
__mod__ | Called to modulo two instances.                                                   math
__divmod__ | Called to divide two instances and return a tuple of the quot and remainr.     math
__pow__ | Called to raise one instance to the power of another instance.                    math

logical operators:
__and__ | Called to bitwise and two instances.                                              logical
__or__ | Called to bitwise or two instances.                                                logical
__xor__ | Called to bitwise xor two instances.                                              logical

others:
__getattribute__ | Called to get an attribute from the instance.
__setattr__ | Called to set an attribute on the instance.
__delattr__ | Called to delete an attribute from the instance.
__call__ | Called to call the instance as a function.
__getstate__ | Called to get the state of the instance for pickling.
__setstate__ | Called to set the state of the instance from pickling.

missing:
__enter__
__exit__


'''

print('--- done ---')