def div(a,b):
    return(a/b)

def smart_div(func):                     #it will take a function as an argument
    def inner(a,b):                      #there will be another inner function which will have same number of argument as the base function
        
        print("Now I am going to divide",a,"by",b)
        if b==0:
            print("Sorry can't be divided by 0")
            return                       #it will return None and will stop excute the block
        return func(a,b)
    return inner

def main():

    div1=smart_div(div)
    a=int(input("Enter a value: "))
    b=int(input("Enter another value: "))

    div1(a,b)

if __name__=='__main__':
    main()