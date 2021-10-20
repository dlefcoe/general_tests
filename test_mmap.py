

'''
This code reads the entire file into physical memory, if there’s enough available at runtime, and prints it to the screen.

This type of file I/O is something you may have learned early on in your Python journey.
The code isn’t very dense or complicated.
However, what’s happening under the covers of function calls like read() is very complicated.
Remember that Python is a high-level programming language, so much of the complexity can be hidden from the programmer.

'''

import time
import mmap


f = r'C:\darren\python\test\hello_world.txt'


def main():
    t0 = time.time()
    regular_io_write(f)
    t1 = time.time()
    print('time taken to write:', round(t1-t0, 6), 'seconds')

    t2 = time.time()    
    regular_io_read(f)
    t3 = time.time()
    print('time taken to read (standard):', round(t3-t2, 6), 'seconds')
    m = t3-t2

    t4 = time.time()
    mmap_io_read(f)
    t5 = time.time()
    print('time taken to read (m_map):', round(t5-t4, 6), 'seconds')
    n = t5-t4

    print()
    print('times better:', round(m/n, ndigits=5)  )


def regular_io_write(filename):
    with open(filename, mode="w", encoding="utf8") as file_obj:
        text = file_obj.write('hello world')
        print('file written')


def regular_io_read(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()
        print(text)



'''

One way to avoid this overhead is to use a memory-mapped file.

You can picture memory mapping as a process in which read and write operations skip 
many of the layers mentioned above and map the requested data directly into physical memory.

A memory-mapped file I/O approach sacrifices memory usage for speed, which is classically called the space–time tradeoff.

'''

# Here’s the memory-mapping equivalent of the file I/O code you saw before:

def mmap_io_read(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()
            print(text)



'''

The API provided by Python’s mmap file object is very similar to the traditional file object except for one additional superpower:
Python’s mmap file object can be sliced just like string objects!

'''


# entry point hoisting
if __name__ == '__main__':
    main()



