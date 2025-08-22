'''

example of valid docstring syntax

looks like it uses a lot of markdown syntax

here is a markdown cheatsheet:
https://www.markdownguide.org/cheat-sheet/

'''


def adddd(x: int, y: int) -> int:
    '''Returns the `sum` of x and y.
    
    parameters
    --- 
    args:
        x (int): .
        y (int): .
    
     - a
     - b
     - c


    # the main bit
    ## second header
    ### third header 
    #### 4th header
    
    
    ```
    "firstName": "John",
    "lastName": "Smith",
    "age": 25
    ```

    >>>  tih sis a block quote
    https://www.example.com

    '''
    return x + y

adddd()
