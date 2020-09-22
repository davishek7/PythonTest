def count(lst):

    more=0
    less=0

    for i in lst:
        if len(i)>=5:
            more+=1
        else:
            less+=1

    return more,less

def main():
    lst=[]
    n=int(input("How many names do you want to add? : "))

    for i in range(n):
        x=input("Enter the next name: ")
        lst.append(x)
    print(lst)
    more,less=count(lst)
    print(more)
    print(less)
    print("Names with more than 5 characters: {} and Names with less than 5 characters: {}".format(more,less))

if __name__=='__main__':
    main()
