# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:42:42 2019

@author: loren
"""

fname = open('mobydick.txt', 'r')

counted_words = {}

for line in fname:
    words = line.split()
    #print(words)
    for i in words:
        #print(i)
        if i in counted_words:
            counted_words[i] = counted_words[i] + 1
        else:
            counted_words[i] = 1
    print(counted_words)
