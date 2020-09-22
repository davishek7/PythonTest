def person(name,age):                      #Position Argument
    print(name)
    print(age)

def details(name,age=18):                  #Default Argument
    print(name)
    print(age)

def sum(a,*b):                             #Variable Length Argument with one position argument
    c=a
    for i in b:
        c=c+i
    print(c)

def add(*b):                               #variable length argument with no position argument
    c=0
    for i in b:
        c=c+i
    print(c)

def user(name,**kw):                       #Keyworded Variable argument
    print(name,kw)
    for i,j in kw.items():
        print(i,j)

def main():

    person('avishek',24)

    details('avishek')

    user('avishek',age=24,mob=1234)

    sum(5,12,36,78)
    
    add(1,3,5,6)
    
if __name__ == "__main__":
    main()

