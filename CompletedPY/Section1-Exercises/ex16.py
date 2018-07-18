"""Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has
to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the
actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to
guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an
infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and
display a different message if the player tries to guess that letter again. Remember to stop the game when all the
letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of
guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...

And so on, until the player gets the word.

ET: 4 hours
"""
import random
import re

word_file = "/usr/share/dict/words"
word_list = open(word_file).read().splitlines()
words = re.sub("['!@#$]", '', str.upper(random.choice(word_list)))
length = 0
for each in words:
    length += 1
answer = ["_"]*length
guess_history = []
print(">>> Welcome to Hangman!")
while True:
    for char in answer:
        print(char, end=" ", flush=True)
    user_guess = input("\n>>> Guess your letters: ")
    guess_history.append(user_guess)
    flag = False
    if user_guess in words:
        flag = True
        for index, value in enumerate(words):
            if value == user_guess:
                answer[index] = user_guess
    if flag:
        print("Correct!\n")
    else:
        print("Incorrect!\n")
    check_list = [x for x in words if x in answer]
    if len(check_list) == length:
        print("~ You have guessed the word! Congratulation! ~")
        print("".join(words))
        print("Your guessed's history: " + " ".join(guess_history))
        break
