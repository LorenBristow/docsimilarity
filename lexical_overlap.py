# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 18:03:59 2019

@author: loren
"""

dict_a = {} 
dict_b = {} 
overlapScore = 0

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
    overlapScore = round(count_of_overlapping_words / ((len(dict_a) + len(dict_b)) - count_of_overlapping_words),3)
    print("compare: (george0{}.txt <> george0{}.txt) = ".format(a,b), overlapScore)
    return overlapScore
#scoreLexicalOverlap(1,2) # takes in the file number of each of the two dictionaries to be compared. 
#AUTOMATE WHAT YOU FEED IT. ie for loop through 1-4 files and logic for which to compare. send to DB?

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

def startTheEngine():
    listOfTextsByNumberPLUSONE = [1,2,3,4,5] # list must include 1 more than actual number of files. Needs to think more on this. 
    for number in listOfTextsByNumberPLUSONE:
        for unique_pairs in range(number + 1, len(listOfTextsByNumberPLUSONE)):
            overlapScore = scoreLexicalOverlap(number,unique_pairs) #running the function and assigning return directly to variable. 
startTheEngine()


#####WORK IN PROGRESS - USER INPUT TO DRIVE NUMBER OF FILES COMPARED###    
#def startTheEngine():
#    listOfTextsByNumberPLUSONE = []
#    number_of_texts = int(input("How many files are to be compared?\n"))
#    for num in range(1,number_of_texts + 1):
#        listOfTextsByNumberPLUSONE.append(num) # list must include 1 more than actual number of files. Needs to think more on this. 
#        #print(listOfTextsByNumberPLUSONE)
#        for number in listOfTextsByNumberPLUSONE:
#            for unique_pairs in range(number + 1, len(listOfTextsByNumberPLUSONE)):
#                overlapScore = scoreLexicalOverlap(number,unique_pairs) #running the function and assigning return directly to variable. 
#startTheEngine()