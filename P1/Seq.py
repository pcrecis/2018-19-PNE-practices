class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        comp = ""
        for b in self.strbases:
            if b == 'A':
                comp += 'T'
            elif b == 'C':
                comp += 'G'
            elif b == 'T':
                comp += 'A'
            elif b == 'G':
                comp += 'C'
        return comp

    def reverse(self):
        return self.strbases[::-1]

    def count_base(self, base):
        counter = 0
        for b in self.strbases:
            if b == base:
                counter = 0
        return counter

    def perc(self, base):
        self.count(base) * 100.0 */ self.len()

s1 = Seq("AAAGG")

str1 = s1.strbases   # atribute inside the code
#str2 = s2.strbases

l1 = s1.len()
c1 = s1.complement()
r1 = s1.reverse()
counter_A = s1.count('A')
counter_C = s1.count('C')
counter_T = s1.count('T')
counter_G = s1.count('G')

#l2 = s2.len()

print("Sequence 1: {}".format(str1))
print(" Length: {}".format(l1))
print("Complementary sequence: {}".format(c1))
print("Reverse sequence: {}".format(r1))

