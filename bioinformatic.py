import random

valid_nuc = "AGCT"

codontab = {
    'UCA': 'S',    # Serina
    'UCC': 'S',    # Serina
    'UCG': 'S',    # Serina
    'UCU': 'S',    # Serina
    'UUC': 'F',    # Fenilalanina
    'UUU': 'F',    # Fenilalanina
    'UUA': 'L',    # Leucina
    'UUG': 'L',    # Leucina
    'UAC': 'Y',    # Tirosina
    'UAU': 'Y',    # Tirosina
    'UAA': '*',    # Stop
    'UAG': '*',    # Stop
    'UGC': 'C',    # Cisteina
    'UGU': 'C',    # Cisteina
    'UGA': '*',    # Stop
    'UGG': 'W',    # Triptofano
    'CUA': 'L',    # Leucina
    'CUC': 'L',    # Leucina
    'CUG': 'L',    # Leucina
    'CUU': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCU': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAU': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGU': 'R',    # Arginina
    'AUA': 'I',    # Isoleucina
    'AUC': 'I',    # Isoleucina
    'AUU': 'I',    # Isoleucina
    'AUG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACU': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAU': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGU': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GUA': 'V',    # Valina
    'GUC': 'V',    # Valina
    'GUG': 'V',    # Valina
    'GUU': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCU': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAU': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGU': 'G'     # Glicina
}

# Generate a random DNA sequence of given length.
dna_sequence = ''
for _ in range(100):
    dna_sequence += random.choice(valid_nuc)

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

if __name__ == "__main__":
    # Interactive menu for DNA analysis.
    while True:
        print("\nWelcome\nPlease choose one of the following options: ")
        print("1. Generate random DNA\n2. Targeted DNA entrance\n3. Exit")
        option = int(input("option number: "))

        if option == 1:
            iteration = int(input("Please define your DNA sequence lengh(e.g 100): "))

            random_dna_sequence = ''
            for _ in range(iteration):
                random_dna_sequence += random.choice(valid_nuc)
        
            if validate_dna_sequence(random_dna_sequence) == True:
                dna_nuc_counter(random_dna_sequence)
                print("\nDNA:")
                print(f"Template strand: {random_dna_sequence}")
                translation(transcription(dna_reverse_complement(random_dna_sequence)))

        elif option == 2:
            user_dna_seqence = input("Please enter your target DNA sequence: ").upper().strip()

            if validate_dna_sequence(user_dna_seqence) == True:
                dna_nuc_counter(user_dna_seqence)
                print("\nDNA:")
                print(f"Template strand: {user_dna_seqence}")
                translation(transcription(dna_reverse_complement(user_dna_seqence)))

        elif option == 3:
            print("\nGoodbye!")
            break

        else:
            print("\nChosen option is invalid!")
            continue
