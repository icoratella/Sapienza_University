DNA = 'TCCCCATCTTCTGTTACGGTCATGGTTTGCAGATGGCCTTAGGCATTGAACCACGCTTAATCGGAATCCCGAATGGTAACGAACCGCAGCACCCACGAAGATAAACAATAGTCGAAGAGCGAGTGGATTTTGGATCTGAATATAGTTTATTGGCTGCCTAACTAACTGAATATGTGCAACAGGCTGTAGCTTTGCGCATTCAACTACTTGACAATGTCAGCGACTTAATACGATTGGGGCTGTGCCGTGCGCGCCCACGCGGGAGCACAGTACGAAATGTAGAGAGACCAACATTGGACGCGCAATTCGTCAGACCTGGTTCCACGCTTCGAGGCAATCGTCGTGTTTTTCTCCTCAGGATGCGATTCGCTGTTAGTGCTGTACGTAAGTGACCCTGCATTGCCCCTGAGTATATTCATCCACGGTATGCTTCTTTCCATTGTTGCAGTGTTTGTCAAGACGGCTCTCCACGACCAGCATCATACATAACTAACTCGTTAGAACGCGATAATGCCTTGCCCTTACAACTGTTCGAGGTTTTCGTTTTCATTTGTCTCAAGAGGCATTACAGGTGAGTAAGGAGAGTGTGTCCACTGACAACCCGGACGTCTTCTGAGTGACGCTATGTCGATGGATGTAGATTGGCCGCGGTAAAGTAGCTTTTATGTTCTACTGTACGGGCATTGGGATCAGGAGGCCTGCTCAGTTGTGAGTACCGGGGTCTTCATGTCATGCGTAGTCTGCTCGTAGCAATCTGTATCGAGAGTCGCTACAGGGCTCCTTTTTCATGTGTGACCCTCCTACAATTATGCTCACTCTAAAGTCCTCCTCTAAGCCCTAGGATCGCCTATCCAGTAGAGTTGATAAGCTCTGACTCGTATACCTTCTCTAACAGTTGCTTAGACGCGCTTTTTCAGTAGCAGA'
RNA = []
for char in DNA:
    if char == 'T':
        RNA.append('U')
    else:
        RNA.append(char)
print(''.join(RNA))


