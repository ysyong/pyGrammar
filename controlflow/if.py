#we must pay attention the way to use 'raw_input()'
number=23
guess=int(raw_input('Enter an integer : '))
if guess==number:
    print 'Congratulations, you guessed it'
    print '(but you do not win any prizes!)'
elif guess<number:
    print 'No, it is a little highter than that'
else:
    print 'No, it is a little lower than thar'

print 'Done'
# This last statement is always executed, after the if statement is executed 
