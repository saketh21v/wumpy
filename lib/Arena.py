from random import randint


def makeBoard(size, inter):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(inter)
    return board


class _NOTATIONS:
    EMPTY = 0
    HERO = 1
    GOLD = 2
    WUMPUS = 3
    PIT = 4
    GLITTER = 5
    STENCH = 6
    BREEZE = 7


class Arena:
    def __init__(self, N):
        self._SIZE = N
        self._EDGE = N - 1
        self.board = makeBoard(N, _NOTATIONS.EMPTY)
        self.stenchBoard = makeBoard(N, 0)
        self.breezeBoard = makeBoard(N, 0)
        self.wumpusBoard = makeBoard(N, 0)
        self.goldBoard = makeBoard(N, 0)
        self.pitBoard = makeBoard(N, 0)

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
        self.goldBoard[self.goldY][self.goldX] = _NOTATIONS.GOLD
        # Not Generating glitter in this version

        # WUMPUS
        self.wumpusX = randint(0, self._EDGE)
        self.wumpusY = randint(0, self._EDGE)

        while self.board[self.wumpusY][self.wumpusX] != 0:
            self.wumpusX = randint(0, self._EDGE)
            self.wumpusY = randint(0, self._EDGE)

        print("WUMPUS: ", self.wumpusX, ", ", self.wumpusY)
        self.board[self.wumpusY][self.wumpusX] = _NOTATIONS.WUMPUS
        self.wumpusBoard[self.wumpusY][self.wumpusX] = _NOTATIONS.WUMPUS
        self.genStench()
        self.genPits(3)

    def isSafe(self, x, y):
        if x < 0: return False
        if y < 0: return False
        if x > self._EDGE: return False
        if y > self._EDGE: return False
        return True

    def genStench(self):
        x = self.wumpusX
        y = self.wumpusY
        if self.isSafe(x-1, y):
            self.stenchBoard[y][x-1] = _NOTATIONS.STENCH
        if self.isSafe(x, y-1):
            self.stenchBoard[y-1][x] = _NOTATIONS.STENCH
        if self.isSafe(x+1, y):
            self.stenchBoard[y][x+1] = _NOTATIONS.STENCH
        if self.isSafe(x, y+1):
            self.stenchBoard[y+1][x] = _NOTATIONS.STENCH
        return 

    
    def genBreeze(self, x, y):
        if self.isSafe(x-1, y):
            self.breezeBoard[y][x-1] = _NOTATIONS.BREEZE
        if self.isSafe(x, y-1):
            self.breezeBoard[y-1][x] = _NOTATIONS.BREEZE
        if self.isSafe(x+1, y):
            self.breezeBoard[y][x+1] = _NOTATIONS.BREEZE
        if self.isSafe(x, y+1):
            self.breezeBoard[y+1][x] = _NOTATIONS.BREEZE

    def genPits(self, NPITS):
        emptyCells = 0
        for i in range(self._EDGE):
            emptyCells += self.board[i].count(_NOTATIONS.EMPTY)
        if NPITS > emptyCells:
            for x in range(self._EDGE):
                for y in range(self._EDGE):
                    if self.board[y][x] == 0:
                        self.board[y][x] = _NOTATIONS.PIT
                        self.pitBoard[y][x] = _NOTATIONS.PIT
                        self.genBreeze(x, y)
        else:
            for i in range(NPITS):
                x = randint(0, self._EDGE)
                y = randint(0, self._EDGE)
                print("x = ", x, " y = ", y, " code = ",self.board[y][x])
                while self.board[y][x] != 0:
                    x = randint(0, self._EDGE - 1)
                    y = randint(0, self._EDGE - 1)
                self.board[y][x] = _NOTATIONS.PIT
                self.pitBoard[y][x] = _NOTATIONS.PIT
                self.genBreeze(x, y)
        return

    def printEverything(self):
        print("Hero: ", self.heroX, ", ", self.heroY)
        print("GOLD: ", self.goldX, ", ", self.goldY)
        print("WUMPUS: ", self.wumpusX, ", ", self.wumpusY)
        print("Board: ")
        for i in range(0, self._EDGE+1):
            print(self.board[i])
        print("Stench: ")
        for i in range(0, self._EDGE+1):
            print(self.stenchBoard[i])
        print("Breeze: ")
        for i in range(0, self._EDGE+1):
            print(self.breezeBoard[i])
        print("Pits: ")
        for i in range(0, self._EDGE+1):
            print(self.pitBoard[i])

    def printBoard(self):
        print("Board: ")
        for i in range(0, self._EDGE+1):
            print(self.board[i])