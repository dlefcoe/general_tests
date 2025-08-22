import pandas as pd

# create a dataframe
d = {'a':[1,2,3,4,5,6,7,8], 'b':[2,4,6,8,10,12,14,16]}
df=pd.DataFrame(d)

# add moving avg column
df['moving av'] = df['b'].rolling(3).mean()

# cumulative sum
df['cumulative'] = df['b'].cumsum()


print(df)
