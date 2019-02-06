def count_bases(seq):
    """ Counting the number of bases (A, C, T, G) in the sequence"""
    counter_A = 0
    counter_C = 0
    counter_T = 0
    counter_G = 0
    for b in seq:
        if b == 'A':
            counter_A += 1
        elif b == 'C':
            counter_C += 1
        elif b == 'T':
            counter_T += 1
        elif b == 'G':
            counter_G += 1
    return dict(A= counter_A, C= counter_C, T= counter_T, G= counter_G)

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

