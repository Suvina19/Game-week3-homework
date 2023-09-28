#Welcome to Escape room
import random
import sys

#Player's data
playerA = {
    "name" : "p1",
}
playerB = {
    "name" : "p2",
}

#Graphic for Sunset island
def printGraphic(name):
    if(name == "Start"):
        print ("         |")
        print ("        \ _ /")
        print ("      -= (_) =-")
        print ("       /   \         _\/_")
        print ("         |           //o\  _\/_ ")
        print ("   _____ _ __ __ ____ _ | __/o\\ _")
        print (" =-=-_-__=_-= _=_=-=_,-'| ---|-,_")

        
    if (name == "VideoGame"):
        print ( "  __________________________")
        print ( " |OFFo oON                  |")
        print ( " | .----------------------. |")
        print ( " | |  .----------------.  | |")
        print ( " | |  |                |  | |")
        print ( " | |  |                |  | |")
        print ( " | |  |                |  | |")
        print ( " | |  |                |  | |")
        print ( " | |  |                |  | |")
        print ( " | |  |                |  | |")
        print ( " | |  |                |  | |")
        print ( " | |  '----------------'  | |")
        print ( " | |__GAME BOY____________/ |")
        print ( " |          ________        |")
        print ( " |    .    (Nintendo)       |")
        print ( " |  _| |_   """"""""   .-.  |")
        print ( " |-[_   _]-       .-. (   ) |")
        print ( " |   |_|         (   ) '-'  |")
        print ( " |    '           '-'   A   |")
        print ( " |                 B        |")
        print ( " |          ___   ___       |")
        print ( " |         (___) (___)  ,., |")
        print ( " |        select start ;:;: |")
        print ( " ----------------------------")
        
#Graphic for envelope        
    if (name == "Envelope"):
        print( "    ...")
        print("  /`   `\ ")
        print(" /       \ ")
        print('|\~~~~~~~/|')
        print('| \=====/ |')
        print("| /`...'\ | ")
        print('|/_______\|')
        
#Graphic for water       
    if (name == "Water"):
        print("               _            ")
        print("              | |")           
        print("__      ____ _| |_ ___ _ __ ")
        print("\ \ /\ / / _` | __/ _ \ '__|")
        print(" \ V  V / (_| | ||  __/ |  ") 
        print("  \_/\_/ \__,_|\__\___|_|  ") 
        
#Graphic for jupitar
    if (name == "Jupiter"):
        print("                      .::.")
        print("                   .:'  .:")
        print("         ,MMM8&&&.:'   .:'")
        print("        MMMMM88&&&&  .:'")
        print("       MMMMM88&&&&&&:'")
        print("       MMMMM88&&&&&&")
        print("     .:MMMMM88&&&&&&")
        print("   .:'  MMMMM88&&&& ")
        print(" .:'   .:'MMM8&&&' ")
        print(" :'  .:'")
        print(" '::' ")
        
#Graphic for Rat        
    if (name == "Rat"):
        print("  ,,==.")
        print("  //    `")
        print(" ||      ,--~~~~-._ _(\--,_")
        print("  \\._,-~   \      '    *  `o")
        print("   `---~\( _/,___( /_/`---~~")
        print("         ``==-    `==-,") 
        
#Graphic for Keyboard
    if (name == "Keyboard"):
        print(",---,---,---,---,---,---,---,---,---,---,---,---,---,-------,")
        print("|1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    |")
        print("|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|")
        print("| ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |")
        print("|-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |")
        print("| Caps | A | S | D | F | G | H | J | K | L | \ | [ | * |    |")
        print("|----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|")
        print("|    | < | Z | X | C | V | B | N | M | , | . | - |          |")
        print("|----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|")
        print("| ctrl |  | alt |                          |altgr |  | ctrl |")
        print("'------'  '-----'--------------------------'------'  '------'")
        
#Graphic for game over        
    if (name == "GameOver"):
        print("Better luck next time")
        print( '   _________    _____   ____     _______  __ ___________ ')
        print( '  / ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \ ')
        print(" / /_/  > __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/")
        print(" \___  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   ")
        print("/_____/     \/      \/     \/                   \/       ")
        
        
