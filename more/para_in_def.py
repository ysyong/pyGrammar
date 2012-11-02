def power(power, *args):
    '''Return the sum of each argument raised to specified power.'''
    total=0
    for i in args:
    	total+=pow(i, power)
    return total
print power(2, 3, 4)
print power(2, 10)
