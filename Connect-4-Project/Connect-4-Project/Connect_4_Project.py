
def printGrid(grid):
    print("\n------------------------------------")
    print("     5-["+grid[0][5]+"]"+"["+grid[1][5]+"]"+"["+grid[2][5]+"]"+"["+grid[3][5]+"]"+"["+grid[4][5]+"]"+"["+grid[5][5]+"]"+"["+grid[6][5]+"]")
    print("     4-["+grid[0][4]+"]"+"["+grid[1][4]+"]"+"["+grid[2][4]+"]"+"["+grid[3][4]+"]"+"["+grid[4][4]+"]"+"["+grid[5][4]+"]"+"["+grid[6][4]+"]")
    print("     3-["+grid[0][3]+"]"+"["+grid[1][3]+"]"+"["+grid[2][3]+"]"+"["+grid[3][3]+"]"+"["+grid[4][3]+"]"+"["+grid[5][3]+"]"+"["+grid[6][3]+"]")
    print("     2-["+grid[0][2]+"]"+"["+grid[1][2]+"]"+"["+grid[2][2]+"]"+"["+grid[3][2]+"]"+"["+grid[4][2]+"]"+"["+grid[5][2]+"]"+"["+grid[6][2]+"]")
    print("     1-["+grid[0][1]+"]"+"["+grid[1][1]+"]"+"["+grid[2][1]+"]"+"["+grid[3][1]+"]"+"["+grid[4][1]+"]"+"["+grid[5][1]+"]"+"["+grid[6][1]+"]")
    print("     0-["+grid[0][0]+"]"+"["+grid[1][0]+"]"+"["+grid[2][0]+"]"+"["+grid[3][0]+"]"+"["+grid[4][0]+"]"+"["+grid[5][0]+"]"+"["+grid[6][0]+"]")
    print("        A "+" B "+" C "+" D "+" E "+" F "+" G ")
    print("------------------------------------\n")

def updateBoard(gGrid,input,tPlayer):
    #replace empty space with player symbol
    slot = 0
    if input == "A" or input == "a" :
        for space in gGrid[0]:
            if space == " ":
                gGrid[0][slot] = tPlayer
                break
            slot+=1
    elif input == "B" or input == "b" :
        for space in gGrid[1]:
            if space == " ":
                gGrid[1][slot] = tPlayer
                break
            slot+=1
    elif input == "C" or input == "c" :
        for space in gGrid[2]:
            if space == " ":
                gGrid[2][slot] = tPlayer
                break
            slot+=1
    elif input == "D" or input == "d" :
        for space in gGrid[3]:
            if space == " ":
                gGrid[3][slot] = tPlayer
                break
            slot+=1
    elif input == "E" or input == "e" :
        for space in gGrid[4]:
            if space == " ":
                gGrid[4][slot] = tPlayer
                break
            slot+=1
    elif input == "F" or input == "f" :
        for space in gGrid[5]:
            if space == " ":
                gGrid[5][slot] = tPlayer
                break
            slot+=1
    elif input == "G" or input == "g" :
        for space in gGrid[6]:
            if space == " ":
                gGrid[6][slot] = tPlayer
                break
            slot+=1

