import time

def wrapper(f):
    def inner(*arg):
        return f(*arg)
    return inner

def foo(x):
    return x

closure = wrapper(foo)
print closure
result = closure(2,-3)
print result
