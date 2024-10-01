# Author: Emmalyn Holmquist
# Class: CPSC 507
# Homework 3
# Date: 9/13
# Problem 4

# Write a function that takes a tweet and returns the number of hashtags that are available in that tweet.
# Hint: you may look for # signs.

def num_hashtags(tweet):
    hash_sum=0  # initiate variable for counting num hashtags
    i = 0 # initialize variable for incrementing
    while i < len(tweet): #this will run until we reach the end of the tweet
        if tweet[i] == "#": #logic statement, will only count index if there is a hashtag
            hash_sum = hash_sum+1
        i += 1 #increments to move to next letter

    #print(hash_sum) #check

num_hashtags("h # and # and # and #")