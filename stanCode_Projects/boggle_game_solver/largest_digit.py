"""
File: largest_digit.py
Name: Vivian
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	n1 = abs(n)
	if n1 < 10:
		return n1
	else:
		n2 = n1 % 10
		n3 = n1//10 % 10
		if n2 > n3:
			n1 = n1//10-n3+n2
		else:
			n1 = n1//10
		return find_largest_digit(n1)


if __name__ == '__main__':
	main()
