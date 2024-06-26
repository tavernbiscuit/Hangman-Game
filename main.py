

import random
import hangman_words
import hangman_art
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guesses = []
wrong_guesses = []
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


print(hangman_art.logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game: 
    print('Already entered: ' + "".join(str(x) for x in guesses))
    guess = input("Guess a letter: ").lower()
    clear_console()
    for char in guesses:
      if guess == char:
        print("You have already entered that letter.")
    guesses.append(guess)



    for position in range(word_length):
        letter = chosen_word[position]
      
        if letter == guess:
            display[position] = letter

  
    if guess not in chosen_word:
       
        print("This letter is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(hangman_art.stages[lives])
    