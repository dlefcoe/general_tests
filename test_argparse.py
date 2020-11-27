'''
https://docs.python.org/3/library/argparse.html

usage (in the command line):
    py test_argparse.py -h
    py test_argparse.py 1 2 3 4
    py test_argparse.py 1 2 3 4 --sum

'''


import argparse

# create the object
parser = argparse.ArgumentParser(description='Process some integers.')

# add arguments
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

# add another arguments
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# parsing arguments
args = parser.parse_args(['--sum', '4', '4', '10'])
print(args.accumulate(args.integers))


# parsing arguments in a different order does not make a difference
args = parser.parse_args(['20', '4', '4', '10', '--sum'])
print(args.accumulate(args.integers))

# parsing arguments
args = parser.parse_args(['20', '4', '4', '10'])
print(args.accumulate(args.integers))

