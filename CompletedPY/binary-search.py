# Generated a list with random element
import random
def gen_Random_List(limit):
	list_ = []
	for __ in range(limit):
		list_.append(random.randint(0,100))
	return list_

# Sorted list to increment list
def sort_List(input_list):
	for i in range(1, len(input_list)-1):
		if input_list[i] < input_list[i-1]:
			temp = input_list[i]
			input_list[i] = input_list[i-1]
			input_list[i-1] = temp
	return input_list

# Binary search
def binary_Search(k, list_):
	x = len(list_)/2
	if k == list_[x]:
		return True
	elif k > list_[x]:
		for i in range(x, len(list_)-1):
			if k == list_[i]:
				return True
	else:
		for i in range(0, x-1):
			if k == list_[i]:
				return True
	#return False

# Print out to the screence
def output_Data(income_data):
	print(income_data)

# __Main__
if __name__ == "__main__":
	limit = input("Enter list limit: ")
	rand_list = sort_List(gen_Random_List(limit))
	output_Data(rand_list);
	key_k = input("Enter Key to search: ")
	if binary_Search(key_k, rand_list) == True:
		print(key_k)
	else:
		print("Cannot find k!")
