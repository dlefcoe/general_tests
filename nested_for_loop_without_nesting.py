'''
Example of how to nest a for loop, but by using a function
in place of the nested for loop.

This has the result of keeping the level of indentation lower.

Can this be extended to 3 levels or even n-levels ?

'''

__author__ = 'dlefcoe'


def main():
    ''' main entry point for the code '''

    for i in range(10):
        inner_for(i)

    return



def inner_for(i):
    for j in range(i):
        print(i, j)
    return



# main guard idiom
if __name__=='__main__':
    main()


