#a= "michael"
#b= "icmahel"

#output : true 
#%%
def check(s1,s2):
    if (sorted(s1)== sorted(s2)):
        print("The strings are anagrams")
    else :
        print ("The strings are not anagrams ")

s1 = "listen"
s2 = "silent"

check(s1,s2)

#%%
#Checking anagram without sorted or dict 
def isAnagram (firstWord, secondWord):
    they_are_anagrams = True;
    
    for c in firstWord:
        index = secondWord.find(c)
        print (secondWord)
        
        if (index >= 0):
            secondWord = secondWord.replace (c, "")
        
    else:
        they_are_anagrams = False
        
    return they_are_anagrams

print(isAnagram("michael","lmichae"))