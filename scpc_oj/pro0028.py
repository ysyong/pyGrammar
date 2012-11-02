while  True:
    line = readline()
    x=raw_input()
    if x=='\n':
        break
    else:
        y=float(x)
        z=int(y)
        if y==z:
            print 'Yes'
        else:
            print 'No'
    
