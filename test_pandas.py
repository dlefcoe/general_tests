


import pandas as pd



mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
df = pd.DataFrame(mydict)
print(df)
print('\n\n')

df['a'][2] = 'test'
print(df['a'][2])

print (df)



# testing concat
print('\n\n--- testing concat ---\n ')
# s1 = pd.DataFrame([['a',1.2], ['b',2.1], ['c',3.1]], columns=['letters', 'numbers'])
# s2 = pd.DataFrame([['a',1.5], ['f',2.5], ['c',5.5]], columns=['letters', 'numbers'])
# s3 = pd.concat([s1, s2])

# print(s3)
# print('\nconcat ignore index')
# s4 = pd.concat([s1, s2], ignore_index=True)
# print(s4)

# print('\nsummary:')

# s3_grouped = s3.groupby(['letters'])['numbers']#.agg('min', 'mean','sum')
# s4_grouped = s4.groupby(['letters'])['numbers']#.agg('min', 'mean','sum')
# #s3_grouped.reset_index()
# print(s3_grouped)
# print(s4_grouped)



df1 = pd.DataFrame([['a', 1], ['b', 2], ['c',3.5], [20,5]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3, 1], ['d', 4,1], ['e',3,1], ['20',5.2,1]], columns=['letter', 'number', 'number2'])

df3 = pd.concat([df1, df2])


print(df3)

df3_group = pd.DataFrame(df3.groupby('letter')['number'].agg(['min','mean'])).reset_index()
print(df3_group)



# dataframe to string
print('\ndataframe to string')

d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(d)

print(df)

df['col2'] = df['col2'].astype(str)
print(df)
print(type(df['col2'][0]))


print(df)





# example of adding a column based on values of other columns

d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(d)



def calc_new_column(row:object):
    ''' creates new column based on values from other columns
    
    args:
        row: the rows of a pandas dataframe
    
    return: value that goes into each row of the new coulmn of the dataframe

    '''
    # print(type(row))

    if int(row['col1']) > 1:
        if int(row['col2']) <= 5:
            return 'in range'
    return 'out range'

# the new column
df['col3'] = df.apply(calc_new_column, axis=1)


print(df)

