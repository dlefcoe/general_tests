# imports go here
import numpy as np
import random


class MyArrayClass:

    def __init__(self, size: int, datatype: str) -> None:
        self.size = size
        self.datatype = datatype



def main():
    """main entry point for the code"""
    make_array()
    make_random_array(8)
    the_book()

    return


def make_array(len_of_array=6) -> None:
    """function to make a numpy array"""
    a = np.array([1, 2, 3, 4, 5])
    b = np.zeros(len_of_array, dtype="int8")
    print(a)
    print(b)


def the_book() -> None:
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a.shape)
    print(a.ndim)
    print(a.dtype)
    print("the value of element [1,1] is . . . ", a[1, 1])

    print(np.__version__)


def make_random_array(len_of_array=10) -> int:
    """function to make a numpy array of random numbers"""
    a = np.random.randint(0, 100, len_of_array)
    print(a)

    # make a list of random numbers not using numpy
    random_numer = random.random()
    print(random_numer)

    return random_numer


# main guard idiom
if __name__ == "__main__":
    main()
