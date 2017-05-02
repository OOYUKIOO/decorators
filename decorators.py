import time

def name(f):
    def inner(*args):
        print "Function name: "+ f.func_name
        print "Arguments: " + str(args)
        return f(*args)
    return inner

def execTime(f):
    init = time.time()
    def inner(*args):
        result = f(*args) 
        return result
    end = time.time()
    t = end-init
    print "Execution time: " + str(t)
    return inner

def memoi(f):
    cache = {}
    def inner(*args):
        if args[0] in cache:
            return cache[args[0]]
        else:
            cache[args[0]] = f(*args)
            return f(*args)
    return inner

@memoi
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1)+fib(n-2)



print fib(300)

fibcache = {}
def Fib(n):
    if n in fibcache:
        return fibcache[n]
    else:
        fibcache[n] = n if n < 2 else fib(n-1)+fib(n-2)
        return fibcache[n]


