"""
Birthday Calculator
Created by @Meooown on Github
Created in 8/31/2022
Last updated 9/6/2022
"""

#Variables
today = ''
day_of_the_year = 0
day_of_the_bday = 0
day_difference = 0
day_in_future = 0

#Introduction
print("Find out what day of the week your birthday falls on by "
      + "answering these 3 questions ")

#User questions
today = input("\nQuestion 1: What day of the week is it today?: "
              ).lower()
day_of_the_year = int(input("Question 2: What day of the year is it"
                            + " today?: "))
day_of_the_bday = int(input("Question 3: What day of the year does your"
                            + " birthday fall on?: "))
      
#Turning the current day of the week into a digit
if today == "sunday":
    today = 1
elif today == "monday":
    today = 2
elif today == "tuesday":
    today = 3
elif today == "wednesday":
    today = 4
elif today == "thursday":
    today = 5
elif today == "friday":
    today = 6
elif today == "saturday":
    today = 7

#Calculations needed to find out the day of the week the birthday is on
day_difference = day_of_the_bday - day_of_the_year
day_in_future = (day_difference + today)% 7

#Prints out what day of the week the birthday will be on
if day_in_future == 1:
    print("Your bithday is on a sunday this year.")
elif day_in_future == 2:
    print("Your bithday is on a monday this year.")
elif day_in_future == 3:
    print("Your bithday is on a tuesday this year.")
elif day_in_future == 4:
    print("Your bithday is on a wednesday this year.")
elif day_in_future == 5:
    print("Your bithday is on a thursday this year.")
elif day_in_future == 6:
    print("Your bithday is on a friday this year.")
elif day_in_future == 7:
    print("Your bithday is on a saturday this year.")
