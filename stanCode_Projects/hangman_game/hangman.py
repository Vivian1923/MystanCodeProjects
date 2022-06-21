"""
File: hangman.py
Name: Vivian
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Users will see a dashed word and try to correctly figure the un-dashed word out by inputting one character each round.
    If the user input is correct, show the updated word on console. Players have N_TURNS chances to try and win this game.
    """
    input_ch = random_word()
    print('The word looks like '+len(input_ch)*'-')
    print('You have '+str(N_TURNS)+' wrong guesses left')
    guess = input('Your guess: ')
    guess2 = guess.upper()
    correct_guesses = ''
    wrong_guesses = ''
    life = N_TURNS
    while life >= 1:
        if len(guess2) == 1 and guess2.isalpha():
            ans = ''
            if guess2 in input_ch:
                correct_guesses += guess2
            for i in range(len(input_ch)):
                ch = input_ch[i]
                if ch in correct_guesses:
                    ans += ch
                else:
                    ans += "-"
            if guess2 in input_ch:
                print("You are correct!")
                if '-' in ans:
                    print('The word looks like '+ans)
                    print('You have '+str(life)+' wrong guesses left.')
                    guess = input('Your guess: ')
                    guess2 = guess.upper()
                else:
                    print("You win!")
                    print('The word was: ' + input_ch)
                    break
            else:
                if guess2 not in wrong_guesses:
                    life -= 1
                    wrong_guesses += guess2
                if life == 0:
                    print('You are completely hung : (')
                    print('The word was: ' + input_ch)
                else:
                    print("There is no " + guess2 + "'s in the word.")
                    print('The word looks like ' + ans)
                    print('You have '+str(life)+' wrong guesses left.')
                    guess = input('Your guess: ')
                    guess2 = guess.upper()
        else:
            print('Illegal format.')
            guess = (input('Your guess: '))
            guess2 = guess.upper()


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
