from Bases import count_bases

#------Main program
s = input("Please enter the sequence: ")
na = count_bases(s)

# Calculate the total sequence length and their percentage
t = len(s)
try:
    print("This sequence is", t, "bases in length")
    print("Base A")
    print("  Counter: ", na['A'])
    print("  Percentage: ", round(100.0 * na['A'] / t, 1))
    print("Base C")
    print("  Counter: ", na['C'])
    print("  Percentage: ", round(100.0 * na['C'] / t, 1))
    print("Base T")
    print("  Counter: ", na['T'])
    print("  Percentage: ", round(100.0 * na['T'] / t, 1))
    print("Base G")
    print("  Counter: ", na['G'])
    print("  Percentage: ", round(100.0 * na['G'] / t, 1))
except KeyboardInterrupt:
    pass
except ZeroDivisionError:
    pass