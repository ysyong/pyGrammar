# a=b: when we change b, a also changed; but when we change a, b is not changed this is so called "reference"
print 'Simple Assignment'
shoplist=['apple','maggo','carrot','banana']
mylist=shoplist #mylist is just another name pointing to the same object

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist #mylist is not being del

print 'copy by making a full slice'
mylist=shoplist[:]
del mylist[0]
 
print 'shoplist is', shoplist #shoplist is not being del
print 'my list is', mylist

