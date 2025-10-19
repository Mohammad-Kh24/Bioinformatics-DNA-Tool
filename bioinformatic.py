import random
from Bi_utility import *
from Bi_functions import *


# Generate a random DNA sequence of given length.
dna_sequence = ''
for _ in range(100):
    dna_sequence += random.choice(valid_nuc)


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
