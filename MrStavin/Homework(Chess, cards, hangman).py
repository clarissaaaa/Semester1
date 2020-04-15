#Chess
def chess ():
    pos = str(input("Enter a position>> "))
    board_pos = [['H','G','F','E','D','C', 'B', 'A'],[1,2,3,4,5,6,7,8]]
    board =[
            [ '_', '_', '_', '_', '_', '_', '_', '_'],
            [ '_', '_', '_', '_', '_', '_', '_', '_'],
            [ '_', '_', '_', '_', '_', '_', '_', '_'],
            [ '_', '_', '_', '_', '_', '_', '_', '_'],
            [ '_', '_', '_', '_', '_', '_', '_', '_'],
            [ '_', '_', '_', '_', '_', '_', '_', '_'],
            [ '_', '_', '_', '_', '_', '_', '_', '_'],
            [ '_', '_', '_', '_', '_', '_', '_', '_']
            ]
    if len(pos)==2 :
        x = board_pos[0].index(str(pos[0].upper()))
        y = board_pos[1].index(int(pos[1].upper()))
    else :
       return "error"

    #Potential moves 
    potential_moves = []   
    potential_moves += [(x+2, y+1), (x+2, y-1)
                       ,(x+1, y+2), (x+1, y-2)
                       ,(x-2, y-1), (x-2, y+1)
                       ,(x-1, y+2), (x-1, y-2)]

    board[x][y]= "o"
    for i, j in potential_moves :
        if i >=0 and i <= 8 and j >= 0 and j <= 8:
            board[i][j] = '*'
            continue
        elif range in (len(board)):
            print(' '.join(board[i]))

    else:
        None 
        
chess()




#%%
#Shuffle Card 
import random 

def deck_of_cards (): 
    shape = ['heart', 'spade', 'diamond', 'club']
    num =['2','3','4','5','6','7','8','9','10','J','Q','K','A']
#
    for i in shape :
        for a in num:
            print(shape[randint(0,3)], num[randint(0,12)])
            
                     
deck_of_cards ()

#%%

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
                     















    