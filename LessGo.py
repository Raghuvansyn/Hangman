import random

from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

print(logo)

chosen_one = random.choice(word_list)



word_list= len(chosen_one)
print(word_list)

placeholder = ""
for position in range(word_list):
    placeholder+="_"
print(placeholder)

number_of_lives = 6


game_over = False

correct_letters=[]

while not game_over:
    print(f"****{number_of_lives}/6 left**** ")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"YOU HAVE ALREADY GUESSED {guess}")

    display = ""
    for letter in chosen_one:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_one:
        number_of_lives-= 1
        print(f"YOU GUESSED {guess} THAT'S WRONG")
        if number_of_lives == 0:
            game_over = True
            print(f"YOU LOSE; IT WAS {chosen_one}")


    if "_" not in display:
        game_over = True
        print("YOU WIN")

    print(stages[number_of_lives])