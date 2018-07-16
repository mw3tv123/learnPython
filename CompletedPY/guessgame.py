import random
count = 0
while True:
	count += 1
	number = random.randint(1, 9)
	answer = input('Please input number: ')
	if answer == "exit":
		break
	elif answer > number:
		print('Your guess was higher!')
	elif answer < number:
		print('Your guess was lowwer!')
	else:
		print('You exactly right!')
print('Times played: ' + str(count))
