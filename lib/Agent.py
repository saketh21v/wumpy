from lib.Arena import Arena
from lib.Arena import _NOTATIONS
from lib.Arena import makeBoard


class _DIRECTION:
    RIGHT = 'RIGHT'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    UP = 'UP'


class Agent:
    def __init__(self, arena):
        self.arena = arena
        self.xCoord = arena.heroX
        self.yCoord = arena.heroY
        self.board = arena.board
        self.points = 0

    def getSenses(self):
        senses = {}

        senses['WUMPUS'] = (self.arena.wumpusBoard[self.yCoord]
                            [self.xCoord] == _NOTATIONS.WUMPUS)
        senses['GOLD'] = (self.arena.goldBoard[self.yCoord]
                          [self.xCoord] == _NOTATIONS.GOLD)
        senses['PIT'] = (self.arena.pitBoard[self.xCoord]
                         [self.yCoord] == _NOTATIONS.PIT)
        senses['GLITTER'] = (self.board[self.yCoord]
                             [self.xCoord] == _NOTATIONS.GLITTER)
        senses['STENCH'] = (self.arena.stenchBoard[self.yCoord]
                            [self.xCoord] == _NOTATIONS.STENCH)
        senses['BREEZE'] = (self.arena.breezeBoard[self.yCoord]
                            [self.xCoord] == _NOTATIONS.BREEZE)
        return senses

    def isSafe(self, x, y):
        return self.arena.isSafe(x, y)

    def move(self, direction, vBoard):
        prevX = self.xCoord
        prevY = self.yCoord
        arena = self.arena

        if direction == _DIRECTION.RIGHT:
            print("Turning Right")
            if self.isSafe(self.xCoord + 1, self.yCoord):
                self.xCoord += 1
            else:
                return False
        elif direction == _DIRECTION.DOWN:
            print("Turing Down")
            if self.isSafe(self.xCoord, self.yCoord + 1):
                self.yCoord += 1
            else:
                return False
        elif direction == _DIRECTION.LEFT:
            print("Turing Left")
            if self.isSafe(self.xCoord - 1, self.yCoord):
                self.xCoord -= 1
            else:
                return False
        elif direction == _DIRECTION.UP:
            print("Turing UP")
            if self.isSafe(self.xCoord, self.yCoord - 1):
                self.yCoord -= 1
            else:
                return False
        self.board[prevY][prevX] = _NOTATIONS.EMPTY
        print("Moved to ", self.yCoord, ", ", self.xCoord)
        self.board[self.yCoord][self.xCoord] = _NOTATIONS.HERO
        vBoard[self.yCoord][self.xCoord] += 1
        self.points -= 10
        return True

    def getXY(self, direc, x, y):
        if direc == _DIRECTION.RIGHT:
            return x + 1, y
        if direc == _DIRECTION.LEFT:
            return x - 1, y
        if direc == _DIRECTION.DOWN:
            return x, y + 1
        if direc == _DIRECTION.UP:
            return x, y - 1

    def isVisited(x, y, vBoard):
        return vBoard[y][x] != 0

    def setCell(self, x, y, CODE, board):
        if x < 0 or y < 0 or x > self.arena._EDGE or y > self.arena._EDGE:
            return
        if board[y][x] == -1:
            board[y][x] = CODE

    def play(self):
        vBoard= makeBoard(self.arena._SIZE, 0)
        wBoard= makeBoard(self.arena._SIZE, 0)
        pBoard= makeBoard(self.arena._SIZE, 0)

        senses= self.getSenses()

        if senses['WUMPUS'] or senses['PIT'] or senses['GOLD']:
            print("Wrong setup. Agent start position overlapping")
            return

        while not(senses['WUMPUS'] or senses['PIT'] or senses['GOLD']):
            direc= {'RIGHT': False, 'DOWN': False, 'LEFT': False, 'UP': False}
            x= self.xCoord
            y= self.yCoord

            goDirec= '' # Final direction to go

            if senses['BREEZE']:
                print("Setting Breeze")
                self.setCell(x - 1, y, _NOTATIONS.PIT, pBoard)
                self.setCell(x + 1, y, _NOTATIONS.PIT, pBoard)
                self.setCell(x, y - 1, _NOTATIONS.PIT, pBoard)
                self.setCell(x, y + 1, _NOTATIONS.PIT, pBoard)
            if senses['STENCH']:
                print("Setting Wumpus")
                self.setCell(x - 1, y, _NOTATIONS.WUMPUS, wBoard)
                self.setCell(x + 1, y, _NOTATIONS.WUMPUS, wBoard)
                self.setCell(x, y - 1, _NOTATIONS.WUMPUS, wBoard)
                self.setCell(x, y + 1, _NOTATIONS.WUMPUS, wBoard)
            if senses['GLITTER']:
                self.setCell(x - 1, y, _NOTATIONS.GOLD, pBoard)
                self.setCell(x + 1, y, _NOTATIONS.GOLD, pBoard)
                self.setCell(x, y - 1, _NOTATIONS.GOLD, pBoard)
                self.setCell(x, y + 1, _NOTATIONS.GOLD, pBoard)

            noDir= True
            print("X = ", x, " Y = ", y)

            for d in direc:
                sX, sY = self.getXY(d, x, y)
                print("Testing coords = ", sX, ", ", sY)

                if not self.isSafe(sX, sY):
                    continue
                # Else => isSafe
                # Have to check if any pits or wumpus maybe present there
                # Need to improve this. This is very stupid
                if not (pBoard[sY][sX] == _NOTATIONS.PIT or wBoard[sY][sX] == _NOTATIONS.WUMPUS):
                    direc[d]= True
                    print("Direction ", d, "is okay")
                    noDir= False

            # Out of for loop. Checking if any valid path
            if noDir:
                break

            possibleDirecs= [] # Get possible directions and choose best one
            for d in direc:
                # print("checking ", d," ",direc[d])
                if direc[d]:
                    possibleDirecs.append(d)

            for d in possibleDirecs:  # Checking if any direction which the player hasn't visited before
                sX, sY= self.getXY(d, x, y)
                if not Agent.isVisited(sX, sY, vBoard):
                    goDirec= d
                    break
                
            if goDirec == '':  # The player has visited all directions
                sX, sY= self.getXY(possibleDirecs[0], x, y)
                mi = vBoard[sY][sX]
                goDirec = possibleDirecs[0]
                for d in possibleDirecs:
                    sX, sY= self.getXY(d, x, y)
                    if mi > vBoard[sY][sX]:
                        mi = vBoard[sY][sX]
                        goDirec = d
            
            self.move(goDirec, vBoard)
            print("Direction = " + goDirec)
            self.arena.printBoard()
            senses = self.getSenses()
            print("Senses = ", senses)
            # End of the while loop
        
        self.arena.printBoard()
        print("Senses = ", senses)
        if senses['GOLD']:
            self.points += 1000
            print("I'm rich")
        if senses['WUMPUS']:
            self.points -= 1000
            print("Wumpus ate me.")
        if senses['PIT']:
            self.points -= 300
            print("Fell in the pit.")
        print("Points = ", self.points)
