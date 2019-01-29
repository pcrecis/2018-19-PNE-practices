def sumn(n):
    total = 0
    for i in range(n):
        total = total + i + 1

    return total

#--- Main program
n = int(input("Please, introduce n: "))
print("The total sum of the first %s is: %s" % (n, sumn(n)))