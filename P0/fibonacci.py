print("Adding the fibonacci terms from 1 to n. In this case the n parameter is a constant: '100'")

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    return

fib(100)