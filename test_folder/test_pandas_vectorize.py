'''

How to Speed Up Pandas Data Operations Using Vectorized Operations

'''

import pandas as pd
import numpy as np


# create some funciton to apply
def some_function(my_input, a_mean, a_stdev):

    result = (my_input-a_mean) / a_stdev
    return result


# make a dataframe
np.random.seed(42)
randmn_numbers_1 = np.random.randint(10e1, size=10_000)
randmn_numbers_2 = np.random.randint(10e2, size=10_000)
randmn_numbers_3 = np.random.randint(10e3, size=10_000)


df = pd.DataFrame(
    {'randmn_numbers_1':randmn_numbers_1,
    'randmn_numbers_2':randmn_numbers_2,
    'randmn_numbers_3':randmn_numbers_3}
)

print(df)


my_mean = df['randmn_numbers_2'].mean()
my_std = df['randmn_numbers_2'].std()

# this is called Vectorized Series
df['new column'] = some_function(df['randmn_numbers_2'], my_mean, my_std)

'''
Based on the definition given by the official Numpy documentation, 
vectorization is defined as being
 “able to delegate the task of performing mathematical operations on 
 the array’s contents to optimized, compiled C code.” 
 Instead of looping through rows, columns or elements, 
 this allows us to apply one set of instructions on multiple elements at the same time.
'''

print(df)

