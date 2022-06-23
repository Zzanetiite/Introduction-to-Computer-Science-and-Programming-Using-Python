# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:17:34 2022

@author: zanete
"""

"""
Task
The program works as follows: you (the user) 
thinks of an integer between 0 (inclusive) 
and 100 (not inclusive). The computer makes guesses, 
and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's
secret number!
"""

    
#function to check if input is valid

def AllowedAnswers (a) :
    #is it one of the allowed answers?
    if str(a) in 'lhc' : return True
    #if neither of the above it is something else - return false
    else : return False

def AskingTheQuestion():
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") 

    while AllowedAnswers (a) == False :
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(x) + "?")
        a = AskingTheQuestion()
    return a


#Start of the program

#counting the tries:
count = 0
#starting from the middle
xh = 100
xl = 0
x = 50

print("Please think of a number between 0 and 100!" )
print("Is your secret number " + str(x) + "?")
count += 1

a = AskingTheQuestion()

while a != "c" :
    if a == 'h' :
        xh = x
        x = int(x-((x-xl)/2)) 
        print("Is your secret number " + str(x) + "?")
        count += 1
        a = AskingTheQuestion()
    if a == 'l' :
        #integers are rounded down so this is edge case
        if x == 98 :
            x = 99
        xl = x
        x = int(x+((xh-x)/2)) 
        print("Is your secret number " + str(x) + "?")
        count += 1
        a = AskingTheQuestion()

#print("")
#print("This is the end of the game!")
print("Game over. Your secret number was:", x)
#print("")
#print("It took me", count, "tries to guess.")