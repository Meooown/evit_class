"""
Password cracker
Created by Meooown on github
Created on 9/2/2022
Last updated 9/2/2022
"""
import random
password = "Wed"




listA = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
for i  in listA:
    if i == password:
        print("Your password is " + str(i))
        break
