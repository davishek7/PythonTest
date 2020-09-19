from numpy import *

arr1=array([
    [1,2,3,7,8,9],
    [4,5,6,3,2,1]
])

arr2=arr1.flatten()
print(arr2)

arr3=arr2.reshape(3,4)
arr4=arr2.reshape(2,2,3)
print(arr3)
print(arr4)

print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

print(arr2.ndim)
print(arr2.shape)
print(arr2.size)

print(arr3.ndim)
print(arr3.shape)
print(arr3.size)

print(arr4.ndim)
print(arr4.shape)
print(arr4.size)