#Graphic for title
    if (name == "title"):
        print('      _______. __    __  .__   __.      _______. _______ .___________.    __       _______. __          ___      .__   __.  _______     ')
        print( '    /       ||  |  |  | |  \ |  |     /       ||   ____||           |   |  |     /       ||  |        /   \     |  \ |  | |       \    ')
        print("    |   (----`|  |  |  | |   \|  |    |   (----`|  |__   `---|  |----`   |  |    |   (----`|  |       /  ^  \    |   \|  | |  .--.  |   ")
        print("     \   \    |  |  |  | |  . `  |     \   \    |   __|      |  |        |  |     \   \    |  |      /  /_\  \   |  . `  | |  |  |  |   ")
        print("  ----)   |   |  `--'  | |  |\   | .----)   |   |  |____     |  |        |  | .----)   |   |  `----./  _____  \  |  |\   | |  '--'  |   ")
        print( "|_______/     \______/  |__| \__| |_______/    |_______|    |__|        |__| |_______/    |_______/__/     \__\ |__| \__| |_______/    ")
        print(      )
        print(      )
        print(" _______     _______.  ______     ___      .______    _______    .______        ______     ______   .___  ___.                         ")
        print("|   ____|   /       | /      |   /   \     |   _  \  |   ____|   |   _  \      /  __  \   /  __  \  |   \/   |                         ")
        print("|  |__     |   (----`|  ,----'  /  ^  \    |  |_)  | |  |__      |  |_)  |    |  |  |  | |  |  |  | |  \  /  |                         ")
        print("|   __|     \   \    |  |      /  /_\  \   |   ___/  |   __|     |      /     |  |  |  | |  |  |  | |  |\/|  |                         ")
        print("|  |____.----)   |   |  `----./  _____  \  |  |      |  |____    |  |\  \----.|  `--'  | |  `--'  | |  |  |  |                         ")
        print("|_______|_______/     \______/__/     \__\ | _|      |_______|   | _| `._____| \______/   \______/  |__|  |__|                         ")
        
    return
    
def Game():
    printGraphic("GameOver")
    print("-------------------------------")
    print("Better luck next time! Do you want to try again?")
    print ("yes or no?")
    user = input(">")
    if (user == "yes"):
        Intro()
    else:
        print("See you soon!")
    return

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        Game()

    return result
    
def WalkAhead():
    print("You hear a deep loud voice which says 'Good job on solving the puzzles'")
    print("You are so close to escaping but you need to roll a dice and get a number higher than 5")
    input("press enter >")
    print(" ")
    print("Do you want to roll a dice? yes or no?")
    response = input(">")
    if(response == "yes"):
        print ("Let's roll a dice to see what happens next!")

        # roll a dice from 0 to 20 to see what happens
        # if your number is higher than the difficulty, you win!
        difficulty = 5
        roll = rollDice(0, 20, difficulty)
        
        # if you roll the dice high enough
        if (roll >= difficulty):
            print("The puzzle pieces you won fit perfectly and the door opens!")
            print("But wait! Only one of you can leave. 'Would you leave your friend behind? 'asks the deep voice")
            print("yes or no?")
            test = input(">")
            print("")
            print(" ")
            print(" ")
            if (test == "no"):
                print("You are a good friend! Both of you can leave and enjoy your vacation!")
            elif (test =="yes"):
                print("That's the wrong answer! You are a bad friend! Your friend can leave safely and you are stuck in the room forever!")
                Game()
    

def VideoGame():
    printGraphic("VideoGame")
    print("")
    print("")
    print("You start the video game and enter into a game of trivia")
    print ("What is H2O?")
    move = input(">")
    
    #let player answer
    if (move == "water"):
        print("Good Job! You just earned 15 mins time and a Key")
        printGraphic("Water")
        print("")
        #question2 once first is correct
        print("Here is the next question")
        print("Which is the largest planet?")
        word1 = input(">")
        if (word1 == "jupiter"):
            printGraphic("Jupiter")
            print("Wow that's amazing you got another one right!")   
            #player can choose if they want to play anothre game or walk away    
            print("Do you want to open the 'envelope' or 'walk ahead'")
            answer = input(">")
            if (answer == "envelope"):
                Envelope()
            elif (answer == "walk ahead"):
                WalkAhead()
        else:        
            print("Oh no you just lost 15 mins")
            VideoGame()
    else:        
        print("Oh no you just lost 15 mins")
        VideoGame()
    
