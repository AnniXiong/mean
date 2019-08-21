
import numpy


def mean (num_list):
	
	assert isinstance (num_list, list)
	#if (len(num_list) == 0):
		#raise Exception ("the mean of an empty list is undefined")

	try:
		return sum(num_list)/len(num_list)
	except ZeroDivisionError:
		return 0
	except TypeError as detail:
		msg = "plz provide a list of numbers"
		raise TypeError(detail.__str__() + "\n" +  msg)
		#msg = "The algebraic mean of an empty list is undefined. Please provide a list of numbers."
		#raise ZeroDivisionError(detail.__str__() + "\n" +  msg)


