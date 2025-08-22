# %%

# passing arguments into a function
# [1] by value and [2] by reference
# [1] immutable and [2] mutable

# immutable data type (by value)
def function(a:int):
    ''' the function doc string '''
    a = 20
    print('inside the function (a)', a)
    print('memory location inside function (a)', id(a))
    return

a = 10
function(a)

print('outside the function (a)',a)
print('memory location outside function (a)', id(a))


print('---------------------')

# mutable data type (by reference)
def function(b:list):
    ''' the function doc string '''
    b.append(40)
    print('inside the function (b)', b)
    print('memory location inside function (b)', id(b))

    b = [1, 2, 3]
    print('inside the function (b)', b)
    print('memory location inside function (b)', id(b))

    b.append(50)
    print('inside the function (b)', b)
    print('memory location inside function (b)', id(b))

    b = [1000, 2000, 3000]
    print('inside the function (b)', b)
    print('memory location inside function (b)', id(b))

    return

b = [10, 20, 30]
function(b)

print('outside the function (b)',b)
print('memory location outside function (b)', id(b))