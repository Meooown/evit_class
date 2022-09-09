"""
statistic converter
Created by @Meooown on Github
Created 9/8/2022
Last updated 9/9/2022
"""

##--Setup--##

#import(s)
import random

#function creation(s)
def valid_input_checker(answers):
    """
    This function will take in predetermined answers as an
    argument, then will ask the user to input an answer. if the
    user answer is not inside the list of valid answers, the 
    function will tell the user so and loop an input statement
    until the answer is valid. The function will return the user
    answer once it is correct.
    """
    user_answer = input()
    while user_answer not in answers:
        print("I didnt get that. please try again.")
        user_answer = input()
    return(user_answer)
    
#variable creation
user_choice = ''
given_number = ''
first_number = 0
answer = 0
goodbye_adjective = ["great", "fantastic", "amazing", "spectacular"
                      , "good", "extravagant"]
valid_answers = []

##--introduction--##

#opening prompt to guide the user
print(
    'Welcome to the free converter app. To start, please enter an'
    ' option from the list below.')

while True:    #The start of the main loop
    print(
          "1) miles <--> kilometers"
          "\n2) meters <--> feet"
          "\n3) grams <--> lbs"
          "\n4) celsius <--> kelvin"
          "\n5) fahrenheit <--> celsius")
    valid_answers = ['1','2','3','4','5']
    user_choice = valid_input_checker(valid_answers)
    print()
    

    #If user choice is equal to one, the program will run the code to
    #convert miles to kilometers
    if user_choice == '1':
        valid_answers = ['miles', 'MILES', 'Miles', 'kilometers'
                         ,'Kilometers', 'KILOMETERS']
        print("What is the first measurement in? (miles/kilometers)")
        given_number = valid_input_checker(valid_answers).lower()
        first_number = float(input("What is the given number?\n"))
        print("\ncalculating...")
    
        #math and output
        if given_number == 'kilometers':
            answer = first_number * 0.62137
            print(str(first_number) + " kilometers is equal to " 
                  + str(answer) + " miles.")
        elif given_number == 'miles':
            answer = first_number * 1.60934
            print(str(first_number) + " miles is equal to " 
                  + str(answer) + " kilometers.")
            
    #If user choice is equal to two, the program will run the code to
    #convert meters to feet
    elif user_choice == '2':
        valid_answers = ['feet', 'FEET', 'Feet', 'Meters'
                         ,'METERS', 'meters']
        print("What is the first measurement in? (feet/meters)")
        given_number = valid_input_checker(valid_answers).lower()
        first_number = float(input("What is the given number?\n"))
        print("\ncalculating...")
        
        #math and output
        if given_number == 'meters':
            answer = first_number * 3.281
            print(str(first_number) + " meters is equal to " 
                  + str(answer) + " feet.")
        elif given_number == 'feet':
            answer = first_number / 3.281
            print(str(first_number) + " feet is equal to " 
                  + str(answer) + " feet.")
            
    #If user choice is equal to three, the program will run the code to
    #convert grams into pounds
    elif user_choice == '3':
        valid_answers = ['grams', 'GRAMS', 'Grams', 'pounds'
                         ,'Pounds', 'POUNDS', 'LBS', 'lbs', 'Lbs']
        print("What is the first measurement in? (grams/pounds)")
        given_number = valid_input_checker(valid_answers).lower()
        first_number = float(input("What is the given number?\n"))
        print("\ncalculating...")
        
        #math and output
        if given_number == 'grams':
            answer = first_number / 453.6
            print(str(first_number) + " grams is equal to " 
                  + str(answer) + " pounds.")
        elif given_number == 'pounds' or given_number == 'lbs':
            answer = first_number * 453.6
            print(str(first_number) + " pounds is equal to " 
                  + str(answer) + " grams.")
            
    #If user choice is equal to four, the program will run the code to
    #convert celsius to kelvin
    elif user_choice == '4':
        valid_answers = ['Celsius', 'CELSIUS', 'celsius', 'Kelvin'
                         ,'KELVIN', 'kelvin']
        print("What is the first measurement in? (celsius/kelvin)")
        given_number = valid_input_checker(valid_answers).lower()
        first_number = float(input("What is the given number?\n"))
        print("\ncalculating...")
        
        #math and output
        if given_number == 'celsius':
            answer = first_number + 273.15 
            print(str(first_number) + " celsius is equal to " 
                  + str(answer) + " kelvin.")
        elif given_number == 'kelvin':
            answer = first_number - 273.15 
            print(str(first_number) + " celsius is equal to " 
                  + str(answer) + " kelvin.")

    #If user choice is equal to five, the program will run the code to
    #convert fahrenheit to celsius
    elif user_choice == '5':
        valid_answers = ['fahrenheit', 'Fahrenheit', 'FAHRENHEIT', 'Celsius'
                         ,'CELSIUS', 'celsius']
        print("What is the first measurement in? (celsius/fahrenheit)")
        given_number = valid_input_checker(valid_answers).lower()
        first_number = float(input("What is the given number?\n"))
        print("\ncalculating...")
        
        #math and output
        if given_number == 'fahrenheit':
            answer = (first_number - 32) * 5/9
            print(str(first_number) + " fahrenheit is equal to " 
                  + str(answer) + " celsius.")
        elif given_number == 'celsius':
            answer = (first_number * 9/5) + 32
            print(str(first_number) + " celsius is equal to " 
                  + str(answer) + " fahrenheit.")
            
    #asks the user if they want to run the program again. if not, the
    #code ends. if so, it runs through the main menu again.
    
    print("\nWould you like to run another calculation? (y/n)")
    user_continue = input().lower() == 'y'
    if not user_continue:
        print("Have a " + random.choice(goodbye_adjective) + " day!")
        break
    else:
        print("\nThank you for your continued patronage! Please enter"
              " another option.")
