# Author: Emmalyn Holmquist
# Class: CPSC 507
# Homework 3
# Date: 9/13
# Problem 5

# Write a function that takes a word and counts and returns the number of letter "o" in that word.
# For example, if you pass "bonobos" to your function, it should return 3

def o_counts(word):
    o_sum=0 #initialize sum of o's

    for i in word: #marching through letters of word
        if i == "o": #logic test to evaluate if the letters is an o
            o_sum+= 1 #if an o, then add to sum

    #print(o_sum) #test

    return(o_sum)

#o_counts("bonobos") # test

