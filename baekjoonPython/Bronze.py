def add(x,y):
    return x + y

def outer(x):
    def inner(y):
        return x+y
    return inner

print(outer(4)(2))