import random
passcodes = ['123456', 'qwerty', 'password', 'iloveyou', 'abc123', 'dragon']

print('passcodes: ' + str(passcodes))
print('I am thinking of a passcode. Can you guess it in 3 attempts?')

num_guesses = 3
index = random.randint(0, len(passcodes) - 1)
secret_word = passcodes[index]

while True:
    guess = input('enter your guess: ')
    num_guesses -= 1
    if guess == secret_word:
        print('You won! :)')
        break
    if num_guesses == 0:
        print('You lost! :(')
        break
    print('Wrong guess. Number of guesses remaining = ' + str(num_guesses))

print('Secret word = ' + secret_word)
