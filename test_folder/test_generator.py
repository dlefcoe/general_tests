'''
generator function operations in python
(generators are iterators).

we use three methods:
  1. using the next() function to traverse the generator
  2. using a simple for loop
  3. generator expression (like list comprehension)

the simple for loop is much better.

author: darren lefcoe
'''



def main():
    ''' the main module '''

    # use_generator_method_1()
    use_generator_method_2()

    # method 3 - generator expression
    result = (n for n in range(10) if n%2 == 0)
    print(type(result))
    for i in result:
        print(i)



def use_generator_method_1():
    ''' this is a function to use the generator (method 1) 
    
    this method uses the next() operator
    '''

    result = my_generator(10)
    

    print('the next result:')

    # loop through result until last item is retrieved
    while True:
        try:
            value = next(result)
            print(value)
        except StopIteration:
            break


def use_generator_method_2():
    ''' this is a function to use the generator (method 2)
    
    this method uses a simple for loop
    '''

    result = my_generator(10)
    print(type(result))

    # we could do this...
    for number in result:
        print(number)  


def my_generator(n: int) -> int:
    ''' this is a generator function 
    
    args:
        n (int): to number to count up to.

    return:
        generates a list of numbers up to n.
    '''
    
    i = 0
    while i <= n:
        yield i

        i += 2


if __name__ == '__main__':
    main()


