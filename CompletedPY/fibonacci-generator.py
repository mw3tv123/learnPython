def generate_fibonacci():
	limit = input("Enter limit: ")
	i = 2
	if limit == 1:
		fib_list = [1]
	elif limit == 2:
		fib_list = [1, 1]
	elif limit > 2:
		fib_list = [1, 1]
		while i < limit-1:
			fib_list.append(fib_list[i-1] + fib_list[i-2])
			i += 1
	return fib_list
	
print(generate_fibonacci())
