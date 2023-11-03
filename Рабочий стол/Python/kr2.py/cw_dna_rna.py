def dna_to_rna(dna:str)->str:
    if 'T' in dna:
        rna = dna.replace('T', 'U')
    else:
        rna = dna
    return rna
print(dna_to_rna('TTTT'))
        