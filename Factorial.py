def fact(n):
    f=1
    if n==0:
        return 1
    for i in range (1,n+1):
        f=f*i
    return f

def main():
    x=int(input("Enter the number: "))
    result=fact(x)
    print(result)

if __name__=='__main__':
    main()