

string_input = 'hello world'

print(string_input)

# string_as_bytes = string_input.bytes
string_as_bytes = string_input.encode('utf-8')
print(string_as_bytes)

string_as_bytes = string_input.encode('utf-16')
print(string_as_bytes)


string_as_bytes = string_input.encode('utf-32')
print(string_as_bytes)


x = '蓏콯캁澽苏'
print(x)
y = x.encode()
print(y)
z1 = y.decode('utf-8')
print(z1)



