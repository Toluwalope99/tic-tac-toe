PlayerOneWin = ""
PlayerTwoWin = ""
wonStatus = False
drawStatus = False
checker2 = True

playLst = ["#", "", "", "", "", "", "", "", "", ""]


def display(player_one_status, player_two_status):
    print(player_one_status)
    print("|" + "\t" + "\t" "|" + "\t" + "\t" + "|" + "\t" + "\t" + "|")
    print("|" + "\t" + playLst[1] + "\t" "|" + "\t" + playLst[2] + "\t" + "|" + "\t" + playLst[3] + "\t" + "|")
    print("|" + "\t" + "\t" "|" + "\t" + "\t" + "|" + "\t" + "\t" + "|")
    print("=========================")
    print("|" + "\t" + "\t" "|" + "\t" + "\t" + "|" + "\t" + "\t" + "|")
    print("|" + "\t" + playLst[4] + "\t" "|" + "\t" + playLst[5] + "\t" + "|" + "\t" + playLst[6] + "\t" + "|")
    print("|" + "\t" + "\t" "|" + "\t" + "\t" + "|" + "\t" + "\t" + "|")
    print("=========================")
    print("|" + "\t" + "\t" "|" + "\t" + "\t" + "|" + "\t" + "\t" + "|")
    print("|" + "\t" + playLst[7] + "\t" "|" + "\t" + playLst[8] + "\t" + "|" + "\t" + playLst[9] + "\t" + "|")
    print("|" + "\t" + "\t" "|" + "\t" + "\t" + "|" + "\t" + "\t" + "|")
    print(player_two_status)


def identify():
    firstPicker = input("First user to select X or O: ").upper()

    while firstPicker != "X" and firstPicker != "O":
        firstPicker = input("WRONG! First user to please select X or O: ").upper()

    if firstPicker == "X":
        player_1 = "X"
        player_2 = "O"
        print("Player 1 is X, Player 2 is O")
    else:
        player_1 = "O"
        player_2 = "X"
        print("Player 1 is O, Player 2 is X")

    Choice = input("Do you want to enter player name: Y or N: ").upper()

    while Choice != "Y" and Choice != "N":
        Choice = input("WRONG! Please select Y or N: ").upper()

    if Choice == "Y":
        player_1_name = input("Player 1 enter your name here: ").capitalize()
        player_2_name = input("Player 2 enter your name here: ").capitalize()
    else:
        player_1_name = "Player 1"
        player_2_name = "Player 2"
    return player_1, player_2, player_1_name, player_2_name


def checkWin():
    global wonStatus
    if playLst[1] == playLst[2] == playLst[3] and playLst[1] != "" and playLst[2] != "" and playLst[3] != "":
        wonStatus = True
    elif playLst[4] == playLst[5] == playLst[6] and playLst[4] != "" and playLst[5] != "" and playLst[6] != "":
        wonStatus = True
    elif playLst[7] == playLst[8] == playLst[9] and playLst[7] != "" and playLst[8] != "" and playLst[9] != "":
        wonStatus = True
    elif playLst[1] == playLst[4] == playLst[7] and playLst[1] != "" and playLst[4] != "" and playLst[7] != "":
        wonStatus = True
    elif playLst[2] == playLst[5] == playLst[8] and playLst[2] != "" and playLst[5] != "" and playLst[8] != "":
        wonStatus = True
    elif playLst[3] == playLst[6] == playLst[9] and playLst[3] != "" and playLst[6] != "" and playLst[9] != "":
        wonStatus = True
    elif playLst[1] == playLst[5] == playLst[9] and playLst[1] != "" and playLst[5] != "" and playLst[9] != "":
        wonStatus = True
    elif playLst[3] == playLst[5] == playLst[7] and playLst[3] != "" and playLst[5] != "" and playLst[7] != "":
        wonStatus = True
    else:
        wonStatus = False


def checkDraw():
    global drawStatus
    draw_lst = []
    for i in range(1, 10):
        if playLst[i] != "":
            draw_lst.append(i)
    checker = True
    while len(draw_lst) == 8 and checker:
        if not wonStatus:
            drawStatus = True
        else:
            drawStatus = False
        checker = False


