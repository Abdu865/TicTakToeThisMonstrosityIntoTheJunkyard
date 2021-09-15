# Start with grid- Grid should be a dictionary.

def TicTakToe(Current_Grid ,Turn ,Move, Spaces):
    Grid = Current_Grid.replace(str(Move), Turn)
    ###
    Spaces[Move]= Turn  # If /1 or 0/ is needed
    ###
    print(Spaces[Move])

    if Turn == "X":
        Turn = "O"
    else:
        Turn = "X"
    return Grid,Turn, Spaces
####Used on Turn 5 and onwards
def WinCondition(Spaces):
   XRow1 = 0
   XRow2 = 0
   XRow3 = 0
   YRow1 = 0
   YRow2 = 0
   YRow3 = 0
   CrossL = 0
   CrossR = 0
   OXRow1 = 0
   OXRow2 = 0
   OXRow3 = 0
   OYRow1 = 0
   OYRow2 = 0
   OYRow3 = 0
   OCrossL = 0
   OCrossR = 0

   for Key, Value in Spaces.items():## Itterates through each indidually
        try:
            int(Value)
        except (ValueError):
            if Value == "X":
                if Key in (1,2,3):
                    XRow1 += 1
                if Key in (4,5,6):
                    XRow2 += 1
                if Key in (7,8,9):
                    XRow3 += 1
                if Key in (1, 4, 7):
                    YRow1 += 1
                if Key in (2, 5, 8):
                    YRow2 += 1
                if Key in (3, 6, 9):
                    YRow3 += 1
                if Key in (1,5,9):
                    CrossL += 1
                if Key in (3,5,7):
                    CrossR += 1
                if 3 in (XRow1, XRow2, XRow3, YRow1, YRow2, YRow3, CrossL, CrossR):
                    print("X wins!")
                    quit()
            else:
                if Key in (1,2,3):
                    OXRow1 += 1
                if Key in (4,5,6):
                    OXRow2 += 1
                if Key in (7,8,9):
                    OXRow3 += 1
                if Key in (1, 4, 7):
                    OYRow1 += 1
                if Key in (2, 5, 8):
                    OYRow2 += 1
                if Key in (3, 6, 9):
                    OYRow3 += 1
                if Key in (1,5,9):
                    OCrossL += 1
                if Key in (3,5,7):
                    OCrossR += 1
                if 3 in (OXRow1, OXRow2, OXRow3, OYRow1, OYRow2, OYRow3, OCrossL, OCrossR):
                    print("O wins!")
                    quit()

#####################################################
Spaces = {1:"1", 2:"2", 3:"3",
           4:"4", 5:"5", 6:"6",
           7:"7", 8:"8", 9:"9"}  # Used to record moves

Grid="1|2|3\n4|5|6\n7|8|9" #Whats printed to the player

Turn = "X" ## X goes first


while True:
    print(Grid)
    while True: ### Gets the player to enter a valid move
        try:
            Move = int(input(("You are playing as", Turn, "Select the space you want to fill:")))
        except (ValueError):
            print("Please Enter a Valid Number")
        if (Move >= 10) or (Move <= 0):
            print("Please Enter a Valid Number")
        elif (str(Spaces[Move]) != str(Move)):
            print("That move has been played, try again.")
        else:
            break

    Grid, Turn, Spaces = TicTakToe(Grid,Turn,Move,Spaces)
    GG= 0#move counter - Game ends at 9#this resets
    for Key, Value in Spaces.items():
        if str(Key) != str(Value):
            GG += 1
    if (GG >= 5) and (GG < 9):
        print(Grid)
        WinCondition(Spaces)
    if (GG == 9):
        print(Grid)
        WinCondition(Spaces)
        print("GG its a tie")
        break
