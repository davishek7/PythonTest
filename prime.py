x=int(input('Enter a number '))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print('Not a Prime number')
            break
    else:
        print('Prime number')