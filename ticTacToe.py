class Players:
    def __init__(self, symbol):
        self._symbol = symbol
        if symbol == 'X':
            self._number = -1
        elif symbol == 'O':
            self._number = 0
        self._wins = 0

    def win(self):
        self._wins += 1

class ticTacToe:
    def clearPlayGround(self):
        print('\n## NEW GAME ##\n')
        self._playGround = [[i + 3 * j for i in range(1, 4)] for j in range(3)]
        self._playsNumber = 0

    def __init__(self):
        self.clearPlayGround()
        self._p1 = Players('X')
        self._p2 = Players('O')
        self._playsNumber = 0
        self._turn = self._p1

    def showPlayGround(self):
        for i in range(3):
            print(*['X' if self._playGround[i][j] == -1 else 'O' if self._playGround[i][j] == 0 else self._playGround[i][j] for j in range(3)])

    def playerWin(self):
        print('======================')
        self.showPlayGround()
        print(f'{self._turn._symbol} wins !\n')
        self._turn.win()
        print(f'X : {self._p1._wins}\tO : {self._p2._wins}')
        self.clearPlayGround()
        return True


    def draw(self):
        print('======================')
        self.showPlayGround()
        print('draw !')
        self.clearPlayGround()
        return True

    def playAndCheck(self):
        self.showPlayGround()
        self._playsNumber += 1
        place = input(f'{self._turn._symbol} turn\n')
        while True:
            try:
                place = int(place) - 1
                x = place % 3
                y = int(place / 3)
                if self._playGround[y][x] <= 0:
                    raise ValueError()
                break
            except:
                print('enter a valid place\n')
                place = input(f'{self._turn._symbol} turn')
        self._playGround[y][x] = self._turn._number
        
        if (self._playGround[y][0] == self._playGround[y][1] == self._playGround[y][2]):
            return self.playerWin()
        elif (self._playGround[0][x] == self._playGround[1][x] == self._playGround[2][x]):
            return self.playerWin()
        elif (self._playGround[0][0] == self._playGround[1][1] == self._playGround[2][2]):
            return self.playerWin()
        elif (self._playGround[2][0] == self._playGround[1][1] == self._playGround[0][2]):
            return self.playerWin()
        elif self._playsNumber == 9:
            return self.draw()
        else:
            if self._turn == self._p1:
                self._turn = self._p2
            else:
                self._turn = self._p1


game = ticTacToe()

while True:
    while not game.playAndCheck():
        pass

