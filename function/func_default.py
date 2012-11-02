#we must notice that: def func(a, b=5) is ok, but def func(a=5, b) is wrong.
def say(m, t=1):
    print m*t

say('hello')
say('hello', 5)
