def recursion_factorial(num):
	if num > 1:
		return num * recursion_factorial(num - 1)
	else:
		return 1

def loop_factorial(num):
	my_factorial = 1
	
	while num > 1:
		my_factorial = my_factorial * num
		num = num - 1
	
	return my_factorial

recursion_factorial(5)
loop_factorial(5)