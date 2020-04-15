# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:40:30 2019

@author: Clarissa
"""
#Hangman
import random 
def words(): 
    word_choice = ['dog','cat', 'pig','elephant', 'giraffe', 'ant','rhino', 'mouse']
    return random.choice (word_choice).lower()

def check (word,guesses,guess):
    display = ''
    turn = 0
    for letter in word:
        if letter in guesses :
            display += letter
        else:
            display += '_'
        
        if letter ==guess:
            turn += 1
    if turn>1 :
        print ('Yes the word contains', turn, '"' , guess, '"' +'s')
    elif turn == 1 :
        print ('Yes the word contains the letter', guess)

    else:
        print ('Sorry the word foes not contain the letter', guess)
    return display

def main() :
    word = words () 
    guesses =[]
    guessed = False 
    print ('The word contains', len (word), ' letters')
    while not guessed :
        text = "please enter a letter>> "
        guess = input(text)
        guess = guess.lower()
        if guess in guesses :
            print ("You already guessed" , guess)
       
            if guess == word :
                guessed = True 
            else:
                print ("Sorry that is wrong")
        elif len(guess) == 1 :
            guesses.append (guess)
            result = check (word,guesses,guess)
            if result == word:
                guessed = True
                
            else :
                print(result)
                
        else:
            print ('Invalid entry')
            
    print ("The word is", word , "You got it in", len(guesses), "tries")
    
main()