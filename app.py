from flask import Flask, render_template, request, redirect, url_for
import random
import hangman_words
import hangman_art

app = Flask(__name__)

# Global variables to store game state
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
guesses = []
display = ['_' for _ in range(word_length)]

@app.route('/', methods=['GET', 'POST'])
def index():
    global end_of_game, lives, guesses, display

    if request.method == 'POST':
        guess = request.form['guess'].lower()

        # Check if the letter was already guessed
        if guess in guesses:
            message = "You have already entered that letter."
        else:
            guesses.append(guess)
            if guess in chosen_word:
                for position in range(word_length):
                    if chosen_word[position] == guess:
                        display[position] = guess
                message = "Correct!"
            else:
                lives -= 1
                message = "This letter is not in the word."
                if lives == 0:
                    end_of_game = True
                    message = "You lose. The word was " + chosen_word

        # Check if the game is won
        if '_' not in display:
            end_of_game = True
            message = "You win!"

        return render_template('index.html', display=display, lives=lives, message=message, guesses=guesses, stages=hangman_art.stages[lives])

    return render_template('index.html', display=display, lives=lives, message='', guesses=guesses, stages=hangman_art.stages[lives])

if __name__ == '__main__':
    app.run(debug=True)
