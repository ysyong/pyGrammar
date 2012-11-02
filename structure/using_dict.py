ab={ 'swaroop'   : 'swaroopch@byteofpython.info',
     'Larry'     : 'larry@wall.org',
     'ysyong'    : 'ysyong@foxmail.com',
     'ysyfff'    : 'ysyfff@qq.com'
   }
print "swaroop's address is %s" % ab['swaroop']

#adding a key/value pair
ab['Guido'] = 'guido@python.org'

#deleting a key/value pari
del ab['Larry']

print '\nThere are %d contacts in thd address-book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s'%(name, address)

if 'Guido' in ab:
    print "\nGuido's address is %s" % ab['Guido']

