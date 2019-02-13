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

    def count_bases(self, base):
        counter = 0
        for b in self.strbases:
            if b == base:
                counter += 1
        return counter

    def perc(self, base):
        return round(self.count_bases(base) * 100.0 / self.len(), 1)

