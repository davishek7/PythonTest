def prime_test(x,y):

    for i in range(x,y+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
    return(i)
                 
def main():

    lower=int(input("Enter the lower range"))
    upper=int(input("Enter the upper range"))
    prime_test(lower,upper)

if __name__=='__main__':
    main()               