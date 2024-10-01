# Author: Emmalyn Holmquist
# Class: CPSC 507
# Homework 3
# Date: 9/13
# Problem 6

# use while-loop and write a function that prints a word triangle by progressively printing less and
# less of the string, like this:

#abracadabra
#abracadabr
#abracadab
#abracada
#abracad
#abraca
#abrac
#abra
#abr
#ab
#a
#

def word_triangle(word):
    length=len(word) #create an inital length of the word to decrease through loop

    while 0 < length:
        print(word[:length]) # prints the word from the beginning to as long as the length
        length -= 1 # decreases length by 1

#word_triangle("HELLOWORLD") test
