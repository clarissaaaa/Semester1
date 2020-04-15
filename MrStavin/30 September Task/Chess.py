#chess problem
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
        for i in range (len(board)):
            print(' '.join(board[i]))

    else:
        None 
        
chess()
