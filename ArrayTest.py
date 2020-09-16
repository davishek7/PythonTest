import array as arr
val=arr.array('i',[4,3,5,8])
print(val)
print(val[0])

for i in range(4):
    print(val[i])

for i in range(len(val)):
    print(val[i])

for i in val:
    print(i)

print(val.buffer_info())
print(val.typecode)
val.reverse()
print(val)

newArr=arr.array(val.typecode,(a for a in val))
for i in newArr:
    print(i)

newsquareArr=arr.array(val.typecode,(a*a for a in val))
for i in newsquareArr:
    print(i)