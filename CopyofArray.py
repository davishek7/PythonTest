from numpy import *

arr1=array([1,2,5,9])
arr2=arr1
print(arr2)
print(id(arr1))
print(id(arr2))

arr3=array([2,9,8,6])
arr4=arr3.view()
print(arr4)
print(id(arr3))
print(id(arr4))

arr3[2]=7
print(arr3)
print(arr4)


arr5=([6,9,8,3])
arr6=arr5.copy()
print(arr6)
print(id(arr5))
print(id(arr6))

arr5[2]=7
print(arr5)
print(arr6)
