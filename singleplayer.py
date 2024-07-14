import time, random, main
from os import system as sys
from termcolor import colored as css

def title():
    print(css("GUESS.THAT.WORD V2.7! @Noulion\n\n", 'yellow', attrs=['bold']))
    
def singleplayer():
    def choose(word):
        title()
        text = "The word is capitalized"
        wordLenght= len(word)
        trace = " * " * wordLenght
        diffculty = ("Easy", "Medium", "Hard", "Impossible for basic english speakers")

        def guess(word):
            Tries = 1
            while Tries != 8:
                print(css(f"\n  You only get 7 Tries || Tries [{Tries}]\n  [Give Up?, Type (g) \\ Leave?, Type (x)]", 'white'))
    
                word_input = input(css("  Guess the word!: ", 'white'))
                if word_input == word: 
                    time.sleep(0.6)
                    if Tries == 1:
                         print(css(f"\n   You guessed '{word}' in {Tries} Try, Nice you are good!\n", 'cyan'))
                    elif Tries <= 4:
                        print(css(f"\n   You guessed '{word}' in {Tries} Tries, Nice you are good!\n", 'cyan'))
                    else:
                        print(css(f"\n   You guessed '{word}' in {Tries} Tries, Better luck next time..\n", 'cyan'))
                    time.sleep(2.5)
                    sys('cls')
                    return singleplayer()
                    break
                
        
                elif word_input == 'g':
                    print(css(f"\n   The word was {word}\n", 'light_red')) 
                    time.sleep(2.3)
                    sys('cls')
                    return singleplayer()
                    break

                elif word_input == 'x':
                    print(css(f"\n   The word was {word}, exiting...\n", 'light_red')) 
                    time.sleep(2.3)
                    sys('cls')
                    return start_menu2()
                    break
    
                elif word_input == '': 
                    print('\n   Blank isnt a word.')
                    Tries+=1

                    if Tries == 7:
                        print(css("   You have one last try!", "red"))
    
                else: 
                    time.sleep(0.6)  
                    s = "" 
                    print(css(f"\n{s:3}Try Again!, '{word_input}' is wrong!!", 'light_red'))
                    Tries+=1

                    if Tries == 7:
                        print(css("   You have one last try!\n", "red"))
            return singleplayer()

        if word == "Astronaut":
            hint = "A person trained to travel and work in space."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Molecule":
            hint = "The smallest unit of a chemical compound, consisting of atoms bonded together."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Apple":
            hint = "A common fruit that can be red, green, or yellow."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Galaxy":
            hint = "A massive system of stars, stellar remnants, interstellar gas, dust, and dark matter, bound together by gravity."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[2]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Fish":
            hint = "An aquatic animal with gills and fins."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Book":
            hint = " An item you read, often made of pages bound together."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Pyramid":
            hint = " A monumental structure with a square base and four triangular sides that meet at a point, often found in Egypt."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)
        
        elif word == "Car":
            hint = "A vehicle with four wheels used for transportation."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Photosynthesis":
            hint = "The process by which green plants use sunlight to synthesize food from carbon dioxide and water."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Quixotic":
            hint = "Extremely idealistic, unrealistic, and impractical."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[3]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Cake":
            hint = " A sweet dessert often eaten on birthdays."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Oasis":
            hint = "A fertile spot in a desert where water is found."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Tsunami":
            hint = " A large sea wave caused by an underwater earthquake or volcanic eruption."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Sesquipedalian":
            hint = "Pertaining to the use of long words."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,\n  {diffculty[3]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)

        elif word == "Chair":
            hint = "A piece of furniture you sit on."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)
        
        elif word == "Sun":
            hint = "The star at the center of our solar system."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[0]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)
            
        elif word == "Carnivore":
            hint = "An animal that eats only meat."
            print(css('  hints: ', 'white', attrs=['bold'])+(css(f"{hint}", 'light_green', attrs=['bold'])))
            print(css(f"\n  [{trace}] ({wordLenght}) letter word,  {diffculty[1]}\n  {text}", 'yellow', attrs=['bold']), '\n\n\n')
            guess(word)    

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
            "Chair",
            "Sun", 
            "Carnivore",]
    
    title()
    for  rd in words:
        rd_counter = 0
        randomizer = random.choice(words)
        rd_counter+=1
        print(f"{randomizer}")
        if rd_counter == 1:
            break
    randomizer = randomizer
    print(randomizer)
    
    if randomizer == randomizer:
        sys('cls')
        choose(randomizer)
 

def start_menu2():
    title()
    print(css("Single Player Mode : \n", 'white', attrs=['bold']))
    option = {1:"Start",
              2:"Go back"
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
            return singleplayer()
        elif option_choose == '2':
            sys('cls')
            time.sleep(0.045)
            return main.start_menu()
            break
        else:
            sys('cls')
            return start_menu2()