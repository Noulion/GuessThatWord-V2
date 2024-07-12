import time
import random 
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
    
def Ai_game():
    title()
    def Ai_choose(word):
        title()
        text = "The word is capitalized"
        wordLenght= len(word)
        trace = " * " * wordLenght
        diffculty = ("Easy", "Medium", "Hard")

        def Ai_guess(word):
            while True:
                print(css("  [Give Up?, type g]", 'white'))
    
                try_i = input(css("  Guess the word!: ", 'white'))
                if try_i == word: 
                    time.sleep(0.6) 
                    print(css(f"\n   You guessed '{word}', correct!\n", 'cyan'))
                    time.sleep(2.5)
                    sys('cls')
                    return start_menu()
                    break
                
        
                elif try_i == 'g':
                    print(css(f"\n   The word was {word}\n", 'light_red')) 
                    time.sleep(2.3)
                    sys('cls')
                    return start_menu()
                    break
    
                elif try_i == '': 
                    print('\n   Blank isnt a word.\n')
    
                else: 
                    time.sleep(0.6)  
                    s = "" 
                    print(css(f"\n{s:3}Try Again!, '{try_i}' is wrong!!\n", 'light_red'))

        if word == "Astronaut":
            hint = "A person trained to travel and work in space."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Molecule":
            hint = "The smallest unit of a chemical compound, consisting of atoms bonded together."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Apple":
            hint = "A common fruit that can be red, green, or yellow."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Galaxy":
            hint = "A massive system of stars, stellar remnants, interstellar gas, dust, and dark matter, bound together by gravity."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[2]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Fish":
            hint = "An aquatic animal with gills and fins."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Book":
            hint = " An item you read, often made of pages bound together."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Pyramid":
            hint = " A monumental structure with a square base and four triangular sides that meet at a point, often found in Egypt."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)
        
        elif word == "Car":
            hint = "A vehicle with four wheels used for transportation."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Photosynthesis":
            hint = "The process by which green plants use sunlight to synthesize food from carbon dioxide and water."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Quixotic":
            hint = "Extremely idealistic, unrealistic, and impractical."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[2]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Cake":
            hint = " A sweet dessert often eaten on birthdays."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Oasis":
            hint = "A fertile spot in a desert where water is found."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Tsunami":
            hint = " A large sea wave caused by an underwater earthquake or volcanic eruption."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == "Sesquipedalian":
            hint = "Pertaining to the use of long words."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,\n  {diffculty[2]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

        elif word == " A speech in a play where a character speaks their thoughts aloud, usually alone on stage.":
            hint = "A person trained to travel and work in space."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[2]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            Ai_guess(word)

    words = ["Astronaut",
            "Molecule",
            "Apple",
            "Galaxy ",
            "Fish",
            "Book",
            "Pyramid",
            "Car",
            "Photosynthesis",
            "Quixotic",
            "Cake",
            "Oasis",
            "Tsunami",
            "Sesquipedalian",
            "Soliloquy"]
    
    for  rd in words:
        rd_counter = 0
        randomizer = random.choice(words)
        rd_counter+=1
        print(f"{randomizer}")
        if rd_counter == 1:
            break
    randomizer = randomizer
    print(randomizer)
    word = randomizer
    
    if randomizer == randomizer:
        sys('cls')
        Ai_choose(randomizer)

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
                sys('cls')
                return start_menu()
                break
                
        
            elif try_i == 'g':
                print(css(f"\n   The word was {word}\n", 'light_red')) 
                time.sleep(2.3)
                sys('cls')
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
        sys('cls')
        guess()    

def start_menu():
    title()
    print(css("\nWelcome to Guess That Word V2!.\nThis is a remake of the original,\ndev log:\n\nSingle Player Mode has now been added!\n  New Logo Design\n  You can now input words in terminal for someone to guess!\n  Not much changes\n", 'white', attrs=['bold']))
    
    option = {1:"friend vs friend",
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
            main()
            break
        elif option_choose == '2':
            sys('cls')
            return Ai_game()
            break
        elif option_choose == '3':
            break
        else:
            sys('cls')
            return start_menu()
