# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:42:42 2019

@author: loren
"""

def readStopWords():
    fname = open('stopwords.txt', 'r')
    #fname = '' ##switch out this line and line above to switch between top 20 before and after considering stopwords
    listOfStopWords = []
    for word in fname:
       listOfStopWords.append(word.strip())
    return listOfStopWords


#create and populated dictionary of words and frequencies

counted_words = {}   

def countWords(stopwords):     
    fname = open('mobydick.txt', 'r')    
    
    for line in fname:
        words = line.split()
        for word in words:
            if word not in stopwords:
                if word in counted_words:
                    counted_words[word] = counted_words[word] + 1
                else:
                    counted_words[word] = 1
    print("YYYYY",counted_words)

countWords(readStopWords())
##find most frequently occurring word
#
#most_frequent = -1
#for k,v in counted_words.items():
#    #print(k,v)
#    if v > most_frequent:
#        most_frequent = v
#
##print("\nThe most frequently occuring word is '{}' which occurs {} time(s) in this text.\n".format(i,most_frequent))
##need more investigation here - printing last word (i) form the loop and saying it is most freq, but actually need to return key assoc with most freq value. 
#
##print(sorted(counted_words.items(), reverse=True))
#print(counted_words.keys())

ranked_counted_words = (sorted(counted_words.items(), key=lambda kv:kv[1], reverse=True))
#print(ranked_counted_words)



#prints toop 20 most frequently occurring words
print("TOP20")  
for i in range(0,20):
    print(ranked_counted_words[0+i])
  
  


