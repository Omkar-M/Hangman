import random


def answer(letters, used_letters, hidden):
    if letters == used_letters:
        print(*hidden, sep='')
        print('''You guessed the word!
    You survived!''')
        exit()


def play():
    words = ['python', 'java', 'kotlin', 'javascript']
    tries = 8
    choice = random.choice(words)
    # a = choice[0:3]
    # b = (len(choice) - 3) * '-'
    hidden = list(len(choice) * '-')
    letters = set(choice)
    used_letters = []
    symbols = '1234567890!@#$%^&*()_-{[}]:;"\'<,|\\>.?/~=+`'

    while tries > 0:
        answer(letters, used_letters, hidden)
        print('\n', *hidden, sep='')

        letter = input('Input a letter:')
        if letter in used_letters:
            print('You already typed this letter')
            continue
        if len(letter) != 1:
            print('You should input a single letter')
            continue
        if letter.isupper() or letter in symbols:
            print('It is not an ASCII lowercase letter')
            continue
        if letter not in used_letters:
            used_letters.append(letter)

        if letter in letters:
            for x in range(len(choice)):
                if letter == choice[x]:
                    hidden.pop(x)
                    hidden.insert(x, letter)
                    print()
        else:
            tries -= 1
            print('No such letter in the word')
    else:
        print('You are hanged!')


def menu():
    choose = input('Type "play" to play the game, "exit" to quit:')
    if choose == 'play':
        play()
    elif choose == 'exit':
        exit()
    else:
        menu()


print('H A N G M A N')
menu()