def checkFullList(gGrid,tPlayer):
    vBorder = len(gGrid[0])
    print("\nIt is player "+tPlayer+" turn")
    gChoices = ["a","b","c","d","e","f","g","A","B","C","D","E","F","G"]
    pInput = str(input("Please input a letter player "+tPlayer+": "))
    while pInput not in gChoices:
        pInput = str(input("Error:Player "+ tPlayer+" enter a letter between A-G: "))

    while pInput == "a" and gGrid[0][vBorder-1 ]!= " ":
        pInput = str(input("\nError:"+ pInput.capitalize()+" list full.\nEnter new letter player "+tPlayer+": "))
    while pInput == "b" and gGrid[1][vBorder-1 ]!= " ":
        pInput = str(input("\nError:"+ pInput.capitalize()+" list full.\nEnter new letter player "+tPlayer+": "))
    while pInput == "c" and gGrid[2][vBorder-1 ]!= " ":
        pInput = str(input("\nError:"+ pInput.capitalize()+" list full.\nEnter new letter player "+tPlayer+": "))
    while pInput == "d" and gGrid[3][vBorder-1 ]!= " ":
        pInput = str(input("\nError:"+ pInput.capitalize()+" list full.\nEnter new letter player "+tPlayer+": "))
    while pInput == "e" and gGrid[4][vBorder-1 ]!= " ":
        pInput = str(input("\nError:"+ pInput.capitalize()+" list full.\nEnter new letter player "+tPlayer+": "))
    while pInput == "f" and gGrid[5][vBorder-1 ]!= " ":
        pInput = str(input("\nError:"+ pInput.capitalize()+" list full.\nEnter new letter player "+tPlayer+": "))
    while pInput == "g" and gGrid[6][vBorder-1 ]!= " ":
        pInput = str(input("\nError:"+ pInput.capitalize()+" list full.\nEnter new letter player "+tPlayer+": "))
    return pInput

def horiWin(gGrid):
    #check horiztonal win cases(all connect 4 from A-D to D-G grid)
    hBorder = len(gGrid)#7
    vBorder = len(gGrid[0])#6
    for row in range(0,hBorder-3):
        for col in range(0,vBorder):
            if gGrid[row][col] == gGrid[row+1][col]== gGrid[row+2][col]== gGrid[row+3][col] and gGrid[row][col] != " ":
                return True
    return False

def vertWin(gGrid):
    #check vertical win cases(all connect 4 from 0-2 to 3-5)
    hBorder = len(gGrid)#7
    vBorder = len(gGrid[0])#6
    for row in range(0,hBorder):
        for col in range(0, vBorder-3):
            if gGrid[row][col] == gGrid[row][col+1]== gGrid[row][col+2] == gGrid[row][col+3] and gGrid[row][col] != " ":
                return True
    return False

def diaWin(gGrid):
    #check diagonal win cases
    #lowest(2nd lowest/3rd lowest) row A-D diagonal up going right up
    for col in range(0,3):
        if gGrid[0][col] == gGrid[1][col+1]== gGrid[2][col+2]== gGrid[3][col+3] and gGrid[0][col] != " ":
            return True
    #lowest(2nd lowest/3rd lowest) row G-D diagonal up going left up
    for col in range(6,2,-1):
        if gGrid[col][0] == gGrid[col-1][1]== gGrid[col-2][2]== gGrid[col-3][3] and gGrid[col][0] != " ":
            return True
        elif gGrid[col][1] == gGrid[col-1][2]== gGrid[col-2][3]== gGrid[col-3][4] and gGrid[col][1] != " ":
            return True
        elif gGrid[col][2] == gGrid[col-1][3]== gGrid[col-2][4]== gGrid[col-3][5] and gGrid[col][2] != " ":
            return True
    #bottom(2nd lowest) row D-G diagonal up going right
    for col in range(1,4):
        if gGrid[col][0] == gGrid[col+1][1]== gGrid[col+2][2]== gGrid[col+3][3] and gGrid[col][0] != " ":
            return True
        elif gGrid[col][1] == gGrid[col+1][2]== gGrid[col+2][3]== gGrid[col+3][4] and gGrid[col][1] != " ":
            return True
    return False

def checkWinCases(gGrid,player):
    #check for horizontal, vertical, and diagonal win case
    if horiWin(gGrid) == True:
        print("Player "+player +" has won! Won by horizontal")
        return True
    elif vertWin(gGrid) == True:
        print("Player "+player +" has won! Won by vertical" )
        return True
    elif diaWin(gGrid) == True:
        print("Player "+player +" has won! Won by diagonal")
        return True
    else:
        return False

