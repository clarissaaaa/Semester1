# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:03:08 2019

@author: Clarissa
"""
import matplotlib.pyplot as plt
import collections

filename = input("Enter a filename : ")
with open (filename) as f :
    string = f.read()

string_lower = string.lower()
string_list = string_lower.split()
string_dict = {}

#print (string_list)
for word in string_list :
    if word in string_dict:
        string_dict[word] = string_dict[word] + 1
    else: 
        string_dict[word] = 1

#Sort the dict by its value so that the bar graph will display from highest to lowest
sorted_string_dict = sorted(string_dict.items(), key=lambda kv:kv[1])
sorted_dict = collections.OrderedDict(sorted_string_dict)

#print (string_dict)
word_list = sorted_dict.keys()
count_list = sorted_dict.values()
indentation = list(range(1,len(count_list)+1))

fig = plt.figure (dpi= 168, figsize= (10,6))
plt.barh(indentation, count_list, color= 'red',edgecolor ='black')
plt.title ("Numbers of words repeated in a File",fontsize = 16)
plt.xlabel("Numbers of repetion", fontsize= 12)
plt.ylabel("Words", fontsize= 12)
plt.yticks(indentation,word_list, fontsize = 8)
plt.show()