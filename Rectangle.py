def perimeter(x,y):
    z=2*(x+y)
    return(z)

def area(x,y):
    z=x*y
    return(z)

def main():
    print('Enter the reuired values')
    length=int(input('Enter the length'))
    breadth=int(input('Enter the breadth'))
    result1=perimeter(length,breadth)
    print(result1)
    result2=area(length,breadth)
    print(result2)
    
if __name__=='__main__':
    main()