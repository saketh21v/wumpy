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


class Arena(object):
    def __init__(self, N):
        self._EDGE = N
        self.board = []
        for i in range(0, N):
            self.board.append([])
        for item in self.board:
            for i in range(0, N):
                item.append(0)

        print("SIZE = ", len(self.board), ", ", len(self.board[0]))

        # Generating Locations
        # Hero
        self.heroX = randint(0, N - 1)
        self.heroY = randint(0, N - 1)

        print("Hero: ", self.heroX, ", ", self.heroY)
        self.board[self.heroX][self.heroY] = _NOTATIONS.HERO

        # GOLD
        self.goldX = randint(0, N - 1)
        self.goldY = randint(0, N - 1)
        while self.board[self.goldX][self.goldY]:
            self.goldX = randint(0, N - 1)
            self.goldY = randint(0, N - 1)

        print("GOLD: ", self.goldX, ", ", self.goldY)
        self.board[self.goldX][self.goldY] = _NOTATIONS.GOLD

        # WUMPUS
        self.wumpusX = randint(0, N - 1)
        self.wumpusY = randint(0, N - 1)

        while self.board[self.wumpusX][self.wumpusY] != 0:
            self.wumpusX = randint(0, N - 1)
            self.wumpusY = randint(0, N - 1)

        print("WUMPUS: ", self.wumpusX, ", ", self.wumpusY)
        self.board[self.wumpusX][self.wumpusY] = _NOTATIONS.WUMPUS

        self.genStench()

    def genStench(self):
        x = self.wumpusX
        y = self.wumpusY

        if x > 0:
            self.board[x - 1][y] = _NOTATIONS.STENCH
        if x < self._EDGE:
            self.board[x + 1][y] = _NOTATIONS.STENCH
        if y > 0:
            self.board[x][y - 1] = _NOTATIONS.STENCH
        if y < self._EDGE:
            self.board[x][y + 1] = _NOTATIONS.STENCH

    def isValid(self, x, y):
        xTrue = True
        yTrue = True
        if x > self._EDGE or x < 0:
            xTrue = False
        if y > self._EDGE or y < 0:
            yTrue = False
        return xTrue, yTrue

    def printBoard(self):
        for i in range(0, self._EDGE):
            print(self.board[i])
        print("Hero: ", self.heroX, ", ", self.heroY)
        print("GOLD: ", self.goldX, ", ", self.goldY)
        print("WUMPUS: ", self.wumpusX, ", ", self.wumpusY)

arena = Arena(5)
arena.printBoard()
