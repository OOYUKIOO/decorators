import time

def name(f):
    def inner(*args):
        print "Function name: "+ f.func_name
        print "Arguments: " + str(args)
        return f(*args)
    return inner

def execTime(f):
    def inner(*args):
        init = time.time()
        result = f(*args)
        end = time.time()
        print "Execution time: " + str(end-init)
        return result
    return inner

@execTime
def foo(x):
    start = time.time()
    end = start + 2
    while start < end:
        start = time.time()
    return x+1

@name
def goo(a,b,c):
    return a+" "+b+" "+c

print foo(2)
print goo("hello","hi","bye")
