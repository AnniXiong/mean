# test
from mean import *

def test_ints():
	num_list = [4,5,28,3]
	obs = mean(num_list)
	exp = 10
	assert obs == exp

def test_zero():
	num_list = [3,0,3]
	obs = mean(num_list)
	exp = 2
	assert obs ==exp

def test_neg():
	num_list = [-1,1]
	obs = mean(num_list)
	exp = 0
	assert obs == exp