f = open('CPLX2.txt', 'r')
content = f.read()
if not(content.startswith('>')):
    print("The total length of the sequence is", len(content))
    print("The number of bases 'A' is: ", content.count('A'))
    print("The number of bases 'C' is: ", content.count('C'))
    print("The number of bases 'T' is: ", content.count('T'))
    print("The number of bases 'G' is: ", content.count('G'))

f.close()


