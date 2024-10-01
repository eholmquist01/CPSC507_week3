# Author: Emmalyn Holmquist
# Class: CPSC 507
# Homework 3
# Date: 9/13
# Problem 3

#create a function that checks a message length. if it is less than 140 characters return the message, if its more than
# say the message is too long!

def check_text_length(message):
    if len(message)>140: # Check if the length of the message exceeds 140 characters

        return "The text message is too long."
    else:
        return message

check_text_length("hello! my name is: ")