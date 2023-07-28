'''
Example of how to nest a for loop, but by using a function
in place of the nested for loop.

This has the result of keeping the level of indentation lower.

We can add a third level of nesting (so a 3d cube, like i,j,k).

The result is a list of lists of dicts which looks like this:
[[{}],
 [{}, {0: 1}],
 [{}, {0: 1}, {0: 2, 1: 2}],
 [{}, {0: 1}, {0: 2, 1: 2}, {0: 3, 1: 3, 2: 3}],
 [{}, {0: 1}, {0: 2, 1: 2}, {0: 3, 1: 3, 2: 3}, {0: 4, 1: 4, 2: 4, 3: 4}],
 [{},
  {0: 1},
  {0: 2, 1: 2},
  {0: 3, 1: 3, 2: 3},
  {0: 4, 1: 4, 2: 4, 3: 4},
  {0: 5, 1: 5, 2: 5, 3: 5, 4: 5}],
 [{},
  {0: 1},
  {0: 2, 1: 2},
  {0: 3, 1: 3, 2: 3},
  {0: 4, 1: 4, 2: 4, 3: 4},
  {0: 5, 1: 5, 2: 5, 3: 5, 4: 5},
  {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6}],
 [{},
  {0: 1},
  {0: 2, 1: 2},
  {0: 3, 1: 3, 2: 3},
  {0: 4, 1: 4, 2: 4, 3: 4},
  {0: 5, 1: 5, 2: 5, 3: 5, 4: 5},
  {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6},
  {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7}],
 [{},
  {0: 1},
  {0: 2, 1: 2},
  {0: 3, 1: 3, 2: 3},
  {0: 4, 1: 4, 2: 4, 3: 4},
  {0: 5, 1: 5, 2: 5, 3: 5, 4: 5},
  {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6},
  {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7},
  {0: 8, 1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8}],
 [{},
  {0: 1},
  {0: 2, 1: 2},
  {0: 3, 1: 3, 2: 3},
  {0: 4, 1: 4, 2: 4, 3: 4},
  {0: 5, 1: 5, 2: 5, 3: 5, 4: 5},
  {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6},
  {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7},
  {0: 8, 1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8},
  {0: 9, 1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 9, 8: 9}]]

Can this be extended to n-levels ?
n-dimension nesting...
it looks a bit recursive, so be careful.

'''



# imports
import pprint


def main():
    ''' main entry point for the code '''

    res = outer_for(11)
    print('result of the nested for loop:')
    pprint.pp(res)

    # nested_for_loop()

    return


def nested_for_loop():
    ''' create and run a nested for loop '''
    
    for i in range(10):
        for j in range(i):
            print(i, j)

    return


def outer_for(n):
    ''' the outer for loop '''

    ans = []
    for i in range(1, n):
        res = inner_for(i)
        ans.append(res)
    return ans


def inner_for(i):
    ''' the inner for loop, loops to i'''
    ans = []
    for j in range(i):
        res = double_inner_for(j)
        ans.append(res)
    return ans


def double_inner_for(j):
    d = {}
    for k in range(j):
            d[k] = j
    return d


# main guard idiom
if __name__=='__main__':
    main()
