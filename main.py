import time, singleplayer
from os import system as sys
from termcolor import colored as css

def title():
    print(css("GUESS.THAT.WORD V2.7! @Noulion\n", 'yellow', attrs=['bold']))
    
def main():
    title()
    def guess():
        title()
        print(css('  hints: ', 'white', attrs=['bold'])+(css(hint, 'light_green', attrs=['bold'])))
        print(css(f"\n  [{trace}] ({wordLenght}) letter word,\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
        
        while True:
            print(css("  [Give Up?, type g]", 'white'))
    
            word_input = input(css("  Guess the word!: ", 'white'))
            if word_input == word: 
                time.sleep(0.6) 
                print(css(f"\n   You guessed '{word}', correct!\n", 'cyan'))
                time.sleep(2.5)
                sys('cls')
                return start_menu()
                
        
            elif word_input == 'g':
                print(css(f"\n   The word was {word}\n", 'light_red')) 
                time.sleep(2.3)
                sys('cls')
                return start_menu()
    
            elif word_input == '': 
                print('\n   Blank isnt a word.\n')
    
            else: 
                time.sleep(0.6)  
                s = "" 
                print(css(f"\n{s:3}Try Again!, '{word_input}' is wrong!!\n", 'light_red'))
            
    print(css("Friend Vs Friend!\nSet Up Your Word\n", 'white'))
    word = input(css("Type a word for someone to guess: ", 'yellow', attrs=['bold']))
    wordLenght= len(word)
    trace = " * " * wordLenght 
    hint = input(css("Type a hint for that word: ", 'yellow', attrs=['bold']))
    
    if word == word.lower():
        text = "The word is lower cased"
    elif word != word.lower():
        text = "The word is capitalized"
    if hint == hint: 
        sys('cls')
        guess()    

def start_menu():
    title()
    print(css("Welcome to Guess That Word V2!.\nThis is a remake of the original,\ndev log:\n\n  Single Player Mode has now been added!\n  New Logo Design\n  You can now input words in terminal for someone to guess!\n  Not much changes\n", 'white', attrs=['bold']))
    
    option = {1:"friend_vs_friend",
              2:"Single_Player",
              3:"Exit"
        }
    for num,option in option.items():
        num = css(num, 'white')
        option = css(option, 'yellow', attrs=['bold'])
        print(f'[{num}]{option}', end='\n')
   
    while True:
        option_choose = input('\n:')
    
        if option_choose == '1':
            sys('cls')
            time.sleep(0.045)
            return main()
        elif option_choose == '2':
            sys("cls")
            time.sleep(0.045)
            return singleplayer.start_menu2()
        elif option_choose == '3':
            time.sleep(0.045)
            break
        else:
            sys('cls')
            return start_menu()
