def fib(n):
    a=0
    b=1
    if n<=0:
        print("Please enter value greater than 0")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

def main():
    x=int(input("Enter the fibonacci range: "))
    fib(x)

if __name__=='__main__':
    main()