"""
File: hailstone.py
Name: Vivian
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Whatever user inputs, the program executes the calculations and makes the end value is 1.
    The program will count how many times the calculations run and print the result.
    """
    print('This program computes Hailstone sequences.')
    print('')
    n = int(input('Enter a number: '))
    j = 0   # Count how many steps the function calculates
    if n > 0:
        while True:
            if n == 1:
                break
            if n % 2 == 1:
                print(str(n)+' is odd, so I make 3n+1: '+str(is_odd(n)))
                n = is_odd(n)
                j += 1
            else:
                print(str(n) + ' is even, so I take half: ' + str(is_even(n)))
                n = is_even(n)
                j += 1
        print('It took '+str(j)+' steps to reach 1.')


def is_odd(n):
    n = 3 * n + 1
    return n


def is_even(n):
    n = int(n/2)
    return n


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
