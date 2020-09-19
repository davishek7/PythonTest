from numpy import *

# Matrix using a 2D array
arr1=array([
    [1,2,3,4],
    [5,6,7,8]
])
m1=matrix(arr1)
print(m1)

# Matrix without an array
m2=matrix('1 2 3; 4 5 6 ;7 8 9')             # ; is used for rows
print(m2)

print(diagonal(m2))                         # printing the diagonal values of the matrix

# Multiplication of 2 Matrices
m3=matrix('2 3 5;5 6 7;4 8 9')
m4=m2*m3
print(m4)

# Addition of 2 Matrices
m5=m2+m3
print(m5)