

from numpy.testing._private.utils import print_assert_equal
import pandas as pd
import json
import pprint


d = {
    'a':[5,3,2,  4,5, 6, 7, 8, 1,2,3, 5,3,2,4,5, 6, 7, 8, 1,2,3],
    'b':[50,30,20,40,50, 60,70,80,100,200,300, 50,30,20,40,50, 60,70,80,100,200,300]
}

df = pd.DataFrame(d)
print(df)

pprint.pp(df)



print(d)
pprint.pp(d, indent=4)

printable_string = json.dumps(d, indent=4)
print(printable_string)


print(df.to_string(justify='right'))

table = df.to_markdown()
print(table)

print(type(table))

