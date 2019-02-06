def count_a(seq):
    """Counting the number of As in the sequence"""

    # Counter for the As
    result = 0
    for b in seq:
        if b == 'A':
            result += 1

     # Return the result
    return result

# Main program

s = "AGTACACTGGT"
na = count_a(s)
print("The number of As is: {}".format(na))

# Calculate the total length
t1 = len(s)

print("This sequence is {} bases in length".format(t1))
print("The percentage of As is {}%".format(round(100.0 * na/t1, 1)))