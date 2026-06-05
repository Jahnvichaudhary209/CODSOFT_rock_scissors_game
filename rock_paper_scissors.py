from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

CHOICES = ['rock', 'paper', 'scissors']

def get_result(user, computer):
    if user == computer:
        return 'tie'
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return 'win'
    return 'lose'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice', '').lower()

    if user_choice not in CHOICES:
        return jsonify({'error': 'Invalid choice'}), 400

    computer_choice = random.choice(CHOICES)
    result = get_result(user_choice, computer_choice)

    messages = {
        'win':  'You win! 🎉',
        'lose': 'Computer wins! 😞',
        'tie':  "It's a tie! 🤝"
    }

    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
        'message': messages[result]
    })

if __name__ == '__main__':
    app.run(debug=True)
