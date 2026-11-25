fibdict = {
    1: 1,
    2: 1
}

def fib(n):

    if n in fibdict:
        return fibdict[n]

    new = fib(n-1) + fib(n-2)
    fibdict[n] = new

    return new

print(fib(250))