def playGame(player_One_Win, player_Two_Win, player_1, player_2, player_1_name, player_2_name):
    print("{} will play first!".format(player_1_name))
    while not wonStatus and not drawStatus:
        print("\n" * 50)
        display(player_One_Win, player_Two_Win)
        print("{} play!".format(player_1_name))
        player_1_error = False
        try:
            play_1 = int(input("Choose where to position your {}: ".format(player_1)))
            if play_1 not in range(1, 10):
                raise ValueError
        except ValueError:
            player_1_error = True

        while player_1_error:
            print("WRONG INPUT! Input must be between 1 and 9!")
            try:
                play_1 = int(input("Choose where to position your {} again: ".format(player_1)))
            except ValueError:
                continue
            if type(play_1) == int and play_1 in range(0, 10):
                player_1_error = False
            else:
                player_1_error = True

        if playLst[play_1] == "":
            playLst[play_1] = player_1
        else:
            player_1_repeat = True
            while player_1_repeat:
                print("SELECTED SLOT NOT EMPTY")
                try:
                    play_1 = int(input("Choose where to position your {}: ".format(player_1)))
                    if play_1 not in range(1, 10):
                        raise ValueError
                except ValueError:
                    player_1_error = True

                while player_1_error:
                    print("WRONG INPUT! Input must be between 1 and 9!")
                    try:
                        play_1 = int(input("Choose where to position your {} again: ".format(player_1)))
                    except ValueError:
                        continue
                    if type(play_1) == int and play_1 in range(0, 10):
                        player_1_error = False
                    else:
                        player_1_error = True

                if playLst[play_1] == "":
                    player_1_repeat = False
                    playLst[play_1] = player_1
                else:
                    player_1_repeat = True
        checkWin()
        checkDraw()
        if wonStatus:
            player_One_Win += "Congratulations {}! You have won the game!".format(player_1_name)
            player_Two_Win += "Sorry {}! You just lost!".format(player_2_name)
            print("\n" * 50)
            display(player_One_Win, player_Two_Win)
        if drawStatus:
            player_One_Win += "Phew! Game Drawn!"
            player_Two_Win += "Phew! Game Drawn!"
            print("\n" * 50)
            display(player_One_Win, player_Two_Win)
        if not wonStatus and not drawStatus:
            print("\n" * 50)
            display(player_One_Win, player_Two_Win)
            print("{} play!".format(player_2_name))
            player_2_error = False
            try:
                play_2 = int(input("Choose where to position your {}: ".format(player_2)))
                if play_2 not in range(1, 10):
                    raise ValueError
            except ValueError:
                player_2_error = True

            while player_2_error:
                print("WRONG INPUT! Input must be between 1 and 9!")
                try:
                    play_2 = int(input("Choose where to position your {} again: ".format(player_2)))
                except ValueError:
                    continue
                if type(play_2) == int and play_2 in range(0, 10):
                    player_2_error = False
                else:
                    player_2_error = True

            if playLst[play_2] == "":
                playLst[play_2] = player_2
            else:
                player_2_repeat = True
                while player_2_repeat:
                    print("SELECTED SLOT NOT EMPTY!")
                    try:
                        play_2 = int(input("Choose where to position your {}: ".format(player_2)))
                        if play_2 not in range(1, 10):
                            raise ValueError
                    except ValueError:
                        player_2_error = True

                    while player_2_error:
                        print("WRONG INPUT! Input must be between 1 and 9!")
                        try:
                            play_2 = int(input("Choose where to position your {} again: ".format(player_2)))
                        except ValueError:
                            continue
                        if type(play_2) == int and play_2 in range(0, 10):
                            player_2_error = False
                        else:
                            player_2_error = True

                    if playLst[play_2] == "":
                        player_2_repeat = False
                        playLst[play_2] = player_2
                    else:
                        player_2_repeat = True
                continue
            checkWin()
            checkDraw()
            if wonStatus:
                player_Two_Win += "Congratulations {}! You have won the game!".format(player_2_name)
                player_One_Win += "Sorry {}! You just lost!".format(player_1_name)
                print("\n" * 50)
                display(player_One_Win, player_Two_Win)
            if drawStatus:
                player_One_Win += "Phew! Game Drawn!"
                player_Two_Win += "Phew! Game Drawn!"
                print("\n" * 50)
                display(player_One_Win, player_Two_Win)


def main():
    print("WELCOME TO THE TIC-TAC-TOE GAME BOARD")
    display(PlayerOneWin, PlayerTwoWin)
    player1, player2, player1name, player2name = identify()
    global checker2

    def startGame():
        playGame(PlayerOneWin, PlayerTwoWin, player1, player2, player1name, player2name)

    def replayGame(choice):
        global checker2
        if choice == "Y":
            global wonStatus, drawStatus, playLst
            wonStatus = False
            drawStatus = False
            playLst = ["#", "", "", "", "", "", "", "", "", ""]
            startGame()
        else:
            checker2 = False

    startGame()

    while checker2:
        choice000 = input("Do you want to play again? Y or N: ").upper()

        while choice000 != "Y" and choice000 != "N":
            choice000 = input("WRONG! Please select Y or N: ").upper()
        replayGame(choice000)

    while not checker2:
        print("\n" * 50)
        print("THANK YOU! GAME WILL BE EXITED!")
        break


main()
