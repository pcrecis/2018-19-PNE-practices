from Seq import Seq

# Main program

s1 = Seq("ACGTTGCAAGCTCCA")
s2 = Seq("GTACGT")
s3 = s1.complement()
s3 = Seq(s3)
s4 = Seq(s2.reverse())

sequences = [s1, s2, s3, s4]

for i in range(len(sequences)):
    l = sequences[i].len()
    counter_A = sequences[i].count_bases('A')
    counter_T = sequences[i].count_bases('T')
    counter_C = sequences[i].count_bases('C')
    counter_G = sequences[i].count_bases('G')
    perc_A = sequences[i].perc('A')
    perc_T = sequences[i].perc('T')
    perc_C = sequences[i].perc('C')
    perc_G = sequences[i].perc('G')


    print("Sequence: {}".format(sequences[i].strbases))
    print("  Length: {}".format(l))
    print("  Bases count: A: {}, T: {}, C: {}, G: {}".format(counter_A, counter_T, counter_C, counter_G))
    print("  Bases percentage: A: {}%, T: {}%, C: {}%, G: {}%".format(perc_A, perc_T, perc_C, perc_G))