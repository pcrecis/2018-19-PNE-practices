f = open('CPLX2.txt', 'r')
line = f.read()
for line in f:
    if not(line.startswith('>')):
        print("The total length of the sequence is", len(line))
        print("The number of bases 'A' is: ", line.count('A'))
        print("The number of bases 'C' is: ", line.count('C'))
        print("The number of bases 'T' is: ", line.count('T'))
        print("The number of bases 'G' is: ", line.count('G'))

f.close()


