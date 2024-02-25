import time
def tictactoe(chosenfield, rowlist):
    global playerturn, totalturns
    n1, n2 = 0, 0
    if 1 <= chosenfield <= 3:
        n1, n2 = 0, chosenfield - 1
    elif 4 <= chosenfield <= 6:
        n1, n2 = 1, chosenfield - 4
    elif 7 <= chosenfield <= 9:
        n1, n2 = 2, chosenfield - 7
    elif chosenfield > 9:
        print("Hey, that's an invalid field number!")
        return tictactoe

    if rowlist[n1][n2] == "_":
        rowlist[n1][n2] = playerturn

        if playerturn == "X":
            playerturn = "O"
        elif playerturn == "O":
            playerturn = "X"
        totalturns += 1
    else:
        print("That field is occupied!")


def winCheck():

    for i in range(3):

        if (rowlist[i][0] == "X" and rowlist[i][1] == "X" and rowlist[i][2] == "X") \
                or (rowlist[0][i] == "X" and rowlist[1][i] == "X" and rowlist[2][i] == "X"):
            print("X won! Congratulations!")
            winOutput(rowlist)

        elif (rowlist[i][0] == "O" and rowlist[i][1] == "O" and rowlist[i][2] == "O") \
                or (rowlist[0][i] == "O" and rowlist[1][i] == "O" and rowlist[2][i] == "O"):
            print("O won! Congratulations!")
            winOutput(rowlist)


    if (rowlist[0][0] == "X" and rowlist[1][1] == "X" and rowlist[2][2] == "X") \
       or (rowlist[0][2] == "X" and rowlist[1][1] == "X" and rowlist[2][0] == "X"):
        print("X won! Congratulations!")
        winOutput(rowlist)
    if (rowlist[0][0] == "O" and rowlist[1][1] == "O" and rowlist[2][2] == "O") \
       or (rowlist[0][2] == "O" and rowlist[1][1] == "O" and rowlist[2][0] == "O"):
        print("O won! Congratulations!")
        winOutput(rowlist)


def winOutput(rowlist):
    for i in rowlist:
        print(i)
    newgame = input("Do you want to play another game?\n").lower()
    if newgame == "yes":
        print("Let's start again!")
        newGame()
    else:
        print("Thank you for playing!")
        time.sleep(5)
        exit()


def newGame():
    global rowlist, playerturn, totalturns
    rowlist = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    playerturn = "X"
    totalturns = 0


rowlist = [["1 ", "2 ", "3"], ["4 ", "5 ", "6"], ["7 ", "8 ", "9"]]

print("Hello! Welcome to the Tic Tac Toe game without a GUI.")
print("If you want to place your symbol, type in the number of the field you want to choose.")

for i in rowlist:
    print(i)
print("Have fun playing against a friend!")

rowlist = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
playerturn = "X"
totalturns = 0

while True:
    print(f"Place your symbol! {playerturn}")
    for i in rowlist:
        print(i)
    try:
        chosenfield = int(input())
        tictactoe(chosenfield, rowlist)


    except:
        print("Hey, that's an invalid field number!")
    winCheck()
    # Tie-Check
    if totalturns == 9:
        print("It's a tie! Play again to find out who the winner is.")
        winOutput(rowlist)