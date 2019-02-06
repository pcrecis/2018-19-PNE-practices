def countbases(filename):
    with open(filename,'r') as f:
        content = f.read()
    print("The total length of the sequence is", len(content))
    print("The number of bases 'A' is: ", content.count('A'))
    print("The number of bases 'C' is: ", content.count('C'))
    print("The number of bases 'T' is: ", content.count('T'))
    print("The number of bases 'G' is: ", content.count('G'))

filename= input("Please introduce a file name: ")
countbases(filename)



