lower=int(input('Enter the lower range'))
upper=int(input('Enter the upper range'))

for x in range(lower,upper):
    if x>1:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            print(x)