import random


class player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

    def coinToss(self, p1num, p2num):
        randomN = random.randint(1, 2)
        print(randomN)
        return randomN


class board:

    def __init__(self):
        self.boardPieces = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def display(self):
        print("%s|%s|%s" % (self.boardPieces[1], self.boardPieces[2], self.boardPieces[3]))
        print("%s|%s|%s" % (self.boardPieces[4], self.boardPieces[5], self.boardPieces[6]))
        print("%s|%s|%s" % (self.boardPieces[7], self.boardPieces[8], self.boardPieces[9]))

    def changeBoardPiece(self, num, playerChar):
        if self.boardPieces[num] == " ":
            # temp = self.boardPieces.index(num)
            self.boardPieces.pop(num)
            self.boardPieces.insert(num, playerChar)
            # self.displayBoardPiece.insert(num, playerChar)

        else:
            print('Gamebot: there is already a letter here!')

    def getTurn(self, letter):
        while True:
            entry = input(print(" Gamebot :Please enter your move by selecting a number from the available moves:"))
            if entry in self.boardPieces:
                temp = self.boardPieces.index(entry)
                self.boardPieces.pop(temp)
                self.boardPieces.insert(temp, letter)
                break
            else:
                print('incorrect entry please try again')

    def getCpuTurn(self, letter):
        if self.boardPieces[5] != 'x' and self.boardPieces[5] != 'o':
            self.boardPieces.pop(5)
            self.boardPieces.insert(5, letter)
        elif self.boardPieces[2] == '2':
            self.boardPieces.pop(2)
            self.boardPieces.insert(2, letter)
        elif self.boardPieces[4] == '4':
            self.boardPieces.pop(4)
            self.boardPieces.insert(4, letter)
        elif self.boardPieces[6] == '6':
            self.boardPieces.pop(6)
            self.boardPieces.insert(6, letter)
        elif self.boardPieces[8] == '8':
            self.boardPieces.pop(8)
            self.boardPieces.insert(8, letter)
        elif self.boardPieces[1] == '1':
            self.boardPieces.pop(1)
            self.boardPieces.insert(1, letter)
        elif self.boardPieces[3] == '3':
            self.boardPieces.pop(3)
            self.boardPieces.insert(3, letter)
        elif self.boardPieces[7] == '7':
            self.boardPieces.pop(7)
            self.boardPieces.insert(7, letter)
        elif self.boardPieces[9] == '9':
            self.boardPieces.pop(9)
            self.boardPieces.insert(9, letter)

    def checkIfTie(self):
        if "1" not in self.boardPieces and "2" not in self.boardPieces and "3" not in self.boardPieces and "4" not in self.boardPieces and "5" not in self.boardPieces and "6" not in self.boardPieces and "7" not in self.boardPieces and "8" not in self.boardPieces and "9" not in self.boardPieces:
            return True
        else:
            return False

    def checkWinDiagonal(self):
        if self.boardPieces[1] == self.boardPieces[5] == self.boardPieces[9] or self.boardPieces[3] == self.boardPieces[
            5] == self.boardPieces[7]:
            return True

        else:
            return False

    def checkWinVertical(self):
        if self.boardPieces[1] == self.boardPieces[2] == self.boardPieces[3] or self.boardPieces[4] == self.boardPieces[
            5] == self.boardPieces[6] or self.boardPieces[7] == self.boardPieces[8] == self.boardPieces[9]:
            return True
        else:
            return False

    def checkWinHorizontal(self):
        if self.boardPieces[1] == self.boardPieces[4] == self.boardPieces[7] or self.boardPieces[2] == self.boardPieces[
            5] == self.boardPieces[8] or self.boardPieces[3] == self.boardPieces[6] == self.boardPieces[9]:
            return True
        else:
            return False


