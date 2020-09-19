def add(x,y):
    z=x+y
    return(z)

def sub(x,y):
    z=x-y
    return(z)

def main():
    a=int(input('enter a number'))
    b=int(input('enter another number'))
    result1=add(a,b)
    print(result1)

    c=int(input('enter a number'))
    d=int(input('enter another number'))
    result2=sub(c,d)
    print(result2)

if __name__=='__main__':
    main()