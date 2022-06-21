"""
File: anagram.py
Name: Vivian
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
lst = []


def main():
    """
    The function will find all anagrams in dictionary when user input a word.
    """
    ####################
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    input_word = input('Find anagrams for: ')
    start = time.time()
    if input_word == EXIT:
        pass
    else:
        while True:
            length = len(input_word)
            read_dictionary(length)
            find_word = input_word.lower()
            print('Searching...')
            find_anagrams(find_word)
            end = time.time()
            input_word = input('Find anagrams for: ')
            if input_word == EXIT:
                break
    ####################
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(length):
    """
    The function will read all the word in file and store in list.
    """
    with open("dictionary.txt", 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) == length:
                lst.append(word)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    all_anagrams = []
    find_anagrams_helper(s, '', len(s), [], all_anagrams)
    print(str(len(all_anagrams))+' anagrams: ', end='')
    print(all_anagrams)


def find_anagrams_helper(s, current_word, ans_len, num_lst, all_anagrams):
    if len(current_word) == ans_len and current_word in lst:
        if current_word not in all_anagrams:
            all_anagrams.append(current_word)
            print('Founds: '+current_word)
            print('Searching...')
    else:
        for i in range(ans_len):
            if i in num_lst:
                pass
            else:
                # choose
                current_word += s[i]
                num_lst.append(i)
                if has_prefix(current_word) is True:
                    # explore
                    find_anagrams_helper(s, current_word, ans_len, num_lst, all_anagrams)
                # un-choose
                current_word = current_word[:-1]
                num_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in lst:
        if word.startswith(sub_s) is True:
            return True
    return False


if __name__ == '__main__':
    main()
