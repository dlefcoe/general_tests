

import pandas as pd
d = {'sex':['male','female','female','female','female'], 'smoke':[1,0,0,0,0], 'hello':[1,2,3,4,5]}

df = pd.DataFrame(d)

def some_test(sex, b):
    ''' some generic fnction'''
    if b<100:
        pass
    else:
        return 10

    if sex == 'male':
        return 1
    else:
        return 0


# example of how to convert sex from string to numeric
df['new'] = df.apply(lambda r: some_test(r['sex'],r['hello']) ,axis=1)
print(df)

c = df[['new','smoke']].corr()
print(c)

