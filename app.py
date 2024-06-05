from flask import Flask, request, render_template, session, redirect, url_for
import random
import hangman_words
import hangman_art

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    session['chosen_word'] = random.choice(hangman_words.word_list)
    session['word_length'] = len(session['chosen_word'])
    session['end_of_game'] = False
    session['lives'] = 6
    session['guesses'] = []
    session['display'] = ["_" for _ in range(session['word_length'])]
    return render_template('home.html', display=session['display'], lives=session['lives'], logo=hangman_art.logo, stages=hangman_art.stages)

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form.get('guess').lower()
    if guess in session['guesses']:
        return redirect(url_for('home'))
    session['guesses'].append(guess)
    for position in range(session['word_length']):
        letter = session['chosen_word'][position]
        if letter == guess:
            session['display'][position] = letter
    if guess not in session['chosen_word']:
        session['lives'] -= 1
        if session['lives'] == 0:
            session['end_of_game'] = True
    if "_" not in session['display']:
        session['end_of_game'] = True
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)