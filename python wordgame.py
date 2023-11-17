import random

words = ['programming', 'laptop', 'desktop', 'youtube','projects','microscope','mouse']

random_word = random.choice(words)

print('our random word', random_word)

print('************* WORD GUESSING GAME ****************')

user_guesses = ''
chances = 10

while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"correct guess: {character}")
        else:
            wrong_guesses += 1
            print('_')
    if wrong_guesses == 0:
        print("Correct.")
        print(f"word : {random_word}")
        break
    guess = input('Make a guesses: ')
    user_guesses += guess


    if guess not in random_word:
        chances -= 1
        print(f"wrong. you have {chances} more chances")


        if chances == 0:
            print('game over')
