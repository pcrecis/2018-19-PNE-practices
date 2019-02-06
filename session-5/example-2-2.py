from Bases import count_bases

#------Main program
s1 = input("Please, enter the sequence 1: ")
s2 = input("Please, enter the sequence 2: ")
sequences = [s1, s2]
na1 = count_bases(sequences[0])
na2 = count_bases(sequences[1])

# Calculate the total sequence length and their percentage
t1 = len(s1)
t2 = len(s2)
try:
    # First sequence
    print("This sequence is {} bases in length".format(t1))
    print("Base A")
    print("  Counter: ", na1['A'])
    print("  Percentage: ", round(100.0 * na1['A'] / t1, 1))
    print("Base C")
    print("  Counter: ", na1['C'])
    print("  Percentage: ", round(100.0 * na1['C'] / t1, 1))
    print("Base T")
    print("  Counter: ", na1['T'])
    print("  Percentage: ", round(100.0 * na1['T'] / t1, 1))
    print("Base G")
    print("  Counter: ", na1['G'])
    print("  Percentage: ", round(100.0 * na1['G'] / t1, 1))
    print("")
    # Second sequence
    print("This sequence is {} bases in length".format(t2))
    print("Base A")
    print("  Counter: ", na2['A'])
    print("  Percentage: ", round(100.0 * na2['A'] / t2, 1))
    print("Base C")
    print("  Counter: ", na2['C'])
    print("  Percentage: ", round(100.0 * na2['C'] / t2, 1))
    print("Base T")
    print("  Counter: ", na2['T'])
    print("  Percentage: ", round(100.0 * na2['T'] / t2, 1))
    print("Base G")
    print("  Counter: ", na2['G'])
    print("  Percentage: ", round(100.0 * na2['G'] / t2, 1))
except KeyboardInterrupt:
    pass
except ZeroDivisionError:
    pass