#!/usr/bin/env python

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci(max_value):
	x_1 = 1
	x_2 = 1

	ret_list = [x_1, x_2]

	while ((x_1 + x_2) < max_value):
		ret_list.append(x_1 + x_2)	
		x_t = x_2
		x_2 = x_1 + x_2
		x_1 = x_t

	return ret_list

def even_sieve(x_list):
	ret_list = []

	for i in x_list:
		if i % 2 == 0:
			ret_list.append(i)

	return ret_list

if __name__ == "__main__":
	fib_sum = 0
	for i in even_sieve(fibonacci(4000000)):
		fib_sum += i
	print str(fib_sum)
	quit()