class game:
    def __init__(self, p1num, p2num):
        self.p1num = p1num
        self.p1num = p2num

    def coinToss(self, p1num, p2num):
        randomN = random.randint(1, 2)
        return randomN

    b = board()
    playAgain = 'yes'
    while playAgain == 'yes':

        print('GameBot: welcome to tictac toe!')
        gameType = input(
            print('GameBot: please select from the following options: [1] Human vs Human [2] Human vs AI [3] AI vs AI'))
        if gameType == '1':
            p1Name = input(print('GameBot: player 1 will be x please enter your name:'))
            p1Letter = 'x'
            p1 = player(p1Name, p1Letter)

            p2Name = input(print('GameBot: player 2 will be o, please enter your name:'))
            p2Letter = 'o'
            p2 = player(p2Name, p2Letter)
            p1num = 1
            p2num = 2
            print('Gamebot: game initiated ' + p1Name + ' vs. ' + p2Name)

            randomN = p1.coinToss(p1num, p2num)
            if randomN == 1:
                print('GameBoard: ' + p1.name + ' who won the cointoss and has x will go first, ')
                while True:
                    b.display()
                    print('GameObject: player 1 turn')
                    b.display()
                    b.getTurn(p1Letter)
                    tValue = b.checkIfTie()
                    if tValue:
                        print('GameBot: Oh No its a tie')
                        break
                    else:
                        dValue = b.checkWinDiagonal()
                        if dValue:
                            print('player 1 wins!')
                            b.display()
                            break
                        else:
                            vValue = b.checkWinVertical()
                            if vValue:
                                print('Player 1 wins!')
                                b.display()
                                break
                            else:
                                hValue = b.checkWinHorizontal()
                                if hValue:
                                    print('player 1 wins!')
                                    b.display()
                                    break
                                else:
                                    print('GameObject: player 2 turn')
                                    b.display()
                                    b.getTurn(p2Letter)
                                    tValue = b.checkIfTie()
                                    if tValue:
                                        b.display()
                                        print('GameBot: Oh No its a tie')
                                        break
                                    else:
                                        dValue = b.checkWinDiagonal()
                                        if dValue:
                                            b.display()
                                            print('player 2 wins!')
                                            break
                                        else:
                                            vValue = b.checkWinVertical()
                                            if vValue:
                                                b.display()
                                                print('Player 2 wins!')

                                                break
                                            else:
                                                hValue = b.checkWinHorizontal()
                                                if hValue:
                                                    b.display()
                                                    print('player 2 wins!')

                                                    break
            elif randomN == 2:
                while True:
                    b.display()
                    print('GameObject: player 2 turn')
                    b.display()
                    b.getTurn(p2Letter)
                    tValue = b.checkIfTie()
                    if tValue:
                        print('GameBot: Oh No its a tie')
                        break
                    else:
                        dValue = b.checkWinDiagonal()
                        if dValue:
                            print('player 2 wins!')
                            b.display()
                            break
                        else:
                            vValue = b.checkWinVertical()
                            if vValue:
                                print('Player 2 wins!')
                                b.display()
                                break
                            else:
                                hValue = b.checkWinHorizontal()
                                if hValue:
                                    print('player 2 wins!')
                                    b.display()
                                    break
                                else:
                                    print('GameObject: player 1 turn')
                                    b.display()
                                    b.getTurn(p1Letter)
                                    tValue = b.checkIfTie()
                                    if tValue:
                                        b.display()
                                        print('GameBot: Oh No its a tie')
                                        break
                                    else:
                                        dValue = b.checkWinDiagonal()
                                        if dValue:
                                            b.display()
                                            print('player 1 wins!')
                                            break
                                        else:
                                            vValue = b.checkWinVertical()
                                            if vValue:
                                                b.display()
                                                print('Player 1 wins!')

                                                break
                                            else:
                                                hValue = b.checkWinHorizontal()
                                                if hValue:
                                                    b.display()
                                                    print('player 1 wins!')

                                                    break

        elif gameType == '2':
            p1Name = input(print('GameBot: player 1 will be x please enter your name:'))
            p1Letter = 'x'
            p1 = player(p1Name, p1Letter)

            p2Letter = 'o'
            p2Name = 'cpu'
            cpu = player(p2Name, p2Letter)

            p1num = 1
            cpuNum = 2
            print('Gamebot: game initiated ' + p1Name + ' vs. ' + p2Name)
            randomM = p1.coinToss(p1num, cpuNum)
            if randomM == 1:
                print('GameBoard: ' + p1.name + ' who won the cointoss and has x will go first, ')
                while True:
                    print('GameObject: player 1 turn')
                    b.display()
                    b.getTurn(p1Letter)
                    tValue = b.checkIfTie()
                    if tValue:
                        print('GameBot: Oh No its a tie')
                        break
                    else:
                        dValue = b.checkWinDiagonal()
                        if dValue:
                            print('player 1 wins!')
                            b.display()
                            break
                        else:
                            vValue = b.checkWinVertical()
                            if vValue:
                                print('Player 1 wins!')
                                b.display()
                                break
                            else:
                                hValue = b.checkWinHorizontal()
                                if hValue:
                                    print('player 1 wins!')
                                    b.display()
                                    break
                                else:
                                    print('GameObject: cpuTurn')
                                    b.getCpuTurn(p2Letter)
                                    tValue = b.checkIfTie()
                                    if tValue:
                                        b.display()
                                        print('GameBot: Oh No its a tie')
                                        break
                                    else:
                                        dValue = b.checkWinDiagonal()
                                        if dValue:
                                            b.display()
                                            print('cpu wins!')
                                            break
                                        else:
                                            vValue = b.checkWinVertical()
                                            if vValue:
                                                b.display()
                                                print('cpu wins!')

                                                break
                                            else:
                                                hValue = b.checkWinHorizontal()
                                                if hValue:
                                                    b.display()
                                                    print('cpu wins!')

                                                    break
            elif randomM == '2':
                print('cpu will go first')
                while True:
                    b.display()
                    print('cpu turn')
                    b.display()
                    b.getCpuTurn(p2Letter)
                    tValue = b.checkIfTie()
                    if tValue:
                        print('GameBot: Oh No its a tie')
                        break
                    else:
                        dValue = b.checkWinDiagonal()
                        if dValue:
                            print('cpu wins!')
                            b.display()
                            break
                        else:
                            vValue = b.checkWinVertical()
                            if vValue:
                                print('cpu  wins!')
                                b.display()
                                break
                            else:
                                hValue = b.checkWinHorizontal()
                                if hValue:
                                    print('cpu wins!')
                                    b.display()
                                    break
                                else:
                                    print('GameObject: player 1 turn')
                                    b.display()
                                    b.getTurn(p1Letter)
                                    tValue = b.checkIfTie()
                                    if tValue:
                                        b.display()
                                        print('GameBot: Oh No its a tie')
                                        break
                                    else:
                                        dValue = b.checkWinDiagonal()
                                        if dValue:
                                            b.display()
                                            print('player 1 wins!')
                                            break
                                        else:
                                            vValue = b.checkWinVertical()
                                            if vValue:
                                                b.display()
                                                print('Player 1 wins!')

                                                break
                                            else:
                                                hValue = b.checkWinHorizontal()
                                                if hValue:
                                                    b.display()
                                                    print('player 1 wins!')

                                                    break

        print("do you want to play again? (yes or no)")
        playAgain = input()
        if playAgain == 'y' or 'yes':
            continue
        else:
            break