def Envelope(): #go to the envelope and find clues
    printGraphic("Envelope")
    print ("It has some riddles")
    print ("The riddle says 'I am full of keys but can't open the locks. What am I? (Hint:You use it to type.)'")
    move = input(">")
    move = move.lower()
    
    if (move == "keyboard"):
        printGraphic("Keyboard")
        print ("That's correct! You won a puzzle piece!")#if answer is correct it goes to next question
        print ("Here is the second riddle")
        print(" ")
        print ("I am a small animal with a tail and I like eating cheese. I rule the streets in New York. My name starts with an 'R'. Who am I?")
        print("")
        answer1 = input(">")
        if(answer1 == "rat"):
            print ("That's right! You just won extra time!")
            printGraphic("Rat")#if this is right player can play another game or go to exit and roll a dice
            print("Do you want to play the 'video game' or 'walk ahead' ")
            answer2 = input(">")
            if(answer2 == "video game"):
                VideoGame()
            elif(answer2 == "walk ahead"):
                WalkAhead()
        else:
            print("you just lost 10 mins")
            Envelope()
    else:
        print("you just lost 10 mins")
        Envelope()


def Intro(): #Gets names from players to start the introduction
    print("Whats your name?")
    playerA["name"] = input("Please enter your name : ")
    print("What's your friend's name?")
    playerB["name"] = input("Please enter your friend's name : ")
    print(" ")
    print(" ")
    print(" ")
    print (playerA["name"]+ " and " + playerB["name"] + " have won a free trip to sunset island in a lucky draw competetion")
    print ("You both were ecstatic and quickly packed your bags for the much-anticipated vacation.")
    print ("The island promised endless fun, picturesque sunsets, and a luxurious resort experience.")
    print ("As soon as you arrived, you couldn't wait to explore the beauty of the island.")
    
    input("Press Enter>")
    print("")
    print("The days were filled with beach activities, water sports, and relaxation by the pool. ")
    print ("Everything seemed perfect until one mysterious night.")
    
    input("Press Enter>")
    print(" ")
    print("One evening, while at the resort's club, you and your friend decided to enjoy some nightlife on the island.")
    print("Suddenly, the music stopped, and the club's lights dimmed.") 
    print("Panic set in as the floor beneath you seemed to give way, and you found yourselves falling into darkness.") 
    print("You landed with a thud in a dimly lit, unfamiliar room. Confused and disoriented, you realized that you were trapped.")
    print("")
    print("")
    
def Instructions():    #gives instructions to the player
    input("Press Enter>")
    print("Game Instructions")
    print("As you explored the room, you discovered clues, puzzles, and symbols scattered around.") 
    print("It became clear that escaping this mysterious room was your only way out. To do so, you must:")
    print("Find Hidden Clues: Search the room for hidden clues and objects that might help you escape.")
    print("Solve Puzzles: Solve intricate puzzles and riddles that hold the key to unlocking the room.")
    print("Race Against Time: You must escape before the sunrise; otherwise, you'll be trapped forever.") 
    print()
    print()
    print("You see two objects")
    
    input ("Press Enter>")
    print("Which object do you want to examine video game or envelope? : ")
    print()
    
    #player can choose envelope or video game
    move = input(">")
    print("")
    # give players to choose two options
    if (move == "video game"):
        print("You chose video game and enter into the trivia quiz game")
        VideoGame()    #call video game to play trivia
    
    elif (move == "envelope"):
        print("You open the envelope")
        Envelope()     #call envelope to solve riddles
    
    else:
        print("Invalid input. Please type carefully")
        Instructions()
    
def main():
    printGraphic("title")# print title graphic
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    
    printGraphic("Start")# print sunset island graphic
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    
    Intro() # START INTRO
    Instructions() #Give Instructions
    
main() #first thing that happens
    
    
      
    
    




    

        

  
        
        
        
