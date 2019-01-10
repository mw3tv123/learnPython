def reverse_Word(word = " "):
	return " ".join(word.split()[::-1])

name = raw_input("Your name is ")

print(reverse_Word(name))

