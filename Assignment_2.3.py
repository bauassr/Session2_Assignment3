# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:51:35 2018

@author: singh.shivam
"""
def reverse(s):
    str=""
    for i in s:
        str = i + str
    return str
    
print("Please enter a word:")
Word = input()
Reverse_string =reverse(Word) 
print(Reverse_string)

#Revese String using built in list function#
Word_list = list(Word)
print("Reverse Word using buit-in function: ")
Word_list.reverse()
print("".join(S for S in Word_list))

