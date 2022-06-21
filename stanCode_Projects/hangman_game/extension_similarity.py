"""
File: similarity.py (extension)
Name: Vivian
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The program will ask user to input long dna sequence and short dna sequence,
    and help user to compare long dna sequence and short dna sequence in order to find which part
    of long dna sequence best match the short dna sequence.
    """
    long_dna = input('please give me a DNA sequence to search: ')
    long_sequence = long_dna.upper()
    short_dna = input('What DNA sequence would you like to match? ')
    short_sequence = short_dna.upper()
    best_match = ''
    match = 0
    for i in range(len(long_sequence)-len(short_sequence)+1):
        string = long_sequence[i:i+len(short_sequence)]
        dna = ''
        for j in range(len(short_sequence)):
            if string[j] == short_sequence[j]:
                dna += short_sequence[j]
        if (len(dna) / len(short_sequence)) > match:
            match = (len(dna) / len(short_sequence))
            best_match = string
    print('The best match is '+best_match)


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
