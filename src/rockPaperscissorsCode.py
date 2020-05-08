'''
Created on Feb 1, 2020

@author: ITAUser
'''
#Objective:
#This program will allow the user to play Rock Paper Scissors against the computer
#-We will...
#-create code that checks who won each round
#-create code that takes the input(choices) from the user
#-create code that takes 'input' from the computer
#-check if the user wants to quit OR if the user doesn't enter one of the options
#-loop each round of the game
#-add statements at the end and beginning that welcome and thank the user for playing
#-loop the whole game, so that they can keep playing until they choose to quit

#Pseudocode:
#set variable keepPlaying to true
keepPlaying = True
#While keepPlaying is true:
    #print statement welcoming player to the game
print("Welcome To Rock! Paper! Scissors!")
    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)
print("Rules: Best 2 out of 3. Press Q to quit")
    #make a key that assigns a number to each choice for the computer
Key = ["Rock","Paper","Scissors"];
Key[0] = "Rock"
Key[1] = "Paper"
Key[2] = "Scissors"
    #(rock is 1, scissors is 2, paper is 3)
     
    #import the random function - the computer makes its choice randomly from this function
import random
index = random.randint(0,2)
    #set computer's score to 0
computerScore = 0
    #set player's score to 0
playerScore = 0
    #while player's score is less than 2 and computer's score is less than 2: -- thins means that the game is still on
while((playerScore < 2) or (computerScore < 2)):
        
        #computer's choice = random number between 1 and 3 (random function gets used here)
        computerChoice = Key[index]
        #player's choice = input(ask player to select rock, paper, or scissors)
        playerInput = input("Choose a move")
        return playerInput.lower()
        #start checking user options
        if playerInput == 1:
            playerChoice = "rock"
        elif playerInput == 2:
            playerChoice = "paper"
        elif playerInput == 3:
            playerChoice = "scissors"
        elif playerInput == "Q":
            keepPlaying = False
        else:
            print("Your input was invalid")
        #useChoice = userChoice.lower()
        #if player inputs 'q': --player wants to end the game
        #   set keepPlaying to false -- ends the loop
        #   stop the loop --whoo! break statement
        
        #else if (player inputs rock and computer chooses rock) or 
        if playerChoice == computerChoice:
        #(player inputs paper and computer chooses paper) or
        #(player inputs paper and computer chooses scissors):
        #   print out DRAW
        #   print out player's score and computer's score
            print("Draw")
            print("Your Score: "+playerScore)
            print("Computer Score: "+computerScore)
        #else if (player inputs rock and computer chooses scissors) or
        #(player inputs paper and computer chooses paper) or 
        #(player inputs paper and computer chooses scissors):
        elif (playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "Scissors" and computerChoice == "paper") or (playerChoice == "paper"and computerChoice == "rock"):
        #   add one to the player's score
        #   print out player's score and computer's score
        
        #else if (player inputs rock and computer chooses paper) or
        #(player inputs scissors and computer chooses rock) or 
        #(player inputs paper and computer chooses scissors):
        #   add one to the computer's score
        #   print out player's score and computer's score
        
        #else:
        #   tell the user their input was not valid
        
    #print statement thanksgiving the player for playing
    #if player's score is 2:
    #    print statement letting player know they won
    #if computer's score is 2
    #    print statement letting player know the computer won
    #print out player's score and computer's score