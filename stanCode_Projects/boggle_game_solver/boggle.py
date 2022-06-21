"""
File: boggle.py
Name: Vivian
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	d = {}
	for i in range(4):
		input_word = input(str(i+1)+' row of letters: ')
		chs = input_word.split()
		if len(chs) == 4:
			for j in range(len(chs)):
				d[(i, j)] = chs[j].lower()
	lst = read_dictionary()
	all_words = []
	for place, ch in d.items():
		find_words(d, lst, place, ch, all_words)
	print('There are '+str(len(all_words))+' words in total.')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	lst = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				lst.append(word)
	return lst


def find_words(d, lst, place, ch, all_words):
	current_word = ''
	place_lst = []
	place_lst.append(place)
	current_word += ch
	find_words_helper(d, current_word, place_lst, all_words, lst, place, ch)
	# print(all_words)


def find_words_helper(d, current_word, place_lst, all_words, lst, place, ch):
	if current_word in lst:
		if current_word not in all_words:
			all_words.append(current_word)
			print('Found '+'\"'+current_word+'\"')  # 這個stack frame退掉之後會從79行接續
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			next_x = place[0]+i
			next_y = place[1]+j
			if 0 <= next_x <= 3:
				if 0 <= next_y <= 3:
					new_place = (next_x, next_y)
					if new_place not in place_lst:
						# choose
						place_lst.append(new_place)
						current_word += d[new_place]
						if has_prefix(current_word, lst) is True:
							# explore
							find_words_helper(d, current_word, place_lst, all_words, lst, new_place, ch)
						# un-choose
						current_word = current_word[:-1]
						place_lst.pop()



def has_prefix(sub_s, lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in lst:
		if word.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
