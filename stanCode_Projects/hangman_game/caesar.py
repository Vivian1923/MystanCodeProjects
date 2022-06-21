"""
File: caesar.py
Name: Vivian
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Users will be asked to input a number to produce shifted ALPHABET as the cipher table.
    After that, any strings typed in will be encrypted.
    """
    num = int(input("Secret number: "))
    new_alphabet = ALPHABET[len(ALPHABET) - num:] + ALPHABET[:len(ALPHABET) - num]
    strings = input("What's the ciphered string? ")
    str2 = strings.upper()
    ans = deciphered_string(str2, new_alphabet)
    print('The deciphered string is: '+ ans)


def deciphered_string(strs, new_alphabet):
    """
    The function will decipher the encrypted string.
    """
    ans = ''
    for i in range(len(strs)):
        ch = strs[i]
        if ch in new_alphabet:
            j = new_alphabet.find(ch)
            ans += ALPHABET[j]
        else:
            ans += ch
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
