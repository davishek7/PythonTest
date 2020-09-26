"""
Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, 
and returns a list consisting of the first elment in l1, then the first element in l2, 
then the second element in l2, then the second element in l2, and so on. If the two lists 
are not of equal length, the remaining elements of the longer list are appended 
at the end of the shuffled output.
"""
def shuffle(l1,l2):
    l3=[]

    a1=len(l1)
    a2=len(l2)

    for i in range(max(a1,a2)):
        if i<a1:
            l3.append(l1[i])
        if i<a2:
            l3.append(l2[i])

    return l3

l1=[0]
l2=[1,3,5]

result=shuffle(l1,l2)
print(result)