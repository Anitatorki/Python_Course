# Example of for in Python
_list = [3, 6, 7, 1,2,3,0]
for i in _list:
    print(i)

# Example of for in Python (String)
_str = "Hello World"
for i in _str:
    print(i)


# Example of for in Python (range)
for i in range(1, 10):
    print(i)

# Example of for in Python (list)
_list = [3, 6, 7, 1,2,3,0]
for i in _list:
    i+=2
print(_list)


for i in range(len(_list)):
    _list[i]+=2
print(_list)