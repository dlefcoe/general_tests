'''

this is the same level as folder A

'''



# import modules
import os
import sys




# append system path so that module from parent directory can be imported
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


# import from sibling folder
import folder_A.code_A as aa

print(aa.p)

