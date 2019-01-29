def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    return

#--- Main program
print("Adding the fibonacci terms from 1 to n.")
n = int(input("Please, introduce n: "))
fib(n)