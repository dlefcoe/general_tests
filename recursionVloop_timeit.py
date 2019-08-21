'''

function to call itself to count to 10
do this by recursion and not a for loop

'''

import timeit as tt
import numpy as np


# recursive function
def rec(n):

    if n < 100:
        # print('keep going', n)
        rec(n+1)
    else:
        # print('REC ended here', n)
        pass
        return 1

    return 1



# loop method
def loo(n):

    for i in range(n, 100):
        # print('keep going',i)
        i = i * 2
        pass
    # print('LOO ended here', i)

    return 1


# numpy loop method
def npl(n):

    for i in np.arange(n,100):
        i = i * 2
        pass
    return 1




x = tt.timeit('rec(0)',number=10000, globals=globals())
y = tt.timeit('loo(0)',number=10000, globals=globals())
z = tt.timeit('npl(0)',number=10000, globals=globals())

print('the timeit function for REC gets',x)
print('the timeit function for LOO gets',y)
print('the timeit function for NPL gets',z)












