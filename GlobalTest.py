a=10
b=15
print(id(a))
print(id(b))
def test():
    a=15
    print(id(a))
    print("Local Variable a: ",a)
    x=globals()['a']
    globals()['a']=17
    print(id(x))
    print("Global variable a Inside: ",x)
    global b
    b=12
    print("Global variable b inside: ",b)

test()

print("Global variable a Outside: ",a)
print("Global variable b outside: ",b)