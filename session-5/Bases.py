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