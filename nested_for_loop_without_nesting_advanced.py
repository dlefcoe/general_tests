'''
Example of how to nest a for loop, but by using a function
in place of the nested for loop.

This has the result of keeping the level of indentation lower.

The result is a list of dicts which looks like this:
[{},
 {0: 1},
 {0: 2, 1: 2},
 {0: 3, 1: 3, 2: 3},
 {0: 4, 1: 4, 2: 4, 3: 4},
 {0: 5, 1: 5, 2: 5, 3: 5, 4: 5},
 {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6},
 {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7},
 {0: 8, 1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8},
 {0: 9, 1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 9, 8: 9}]

Can this be extended to 3 levels or even n-levels ?

'''

__author__ = 'dlefcoe'

# imports
import pprint

def main():
    ''' main entry point for the code '''

    res = outer_for()
    pprint.pp(res)
    print('---')

    res = inner_for(9)
    pprint.pp(res)

    return


def outer_for():
    ''' the outer for loop '''
    ans = []
    for i in range(10):
        res = inner_for(i)
        ans.append(res)
    
    return ans



def inner_for(i):
    d = {}
    for j in range(i):
        d[j] = i
    return d



# main guard idiom
if __name__=='__main__':
    main()
