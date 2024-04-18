#Give 2 number from user and print the range of number (Even number)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x>y:
    x,y = y,x

if x%2:
    x+=1


print(list(range(x,y,2)))