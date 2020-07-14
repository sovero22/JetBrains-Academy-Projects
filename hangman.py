import random
import sys

program_lang = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')


def hangman_menu():
    decision = ''
    while decision != 'play' or decision != 'exit':
        decision = input('Type "play" to play the game, "exit" to quit: ')
        if decision == 'exit':
            sys.exit()
        elif decision == 'play':
            break


hangman_menu()
survival_word = random.choice(program_lang)
msg = len(survival_word) * '-'
attempt = 1
input_letters = []
abc = 'qwertyuiopasdfghjklzxcvbnm'

while attempt < 9:
    print()
    print(msg)
    n_msg = ''
    letter = input('Input a letter:')
    if letter in input_letters:
        print('You already typed this letter')
        continue
    if len(letter) != 1:
        print('You should input a single letter')
        continue
    elif letter not in abc:
        print('It is not an ASCII lowercase letter')
        continue

    input_letters.append(letter)
    if letter in set(survival_word):
        q = 0
        for q in range(len(survival_word)):
            if letter == survival_word[q] and '-' in msg:
                n_msg = n_msg + msg[q].replace('-', letter)
            elif msg[q] == '-':
                n_msg = n_msg + '-'
            else:
                n_msg = n_msg + msg[q]
        msg = n_msg
        if '-' not in msg:
            print()
            print(msg)
            print('You guessed the word!')
            print('You survived!')
            break
    else:
        print('No such letter in the word')
        attempt += 1
        continue

if '-' in msg:
    print('You are hanged!')
print()
hangman_menu()
