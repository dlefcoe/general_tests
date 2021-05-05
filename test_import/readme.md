# python imports from the parent folder
In python 3, it is not possible to import from the parent folders without one of two options.

1. use the environment variable PYTHONPATH
2. append system path so that module from parent directory can be imported

This example uses method 2 which means that it can be used in the modules itself.



## python imports from the sibling folders
Sibling folders use the same method

## grandparent folders
There is an example for 2 parents up in this structure. 
Basically the user needs to add one extra line to get a second level up.



### conclusion
Although this solution is a bit hacky and it is recommended to not meddle with sys.path programmatically, it does get the job done when we have no other choice in Python but to import from parent directory using sys path. Using the os and sys module in Python gives us a way to go up a layer or two.



### useful links
https://codeolives.com/2020/01/10/python-reference-module-in-parent-directory/comment-page-1/?unapproved=789&moderation-hash=cbc3a4a424f32e835b4f5198b0570d72#comment-789

