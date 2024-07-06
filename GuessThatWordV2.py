import time 
from os import system as sys
from termcolor import colored as css


    
def title():

    
    print(css(f"""
      ╮╭┻┻╮╭┻┻╮╭▕╮╲
     ▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏
     ▕╭┻┻┻┛┗┻┻┛ ╰▏▕  GUESS.THAT.WORD V2! @Noulion   
     ▕╰━━━┓┈┈┈╭╮▕╭╮▏  
     ▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏
     ▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏
     """, 'yellow', attrs=['bold']))

def main():
    
    def guess():
        title()
        print(css('  hints: ', 'white', attrs=['bold'])+(css(hint, 'light_green', attrs=['bold'])))
        print(css(f"\n  [{trace}] ({wordLenght}) letter word,\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
        
        
        

        while True:
            print(css("  [Give Up?, type g]", 'white'))
    
            try_i = input(css("  Guess the word!: ", 'white'))
            if try_i == word: 
                time.sleep(0.6) 
                print(css(f"\n   You guessed '{word}', correct!\n", 'cyan'))
                time.sleep(2.5)
                sys('clear')
                return start_menu()
                break
                
        
            elif try_i == 'g':
                print(css(f"\n   The word was {word}\n", 'light_red')) 
                time.sleep(2.3)
                sys('clear')
                return start_menu()
                break
    
            elif try_i == '': 
                print('\n   Blank isnt a word.\n')
    
            else: 
                time.sleep(0.6)  
                s = "" 
                print(css(f"\n{s:3}Try Again!, '{try_i}' is wrong!!\n", 'light_red'))
    
    title()
    print(css("\nSet-Up Menu\n", 'white'))
    word = input(css("Type a word for someone to guess: ", 'yellow', attrs=['bold']))
    wordLenght= len(word)
    trace = " * " * wordLenght 
    hint = input(css("Type a hint for that word: ", 'yellow', attrs=['bold']))
    
    if word == word.lower():
        text = "The word is lower cased"
    elif word != word.lower():
        text = "The word is capitalized"
    if hint == hint: 
        sys('clear')
        guess()
      
def start_menu():
    title()
    print(css("\nWelcome to Guess That Word V2!.\nThis is a remake of the original,\ndev log:\n\n  New Logo Design LMAOOO\n  You can now input words in terminal for someone to guess!\n  Not much changes\n", 'white', attrs=['bold']))
    
    option = {1:"friend vs friend",
              2:"Man vs Ai (soon!)",
              3:"Exit"
        }
    for num,option in option.items():
        num = css(num, 'white')
        option = css(option, 'yellow', attrs=['bold'])
        print(f'[{num}]{option}', end='\n')
   
    while True:
        option_choose = input('\n:')
    
        if option_choose == '1':
            sys('clear')
            main()
            break
        elif option_choose == '2':
            sys('clear')
            return start_menu()
        elif option_choose == '3':
            break
        else:
            sys('clear')
            return start_menu()
start_menu()