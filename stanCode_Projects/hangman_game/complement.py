"""
File: complement.py
Name: Vivian
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The program will find the complement of DNA that depends on user inputs.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna2 = dna.upper()
    print('The complement of '+dna+' is '+build_complement(dna2))


def build_complement(dna2):
    """
    The function will build the complement of DNA that depends on user inputs.
    """
    ans = ''
    for i in range(len(dna2)):
        ch = dna2[i]
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'C':
            ans += 'G'
        elif ch == 'G':
            ans += 'C'
    return ans
    print(ans)


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
