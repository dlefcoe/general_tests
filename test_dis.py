# python code runs faster inside a function !

import dis

def my_function():
    ''' this is a function '''

    for i in range(100):
        print(i)


    return

dis.dis(my_function)

'''

the reason for this is because the variables are local and they load fast.
as opposed to global vaiables which load slower.

'''
