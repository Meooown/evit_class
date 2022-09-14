"""
Space ball assignment
Created by @Meooown on Github
Created 9/12/2022
Last updated 9/12/2022
"""

#Librarie(s)
import random

#Variable(s)
current_team = 1 
previous_inning = 0
inning = 1
strikeouts = 0
user_score = 0
ai_score = 0
bat_outcome = 0
user_name = ''

#input
user_name = input("What is the name of your team? ").title()

#intro
print("Today you're up against the Miami Martians. Good luck!")
print()

#Game logic
while inning < 10:

    #This prints out the "inning" message if a new inning has started
    if current_team == 1:
        print("Inning: " + str(inning))
        print("=========")
    
    if current_team == 1:    #If the AI is batting
        print("Team 1 Batting: Miami Martians") 
        
        #Will loop a rendom chance of scoring a home run and strike out
        #until 3 strike outs have been reached
        while strikeouts != 3:
            bat_outcome = random.randint(1,3)
            if bat_outcome == 1:
                print("A home run!")
                ai_score += 1
            else:
                print("A strikeout!")
                strikeouts += 1 
    else:    #If the user is batting
        print("Team 2 Batting: " + user_name) 
        while strikeouts != 3:
            bat_outcome = random.randint(1,3)
            if bat_outcome == 1:
                print("A home run!")
                user_score += 1
            else:
                print("A strikeout!")
                strikeouts += 1
    strikeouts = 0
    #The score after each round
    print("The score is Miami Martians " + str(ai_score) + ", " + str(user_name)
          + " " + str(user_score) + ".")
    
    print("Press enter to continue")
    input()
    #incrementing the inning and current team by necessary amount
    current_team = (current_team % 2) + 1
    if current_team == 1:
        inning += 1

print("\nThe game is over!")
input("Press enter to end the program.")



