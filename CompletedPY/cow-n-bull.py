import random

def compare_number(base_number, user_number):
	cow_n_bull = [0,0]
	for i in range(len(base_number)):
		if base_number[i] == user_number[i]:
			cow_n_bull[1] += 1
		else:
			cow_n_bull[0] += 1
	return cow_n_bull

if __name__=="__main__":
	playing = True
	time_play = 0
	_base_number_ = str(random.randint(0,9999))
	print(_base_number_)
	
	while playing:
		time_play += 1
		_user_number_ = str(input(">Enter your guess: "))
		_cow_n_bull_ = compare_number(_base_number_, _user_number_)
		if _cow_n_bull_[1] == 4:
			print("You totally right! You guess exactly after " + str(time_play) + " guessed!")
			playing = False
			break
		else:
			print("Mostly there! " + str(_cow_n_bull_[0]) + " cow(s) and " + str(_cow_n_bull_[1]) + " bull(s).")
