def count(lst):

    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
        
def main():

    lst=[]
    n=int(input("enter the number of values you want to add"))

    for i in range (n):
        x=int(input("enter the next value"))
        lst.append(x)
    print("List: ",lst)

    even,odd=count(lst)
    print(even)
    print(odd)

    print("Even:{} and Odd:{}".format(even,odd))

    """
    Python window will continue to run
    
    while True:
        pass
    """

if __name__=='__main__':
    main()