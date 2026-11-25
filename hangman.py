
import random

words = ["python", "apple", "mango", "tiger", "school"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_attempts - wrong_guesses)

else:
    print("\nGame Over!")
    print("The word was:", secret_word)
