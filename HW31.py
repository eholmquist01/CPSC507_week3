# Author: Emmalyn Holmquist
# Class: CPSC 507
# Homework 3
# Date: 9/13
# Problem 1

# Write a function that reads the elements inside the list below and:
# if it is banana, prints "Banana, it is!"
# if it is apple, prints "You are the apple of my pie!"
# if it is cherry, prints "I cherry-ish you!"
# if it is something else, prints "Objection!"
# [cherry, pomegranate, apple, cherry, banana, apple, orange, banana, cherry]

for i in ["cherry", "pomegranate", "apple", "cherry", "banana", "apple", "orange", "banana", "cherry"]: #for loop to march through elements
    if i == "banana": #using if statement to evaluate cases
        print("Banana it is!")
    elif i == "apple":
        print("You are the apple of my pie!")
    elif i == "cherry":
        print("I cherry-ish you!")
    else:
        print("Objection!")