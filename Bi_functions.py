from Bi_utility import *

def validate_dna_sequence(s: str) -> bool:
    # Check if sequence contains only valid nucleotides (A, G, C, T).
    for n in s:
        if n not in valid_nuc:
            print("The DNA sequence is not valid!")
            return False
    print("The DNA sequence is valid.")
    return True

def dna_nuc_counter(s: str):
    # Return a count of nucleotides in the sequence. 
    a = s.count("A")
    g = s.count("G")
    c = s.count("C")
    t = s.count("T")
    print(f"\nNumber of nuc in DNA sequence:\nA: {a}\nG: {g}\nC: {c}\nT: {t}")

def dna_reverse_complement(s: str) -> str:
    # Return the reverse complement of a DNA sequence.
    complement = ''

    nuc = {
        "A": 'T',
        "G": 'C',
        "C": 'G',
        "T": 'A'
    }

    for n in s:
        complement += nuc[n]

    print(f"Complement: {complement}")
    print(f"Reversed Complement: {complement[::-1]}")
    return complement[::-1]

def transcription(rc: str) -> str:
    # Transcribe DNA (template strand) into RNA.
    rna = rc.replace("T", "U")

    print(f"\nRNA:\n{rna}")
    return rna

def translation(rna: str) -> str: 
    # Translate RNA into protein sequence.
    protein = ''
    for i in range(0, len(rna)-2, 3):
        protein += codontab[rna[i:i+3]]

    print(f"\nProtein:\n{protein}")
