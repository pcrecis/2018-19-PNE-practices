def countbases(filename):
    with open(filename,"r") as f:
        for line in f:
            line = line.strip("\n")
            print("The total length of the sequence" "is", len(line))
            print("The number of bases 'A' is: ", line.count('A'))
            print("The number of bases 'C' is: ", line.count('C'))
            print("The number of bases 'T' is: ", line.count('T'))
            print("The number of bases 'G' is: ", line.count('G'))

countbases('seq_external.py')



