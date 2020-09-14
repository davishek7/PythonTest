a=int(input('enter a number'))
b=int(input('enter another number'))
if a>b:
    c=a-b
    print('a is greater than b')
    print(c)
elif a==b:
    print('a & b are both equal')
    c=a-b
    print(c)
else:
    c=b-a
    print('b is greater than a')
    print(c)