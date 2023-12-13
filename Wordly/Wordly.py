from random import choice
from colorama import Fore, Style
from os import system
from time import sleep
with open('words.txt', 'r') as f:
    words = list(f.read().split('\n'))

attempts = [
    list('_' * 5),
    list('_' * 5),
    list('_' * 5),
    list('_' * 5),
    list('_' * 5),
    list('_' * 5),
]

def test(user_input, word):
    gameWin = False
    if user_input.upper() == word.upper():
        gameWin = True
    
    s = ''
    for i in range(5):
        if user_input[i] == word[i]:
            s += f'{user_input[i]}+'
        
        elif user_input[i] in word:
            s += f'{user_input[i]}='
        
        else:
            s += f'{user_input[i]}-'
    
    return s, gameWin

def screen(attempts, user):
    if not user:
        pass
    
    else:
        for i in attempts:
            if i[0] != '_':
                continue
        
            else:
                k = 0
                for j in range(1, 10, 2):
                    i[k] = user[j-1:j+1]
                    k += 1
            
                break
            
    print('    Wordly   \n')
    for i in attempts:
        for j in i:
            if j == '_':
                print('|_|', end='')
            
            else:
                if j[1] == '+':
                    print(f'|{Fore.GREEN}{j[0]}{Style.RESET_ALL}|', end='')
                    
                elif j[1] == '=':
                    print(f'|{Fore.YELLOW}{j[0]}{Style.RESET_ALL}|', end='')
                    
                else:
                    print(f'|{Fore.RED}{j[0]}{Style.RESET_ALL}|', end='')
        
        print('\n---------------')
    
    return attempts
        

# Game Start Variables
gameWin = False
user_try = 0
attempts = [
list('_' * 5),
list('_' * 5),
list('_' * 5),
list('_' * 5),
list('_' * 5),
list('_' * 5),
]
word = choice(words).upper()
user = None
while True:
    while True:
        try:
            attempts = screen(attempts, user)
            if user_try == 6 or gameWin:
                break
                
            user = str(input("Enter: ")).upper()
            if not user.isalpha():
                print('Only letters are accepted')
                sleep(1)
                user = None
                system('cls')
                
            elif len(user) != 5:
                print('Count of letters must be 5')
                sleep(1)
                user = None
                system('cls')
                
            else:
                user, gameWin = test(user, word)
                user_try += 1
                system('cls')
                    
        except:
            print('Error ocurred')
            sleep(1)
            user = None
            system('cls')
        
    if gameWin:
        print(f'{Fore.GREEN}You have won the game{Style.RESET_ALL}')
        
    else:
        print(f'{Fore.RED}You have lost the game. Word was: {word}{Style.RESET_ALL}')
        
    break