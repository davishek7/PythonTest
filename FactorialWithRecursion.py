def fact(n):

    f=1
    if n==0:
        return 1
    for i in range(1,n+1):
        f=n*fact(n-1)
    return f

def main():

    x=int(input("Enter the number: "))
    print("The Factorial of {} is: {}".format(x,fact(x)))

if __name__=='__main__':
    main()




