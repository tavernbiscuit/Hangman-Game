

import random
import hangman_words
import hangman_art



chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guesses = []


print(hangman_art.logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game: 
    guess = input("Guess a letter: ").lower()
   
    for char in guesses:
      if guess == char:
        print(f"You have entered: {guess}. You have already entered that letter.")
    guesses.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
      
        if letter == guess:
            display[position] = letter

  
    if guess not in chosen_word:
       
        print(f"You have entered: {guess}. This letter is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(hangman_art.stages[lives])