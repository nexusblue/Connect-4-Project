
#figure out updaing game board with nested lists

def printGrid(grid):
    print("\nRuning updateBoard func")
    print("  ["+grid[0][5]+"]"+"["+grid[1][5]+"]"+"["+grid[2][5]+"]"+"["+grid[3][5]+"]"+"["+grid[4][5]+"]"+"["+grid[5][5]+"]"+"["+grid[6][5]+"]")
    print("  ["+grid[0][4]+"]"+"["+grid[1][4]+"]"+"["+grid[2][4]+"]"+"["+grid[3][4]+"]"+"["+grid[4][4]+"]"+"["+grid[5][4]+"]"+"["+grid[6][4]+"]")
    print("  ["+grid[0][3]+"]"+"["+grid[1][3]+"]"+"["+grid[2][3]+"]"+"["+grid[3][3]+"]"+"["+grid[4][3]+"]"+"["+grid[5][3]+"]"+"["+grid[6][3]+"]")
    print("  ["+grid[0][2]+"]"+"["+grid[1][2]+"]"+"["+grid[2][2]+"]"+"["+grid[3][2]+"]"+"["+grid[4][2]+"]"+"["+grid[5][2]+"]"+"["+grid[6][2]+"]")
    print("  ["+grid[0][1]+"]"+"["+grid[1][1]+"]"+"["+grid[2][1]+"]"+"["+grid[3][1]+"]"+"["+grid[4][1]+"]"+"["+grid[5][1]+"]"+"["+grid[6][1]+"]")
    print("  ["+grid[0][0]+"]"+"["+grid[1][0]+"]"+"["+grid[2][0]+"]"+"["+grid[3][0]+"]"+"["+grid[4][0]+"]"+"["+grid[5][0]+"]"+"["+grid[6][0]+"]")
    print("   A "+" B "+" C "+" D "+" E "+" F "+" G ")

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
    printGrid(gGrid)

def checkFullList(gGrid,tPlayer):
    print("\nIt is player "+tPlayer+" turn")
    gChoices = ["a","b","c","d","e","f","g","A","B","C","D","E","F","G"]
    playerInput = str(input("Please input a letter player "+tPlayer+": "))
    while playerInput not in gChoices:
        playerInput = str(input("Player "+ tPlayer+" lease enter a letter between A-G: "))


    while playerInput == "a" and gGrid[0][len(gGrid[0])-1 ]!= " ":
        print("a list is full")
        playerInput = str(input("Please input a letter player "+tPlayer+": "))

    while playerInput == "b" and gGrid[1][len(gGrid[0])-1 ]!= " ":
        print("b list is full")
        playerInput = str(input("Please input a letter player "+tPlayer+": "))

    while playerInput == "c" and gGrid[2][len(gGrid[0])-1 ]!= " ":
        print("c list is full")
        playerInput = str(input("Please input a letter player "+tPlayer+": "))

    while playerInput == "d" and gGrid[3][len(gGrid[0])-1 ]!= " ":
        print("d list is full")
        playerInput = str(input("Please input a letter player "+tPlayer+": "))

    return playerInput

def checkForWin():
    print()

def StartGame():
    
    gGrid = ( [" "," "," "," "," "," "],
              [" "," "," "," "," "," "],
              [" "," "," "," "," "," "],
              [" "," "," "," "," "," "], 
              [" "," "," "," "," "," "],
              [" "," "," "," "," "," "],
              [" "," "," "," "," "," "] )

    printGrid(gGrid)
    winGame = False
    turnNum = 0
    #main game loop that takes user input each turn
    while winGame == False:
        if turnNum % 2 == 0:
            playerInput = checkFullList(gGrid,"X")
            updateBoard(gGrid,playerInput,"X")
        else:
            playerInput = checkFullList(gGrid,"O")
            updateBoard(gGrid,playerInput,"O")
        turnNum+=1
        checkForWin()

    
    #restart game if answer is yes
    playAgain = str(input("Would you like to play again?"))
    if playAgain == "yes" or playAgain == "Yes":
        StartGame()
    

def main():
    StartGame()
   
            
main()
