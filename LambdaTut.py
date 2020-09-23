from functools import reduce
def main():

    nums=[]
    n=int(input("How many numbers do you want to add: "))

    for i in range(n):
        x=int(input("Enter the next value: "))
        nums.append(x)
    print(nums)

    evens=list(filter(lambda n:n%2==0,nums))
    print(evens)

    doubles=list(map(lambda n:n*2,evens))
    print(doubles)

    sum=reduce(lambda a,b:a+b,doubles)
    print(sum)


if __name__=='__main__':
    main()