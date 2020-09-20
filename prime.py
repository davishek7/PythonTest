def prime(x):
    for i in range(2,x):
        if x%i==0:
            print('Not a Prime number')
            break
    else:
        print('Prime number')
    return(x)
def main():
    a=int(input('Enter a number '))
    if a>1:
        prime(a)
    else:
        print("Enter a value greater than 1")
if __name__=='__main__':
    main()