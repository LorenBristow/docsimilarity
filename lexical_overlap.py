# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 18:03:59 2019

@author: loren
"""

dict_a = {} 
dict_b = {} 
overlapScore = 0

def extractTexta(a):  
    fname = open("george0{}.txt".format(a))
    for line in fname:
        words = line.split()
        for word in words:
            if word in dict_a:
               dict_a[word] += 1
            else:
                dict_a[word] = 1
#    print("TEXT {}".format(a), dict_a)
#    print(len(dict_a))
    return dict_a

def extractTextb(b):     
    fname = open("george0{}.txt".format(b))
    for line in fname:
        words = line.split()
        for word in words:
            if word in dict_b:
               dict_b[word] += 1
            else:
                dict_b[word] = 1
#    print("TEXT {}".format(b), dict_b)
#    print(len(dict_b))
    return dict_b

def scoreLexicalOverlap(a,b):
    extractTexta(a)
    extractTextb(b)
    count_of_overlapping_words = 0
    count_of_non_overlapping_words_ie_in_a_but_not_b = 0 
    for word in dict_a:
        if word in dict_b:
            count_of_overlapping_words += 1 # is overlap value magnified when x occurs many times in a, and only once in b?
       #is the number different when reversing which text is a or b?
        else:
            count_of_non_overlapping_words_ie_in_a_but_not_b += 1
#    print(count_of_overlapping_words)
#    print(count_of_non_overlapping_words_ie_in_a_but_not_b)
    recon = len(dict_a) - (count_of_overlapping_words + count_of_non_overlapping_words_ie_in_a_but_not_b)
    #print("recon ", recon) #check - should be zero. #maybe add a test to check this and return verdict?
    overlapScore = count_of_overlapping_words / ((len(dict_a) + len(dict_b)) - count_of_overlapping_words)
    print("compare: (george0{}.txt <> george0{}.txt) = ".format(a,b), overlapScore)
    return overlapScore
#scoreLexicalOverlap(1,2) # takes in the file number of each of the two dictionaries to be compared. 
#AUTOMATE WHAT YOU FEED IT. ie for loop through 1-4 files and logic for which to compare. send to DB?


for number in range(0,3):
    overlapScore = scoreLexicalOverlap(number + 1,number + 2) #running the function and assigning return directly to variable. 
    

###############################################
#scoreLexicalOverlap(a,b) # takes in the file number of each of the two dictionaries to be compared. 


#def create_dictionaries(1,2):
#    for number in range(1,5):
##        name_dict = "d{}".format(number)
#        d = {}
#        fname = open("george0{}.txt".format(number))
#        for line in fname:
#            words = line.split()
#            for word in words:
#                if word in d:
#                   d[word] += 1
#                else:
#                    d[word] = 1
#    print("TEXT {}".format(number), d)
#    return {}

#counted_words = {}   
#
#def countWords(stopwords):     
#    fname = open('mobydick.txt', 'r')    
#    
#    for line in fname:
#        words = line.split()
#        for word in words:
#            if word not in stopwords:
#                if word in counted_words:
#                    counted_words[word] = counted_words[word] + 1
#                else:
#                    counted_words[word] = 1
#    print("YYYYY",counted_words)
#
#countWords(readStopWords())