from random import randint
import os
import time
import sys
option = ["Rock", "Paper", "Scissors"]
# Welcome to my game of Rock Paper Scissors!!!
#--------------------------------------------------------------------
# Assigns a random play to the computer
computer = option[randint(0,2)]

# For Human v. Computer
comp = 0
play = 0
#set player to False
player = False
# For Human v. Human
play1 = 0
play2 = 0
kpop = False
print("")
print("Loading Rock-Paper-Scissors.py", end = '')
def writeText(string, t):
    i = 0
    while i < len(string):
        print(string[i], end = '')
        time.sleep(float(t))
        i += 1
        sys.stdout.flush()

writeText("...", 1)
time.sleep(2)
os.system('clear')

print("")
print("         --------        ------------    \          /  ")
print("        /        \       |          |     \        / ")
print("       /          \      |          |      \      /       ")
print("      (            )     |          |       \    / ")
print("      |            |     |          |        \**/ ")
print("      |            |     |          |         /\    ")
print("       \          /      |          |    ____/--\____     ")
print("        \        /       |          |    |[  ]  [  ]|       ")
print("         \------/        ------------    |[__]  [__]|        ")
print("")
print(" Rock Paper Scissors! ")


oppo = 0
while oppo == 0:
    print("Rock Paper Scissor Game Menu: ")
    print("1) Human vs. Computer")
    print("2) Human vs. Human")
    print("3) Help/How To Play?")
    print("4) Quit")
        
    print("What option will you choose: ")
    menu = input("Input a number to begin: ")
    if menu == "1":
        # Human vs. Computer:
        os.system('clear')
        print("Human vs. Computer Mode:")
        print("Note that first letter should be capital.")
        print("")
        while player == False:
        #set player to True
            player = input("What do you choose?? ")
            if player == computer:
                print("It's a Tie!")
            elif player == "Rock":
                if computer == "Paper":
                    print("You lost!", computer, "covers", player)
                    comp += 1
                else:
                    print("You win!", player, "obliterates", computer)
                    play += 1
            elif player == "Paper":
                if computer == "Scissors":
                    print("You lost!", computer, "cuts", player)
                    comp += 1
                else:
                    print("You win!", player, "covers", computer)
                    play += 1
            elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                    comp += 1
                else:
                    print("You win!", player, "cuts", computer)
                    play += 1
            else:
                print("Please enter a valid input...")
            print( "Computer: " + str(comp))
            print( "Player: " + str(play))
            if comp >= 3:
                player = True
                os.system('clear')
                print("You lost the game!")
                time.sleep(2)
                print("Better luck next time!")
                time.sleep(2)    
                break
            elif play >= 3:
                print("Congratulations! You have won the game!!")
                time.sleep(2)
                print("Thanks for Playing!")
                time.sleep(2)
                break
            else:
                pass
            player = False
            computer = option[randint(0,2)]
    elif menu == "2":
        time.sleep(0.5)
        os.system('clear')
        print("Human vs. Human Mode:")
        print("Note that first letter should be capital.")
        print("")
        
        while kpop == False:
        #set player to True
            print("Player 1's Turn")
            player1 = input("What do you choose?? ")
            os.system('clear')
            print("Player 2's Turn:")
            player2 = input("What do you choose?? ")
            os.system('clear')
            if player1 == player2:
                print("It's a Tie!")
            elif player1 == "Rock":
                if player2 == "Paper":
                    print("Player 2 wins!", player2, "covers", player1)
                    play2 += 1
                else:
                    print("Player 1 won!", player1, "obliterates", player2)
                    play1 += 1
            elif player1 == "Paper":
                if player2 == "Scissors":
                    print("Player 2 wins!", player2, "cuts", player1)
                    play2 += 1
                else:
                    print("Player 1 won!", player1, "covers", player2)
                    play1 += 1
            elif player1 == "Scissors":
                if player2 == "Rock":
                    print("Player 2 wins!", player2, "smashes", player1)
                    play2 += 1
                else:
                    print("Player 1 won!", player1, "cuts", player2)
                    play1 += 1
            else:
                print("Please enter a valid input...")
            print( "Player1: " + str(play1))
            print( "Player2: " + str(play2))        
            if play1 >= 3:
                kpop = True
                os.system('clear')
                print("Player 1 won the game!")
                time.sleep(2)
                print("Congratulations!")
                time.sleep(2)
                print("Better luck next time Player 2!")
                time.sleep(2)   
                print("Thanks for Playing!")
                break
            elif play2 >= 3:
                kpop = True
                os.system('clear')
                print("Player 2 won the game!")
                time.sleep(2)
                print("Congratulations!")
                time.sleep(2)
                print("Better luck next time Player 1!")
                time.sleep(2)    
                break
                print("Thanks for Playing!")
                time.sleep(2)
                break
            else:
                pass
            kpop = False
    elif menu == "3":
        time.sleep(0.5)
        os.system('clear')
        print("")
        print("• The game starts by asking you which mode you want to play in.")
        time.sleep(2.5)
        print("• You can choose either Human v. Human or Human v. Computer mode.")
        time.sleep(2.5)
        print("• If you choose Human v. Human, you play between you and another person.")
        time.sleep(2.5)
        print("• The first person to reach 3 wins, wins!.")
        time.sleep(2.5)
        print("• If you choose Human v. Computer, you play against an computer.")
        time.sleep(2.5)
        print("• The first player to reach 3 wins, wins!.")
        time.sleep(2.5)
        print("Ready to proceed?                                                                            ")
        proceed = input("Type Yes or No: ")
        zz = 0
        while zz == 0:
            if proceed == "Yes" or proceed == "yes":
                zz += 1
            elif proceed == "No" or proceed == "no":
                print("Okay I'll wait...")
                time.sleep(5)
                proceed = input("Ready now? ")
            else:
                print ("Please print Yes or No.")
                proceed = input()            
        time.sleep(1)
        print("Good luck and have Fun!!                                                                     ")
        time.sleep(2)
        print("")
        os.system('clear')
    elif menu == "4":
        os.system('clear')
        print("")
        print("Quitting so soon??")
        time.sleep(1.5)
        print("oh well...")
        time.sleep(1.5)
        print("Please play again some time!!!!")
        time.sleep(2)
        sys.exit()
    else:
        print("Please input a number between 1 and 4.")



    
