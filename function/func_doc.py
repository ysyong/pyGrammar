def Max(x, y):
    '''print the maxinum of two numbers.

       the two values must be integers.'''
    x=int(x)
    y=int(y)
    if x>y:
        print x, 'is maxinum'
    else:
        print y, 'is maxinum'
Max(3,5)
print Max.__doc__
#help(max)
