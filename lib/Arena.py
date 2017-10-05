from random import randint

# HERO = 'H'
# GOLD = 'G'
# WUMPUS = '3'
# PIT = 'P'
# GLITTER = 'GL'
# STENCH = 'S'
# BREEZE = 'B'


class _NOTATIONS:
    EMPTY = 0
    HERO = 1
    GOLD = 2
    WUMPUS = 3
    PIT = 4
    GLITTER = 5
    STENCH = 6
    BREEZE = 7


def makeBoard(N):
    board = []
    for i in range(0, N):
            board.append([])
    for item in board:
        for i in range(0, N):
            item.append(0)
    return board

class Arena(object):
    def __init__(self, N):
        self._EDGE = N - 1
        self.board = makeBoard(N)
        self.stenchBoard = makeBoard(N)
        self.breezeBoard = makeBoard(N)

        print("SIZE = ", len(self.board), ", ", len(self.board[0]))

        # Generating Locations
        # Hero
        self.heroX = randint(0, self._EDGE)
        self.heroY = randint(0, self._EDGE)

        print("Hero: ", self.heroX, ", ", self.heroY)
        self.board[self.heroY][self.heroX] = _NOTATIONS.HERO

        # GOLD
        self.goldX = randint(0, self._EDGE)
        self.goldY = randint(0, self._EDGE)
        while self.board[self.goldY][self.goldX]:
            self.goldY = randint(0, self._EDGE)
            self.goldX = randint(0, self._EDGE)

        print("GOLD: ", self.goldX, ", ", self.goldY)
        self.board[self.goldY][self.goldX] = _NOTATIONS.GOLD
        # Not Generating glitter in this version

        # WUMPUS
        self.wumpusX = randint(0, self._EDGE)
        self.wumpusY = randint(0, self._EDGE)

        while self.board[self.wumpusY][self.wumpusX] != 0:
            self.wumpusX = randint(0, self._EDGE)
            self.wumpusY = randint(0, self._EDGE)

        print("WUMPUS: ", self.wumpusX, ", ", self.wumpusY)
        self.board[self.wumpusY][self.wumpusX] = _NOTATIONS.WUMPUS
        self.genStench()
        self.genPits(3)

    def genStench(self):
        x = self.wumpusX
        y = self.wumpusY

        if y > 0:
            self.stenchBoard[y - 1][x] = _NOTATIONS.STENCH
        if y < self._EDGE - 1:
            self.stenchBoard[y + 1][x] = _NOTATIONS.STENCH
        if x > 0:
            self.stenchBoard[y][x - 1] = _NOTATIONS.STENCH
        if x < self._EDGE - 1:
            self.stenchBoard[y][x + 1] = _NOTATIONS.STENCH

    def genPits(self, NPITS):
        emptyCells = 0
        for i in range(self._EDGE):
            emptyCells += self.board[i].count(0)
        if NPITS > emptyCells:
            for i in range(self._EDGE):
                for j in range(self._EDGE):
                    if self.board[i][j] == 0:
                        self.board[i][j] = _NOTATIONS.PIT
                        self.genBreeze(i, j)
            # return True
        else:
            for i in range(NPITS):
                x = randint(0, self._EDGE - 1)
                y = randint(0, self._EDGE - 1)
                print("x = ", x, " y = ", y, " code = ",self.board[x][y])
                while self.board[x][y] != 0:
                    x = randint(0, self._EDGE - 1)
                    y = randint(0, self._EDGE - 1)
                self.board[x][y] = _NOTATIONS.PIT
                self.genBreeze(x, y)
        # return True

    def genBreeze(self, x, y):
        if y > 0:
            self.breezeBoard[y - 1][x] = _NOTATIONS.BREEZE
        if y < self._EDGE - 1:
            self.breezeBoard[y + 1][x] = _NOTATIONS.BREEZE
        if x > 0:
            self.breezeBoard[y][x - 1] = _NOTATIONS.BREEZE
        if x < self._EDGE - 1:
            self.breezeBoard[y][x + 1] = _NOTATIONS.BREEZE

    def isValid(self, x, y):
        xTrue = True
        yTrue = True
        if x > self._EDGE or x < 0:
            xTrue = False
        if y > self._EDGE or y < 0:
            yTrue = False
        return xTrue, yTrue

    def printEverything(self):
        print("Hero: ", self.heroX, ", ", self.heroY)
        print("GOLD: ", self.goldX, ", ", self.goldY)
        print("WUMPUS: ", self.wumpusX, ", ", self.wumpusY)
        print("Board: ")
        for i in range(0, self._EDGE):
            print(self.board[i])
        print("Stench: ")
        for i in range(0, self._EDGE):
            print(self.stenchBoard[i])
        print("Breeze: ")
        for i in range(0, self._EDGE):
            print(self.breezeBoard[i])

    def printBoard(self):
        print("Board: ")
        for i in range(0, self._EDGE+1):
            print(self.board[i])

# arena = Arena(5)
# arena.printEverything()