def StartGame():
    #inital game setup
    gGrid = ( [" "," "," "," "," "," "],[" "," "," "," "," "," "],
              [" "," "," "," "," "," "],[" "," "," "," "," "," "], 
              [" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "] )
    #horiLen(7)print(len(gGrid))
    #vertLen(6)print(len(gGrid))
    winGame = False
    turnNum = 1
    #main game loop that takes user input each turn
    while winGame == False:
        printGrid(gGrid)
        if turnNum % 2 == 1:
            playerInput = checkFullList(gGrid,"X")
            updateBoard(gGrid,playerInput,"X")
            gameWon = checkWinCases(gGrid,"X")
        else:
            playerInput = checkFullList(gGrid,"O")
            updateBoard(gGrid,playerInput,"O")
            gameWon = checkWinCases(gGrid,"O")
        turnNum+=1
        if turnNum > 42:
            print("Neither player has won the game this game is a tie!")
            break
        if gameWon == True:
            break

    #restart game if answer is yes
    playAgain = str(input("Would you like to play again?"))
    if playAgain == "yes" or playAgain == "Yes":
        StartGame()
    
def main():
    StartGame()
   
            
main()


def Done(): 
    print()
    #elif gGrid[0][1] == gGrid[1][2] == gGrid[2][3] == gGrid[3][4] and gGrid[0][1] != " ":
    #elif gGrid[1][2] == gGrid[2][3] == gGrid[3][4] == gGrid[4][5] and gGrid[1][2] != " ":
    #elif gGrid[0][2] == gGrid[1][3] == gGrid[2][4] == gGrid[3][5] and gGrid[0][2] != " ":
    #elif gGrid[3][1] == gGrid[2][2] == gGrid[1][3] == gGrid[0][4] and gGrid[3][1] != " ":
    #elif gGrid[4][1] == gGrid[3][2] == gGrid[2][3] == gGrid[1][4] and gGrid[4][1] != " ":
    #elif gGrid[5][1] == gGrid[4][2] == gGrid[3][3] == gGrid[2][4] and gGrid[5][1] != " ":
    #elif gGrid[6][1] == gGrid[5][2] == gGrid[4][3] == gGrid[3][4] and gGrid[6][1] != " ":
    #elif gGrid[2][1] == gGrid[3][2] == gGrid[4][3] == gGrid[5][4] and gGrid[2][1] != " ":
    #elif gGrid[3][1] == gGrid[4][2] == gGrid[5][3] == gGrid[6][4] and gGrid[3][1] != " ":
    #elif gGrid[0][0] == gGrid[1][1] == gGrid[2][2] == gGrid[3][3] and gGrid[0][0] != " ":
    #elif gGrid[1][1] == gGrid[2][2] == gGrid[3][3] == gGrid[4][4] and gGrid[1][1] != " ":
    #elif gGrid[2][2] == gGrid[3][3] == gGrid[4][4] == gGrid[5][5] and gGrid[2][2] != " ":
    #elif gGrid[3][2] == gGrid[4][3] == gGrid[5][4] == gGrid[6][5] and gGrid[3][2] != " ":
    #elif gGrid[3][0] == gGrid[2][1] == gGrid[1][2] == gGrid[0][3] and gGrid[3][0] != " ":
    #elif gGrid[4][0] == gGrid[3][1] == gGrid[2][2] == gGrid[1][3] and gGrid[4][0] != " ":
    #elif gGrid[5][0] == gGrid[4][1] == gGrid[3][2] == gGrid[2][3] and gGrid[5][0] != " ":
    #elif gGrid[6][0] == gGrid[5][1] == gGrid[4][2] == gGrid[3][3] and gGrid[6][0] != " ":                                             
    #elif gGrid[3][2] == gGrid[2][3] == gGrid[1][4] == gGrid[0][5] and gGrid[3][2] != " ":
    #elif gGrid[4][2] == gGrid[3][3] == gGrid[2][4] == gGrid[1][5] and gGrid[4][2] != " ":
    #elif gGrid[5][2] == gGrid[4][3] == gGrid[3][4] == gGrid[2][5] and gGrid[5][2] != " ":
    #elif gGrid[6][2] == gGrid[5][3] == gGrid[4][4] == gGrid[3][5] and gGrid[6][2] != " ":