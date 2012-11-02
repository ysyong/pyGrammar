poem='''\ysyong , how are you
how are you
chang jin a 
ni bu yao shang xin, ye bu yao ku qi,
geng bu yao qing yan fang qi
'''
f = file('poem.txt', 'w') #open a file for writing something
f.write(poem) #write
f.close #close

f =  file('poem.txt') #'r' mode is assumed by default
while True:
    line = f.readline()
    if len(line)==0:#zero length indicates EOF
        break
    print line,
f.close()
