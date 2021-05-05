'''

this is in the first subfolder

'''


# import modules
import os
import sys


# import files from the sub directories
import folder_A.code_A as aa


# append system path so that module from parent directory can be imported
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# print()
# print('the system path:')
# print(sys.path)


# import modules from parent directory
import base_code

print()
print('this is from the parent:')
print(base_code.x)

print()
print('this is from the child:')
print(aa.p)



