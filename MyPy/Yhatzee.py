"""
Yhatzee
Created by @Meooown on Github
Created 9/23/2022
Last updated 10/13/2022
"""

## -- Setup -- ##

####import libraries

import random

####variable creation

reroll_chances = 3
user_score = 0
turns = 1
rolls_logic = []
reroll_choice = []
dice_faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
valid_options = ['1', '2', '3', '4', '5',]
valid_scoring_options = ["1: Ones", "2: Twos", "3: Threes", "4: Fours",
                         "5: Fives", "6: Sixes", "7: Three of a kind",
                         "8: Four of a kind", "9: Full house",
                         "10: Small straight", "11: Large straight",
                         "12: Yahtzee", "13: Chance"]
valid_scoring_options_logic = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                               "10", "11", "12", "13"]

####function creation

##This function is the first used to create the initial dice roll. This
##is run after every main loop of the game.

def roll_dice():
    dice_faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    rolls = []
    rolls_logic = []
    loop_killer = 0
    
    while loop_killer != 5:
        random_roll = random.randint(0,5)
        rolls.append(dice_faces[random_roll])
        rolls_logic.append(random_roll + 1)
        loop_killer += 1
    return(rolls_logic, rolls)

##This function is used to reroll dice if the user chooses too, keeping
##the desired held dice in the same position and rerolling the unheld
##dice.

def reroll(rolls_logic, reroll_choice, rolls):
    dice_faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    random_roll = 0
    increment_helper = 0

    for i in range(len(rolls_logic)):
        if (i+1) not in reroll_choice:
            random_roll = random.randint(0,5)
            rolls[i] = dice_faces[random_roll]
            rolls_logic[i] = (random_roll + 1)
            
    return rolls_logic, rolls

###This function asks the user which dice they want to reroll, adding
##them to a dignified list if it is valid and returning said list.

def ask_reroll(continu):
    instructions_printed = False
    reroll_choice = []
    
    while continu != '':
        if not instructions_printed:
            print("Enter the spot number the die is on of a dice you would"
                  " like to hold. (1-5). \nEnter nothing to reroll ")
            instructions_printed = True
            
        continu = input("Enter a dice: ")
        
        if continu in valid_options:
            continu = int(continu)
            reroll_choice.append(continu)
            
    rolls_logic = list(set(reroll_choice))
            
    return(reroll_choice)

##This function is called after all dice are finalized, giving the user
##the options for scoring they have left and running their answer
##through the scoring_math function to get the number of points scored.
##Afterwards, it will remove the option from further use.

def scoring(valid_scoring_options, valid_scoring_options_logic,
            rolls_logic, user_score):
    print()
    print("Please choose a scoring options to add too your score")
    
    for i in range(7):
        if 0 <= i < 2:
            spacing = "             "
        elif i == 2:
            spacing = "           "
        else:
            spacing = "            "
        if i != 6:
            print(valid_scoring_options[i] + spacing +
                  valid_scoring_options[i+7])
        else:
            print(valid_scoring_options[6])
            
    user_choice = input()
    
    if user_choice not in valid_scoring_options_logic:
        while user_choice not in valid_scoring_options_logic:
            print("Please enter a valid option. Valid option cannot be one"
                  " you have already used.")
            user_choice = input()
    
    user_choice = int(user_choice)
    user_choice -= 1
    user_score += scoring_math(user_choice, rolls_logic)

    x = valid_scoring_options[user_choice].replace \
                                (str(user_choice + 1), "XX")
    valid_scoring_options[user_choice] = x
    valid_scoring_options_logic.remove(str(user_choice + 1))
    
    return user_score, valid_scoring_options, valid_scoring_options_logic

##This function is used to calculate the users score based on their
##chosen scoring method. It will calculate the points they accululated,
##then return the number of points they got, along with printing a
##message telling the user how many points they got. This function
##should only be used within the scoring function.

def scoring_math(user_choice, rolls_logic):
    iteration_score = 0

    #Ones to sixs
    
    if 0 <= user_choice <= 5:
        for i in rolls_logic:
            if i == (user_choice + 1):
                iteration_score += (user_choice + 1)

    #Three of a kind
        
    elif user_choice == 6:
        for i in range(1,6):
            if rolls_logic.count(i) >= 3:
                for j in rolls_logic:
                    iteration_score += j
                break

    #Four of a kind
            
    elif user_choice == 7:
        for i in range(1,6):
            if rolls_logic.count(i) >= 4:
                for j in rolls_logic:
                    iteration_score += j
                break

    #Full house 
            
    elif user_choice == 8:
        for i in range(1,6):
            if rolls_logic.count(i) == 3:
                for j in range(1,6):
                    if rolls_logic.count(j) == 2:
                        iteration_score += 25
                break

    #Small straight (four in a row)
            
    elif user_choice == 9:
        rolls_logic.sort()
        rolls_logic = list(set(rolls_logic))
        if (len(rolls_logic) == 4 and (rolls_logic[-1] - rolls_logic[0]) == \
           3) or len(rolls_logic) == 5:
            iteration_score += 30

    #large straight (five in a fow)
            
    elif user_choice == 10:
        rolls_logic = list(set(rolls_logic))
        if len(rolls_logic) == 5:
            iteration_score += 40

    #yhatzee (five of a kind)
            
    elif user_choice == 11:
        rolls_logic = list(set(rolls_logic))
        if len(rolls_logic) == 1:
            iteration_score += 50

    #Chance (sum of all)
            
    elif user_choice == 12:
        for i in rolls_logic:
            iteration_score += i

    print()

    if iteration_score == 0:
        print("You have gained no points this round. A shame.")
    else:
        print("You have gained " + str(iteration_score) + " points this "
              "round.")
        
    return iteration_score

## -- Begining of game -- ##

####introduction

print("Welcome to Yahtzee! Roll five dice and try to get specific\n"
      "combinations to get the highest score possible!\nTo start, press"
      " enter.")
input()
print("---------------------------------------")

####Main game loop

while turns != 14 :

    print("Turn " + str(turns) + ": " + str(user_score) + " points.")
    print()
    
    rolls_logic, rolls = roll_dice()
    print(rolls)
    print(rolls_logic)

    while reroll_chances != 0:
        continu = input("You have " + str(reroll_chances) + " rerolls left."
                        " Would you like to reroll? (y/n) :").lower() == 'y'

        if continu:
            print()
            
            reroll_choice = ask_reroll(continu)
            rolls_logic, rolls = reroll(rolls_logic, reroll_choice, rolls)
            
            print()
            print(rolls)
            print(rolls_logic)
        else:
            break
        
        reroll_chances -= 1
        
    else:
        print("You are out of reroll opprotunities")

    user_score, valid_scoring_options, valid_scoring_options_logic \
    = scoring(valid_scoring_options, valid_scoring_options_logic,
              rolls_logic , user_score)

    turns += 1
    reroll_chances = 3
    print()
    print("---------------------------------------")

print()
print()
print("Game finish! You have ended with a total of " + str(user_score) + " points!")
    #add a cpu if you feel like it. imma be honest i dont rn.
