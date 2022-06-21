"""
File: quadratic_solver.py
Name: Vivian
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	The program asks the user to input three numbers(a, b, and c) and help the to solve the quadratic equtation.
	"""
	print('stanCode Quadratic Solver!')
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	t = b * b - 4 * a * c
	if t < 0:
		print('no real roots')
	else:
		y = math.sqrt(t)
		if t > 0:
			x1 = (-b+y) / 2*a
			x2 = (-b-y) / 2*a
			print('Two roots: '+str(x1)+' , '+str(x2))
		elif t == 0:
			x = (-b+y) / 2*a
			print('One root: ' + str(x))


###### DO NOT EDIT CODE BELOW THIS LINE ######


if __name__ == "__main__":
	main()
