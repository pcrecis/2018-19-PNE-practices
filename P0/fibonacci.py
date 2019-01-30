print("Adding the fibonacci terms from 1 to n.")
n = int(input("Please, introduce n: "))

def fibonacci(n):
    a, b = 1,1
    for i in range(n-2):
        a, b = b,a+b
    return a
print(fibonacci(n))
