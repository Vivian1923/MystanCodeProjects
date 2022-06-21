"""
File: weather_master.py
Name: Vivian
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100     # Sentinel value


def main():
	"""
	Whatever the temperatures the user input, the program can calculate the highest, lowest, average
	and cold days among the inputs.
	"""
	print("stanCode \"Weather Master 4.0\"!")
	n = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	i = 0   # i = Sum of the temperatures that user input
	if i != EXIT:
		i = n
	j = 1   # j = Count how many temperatures that user input
	k = 0   # k = Count how many cold days ( temperature < 16)
	if n < 16:
		k += 1
	maximum = n  # Highest temperature
	minimum = n  # Lowest temperature
	if n == EXIT:
		print('No temperatures were entered.')
	else:
		while True:
			if n == EXIT:
				break
			if n != EXIT:
				n = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
				if n != EXIT:
					if maximum < n:
						maximum = n
					if n < minimum:
						minimum = n
					i += n
					j += 1
					if n < 16:
						k += 1
		print('Highest temperature = '+str(maximum))
		print('Lowest temperature = '+str(minimum))
		print('Average = '+str(avg_temperature(i,j)))
		print(str(k)+' cold day(s)')


def avg_temperature(i,j):
	ans = i / j
	return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
