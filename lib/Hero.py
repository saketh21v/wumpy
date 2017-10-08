from lib.Arena import _NOTATIONS
from lib.Arena import makeBoard

class _DIRECTION:
    RIGHT = 'RIGHT'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    UP = 'UP'

class Hero(object):
    
    def __init__(self, arena, drone):
        self.xCoord = arena.heroX
        self.yCoord = arena.heroY
        self.arena = arena
        self.board = arena.board
        self.drone = drone
        self.points = 0

    def getSenses(self):
        senses = {}
        code = self.board[self.xCoord][self.yCoord]
        senses['WUMPUS'] = (code == _NOTATIONS.WUMPUS)
        senses['GOLD'] = (code == _NOTATIONS.GOLD)
        senses['PIT'] = (code == _NOTATIONS.PIT)
        senses['GLITTER'] = (code == _NOTATIONS.GLITTER)
        senses['STENCH'] = (code == _NOTATIONS.STENCH)
        senses['BREEZE'] = (code == _NOTATIONS.BREEZE)
        return senses

    def moveSelf(self, direction):
        prevX = self.xCoord
        prevY = self.yCoord
        if direction == _DIRECTION.LEFT:
            print("Turning left")
            if self.xCoord - 1 < 0:
                return False
            self.xCoord -= 1
        elif direction == _DIRECTION.RIGHT:
            print("Turning right")
            if self.xCoord + 1 > self.arena._EDGE:
                return False
            self.xCoord += 1
        elif direction == _DIRECTION.UP:
            print("Turning up")
            if self.yCoord - 1 < 0:
                return False
            self.yCoord -= 1
        elif direction == _DIRECTION.DOWN:
            print("Turning down")
            if self.yCoord + 1 > self.arena._EDGE:
                return False
            self.yCoord += 1
        self.board[prevY][prevX] = _NOTATIONS.EMPTY
        print(self.yCoord, ", ", self.xCoord)
        self.board[self.yCoord][self.xCoord] = _NOTATIONS.HERO
        return True

    def moveDrone(self, direction):
        drone = self.drone
        if direction == _DIRECTION.LEFT:
            if drone.xCoord - 1 < 0:
                return "Invalid"
            drone.xCoord -= 1
        elif direction == _DIRECTION.RIGHT:
            if drone.xCoord + 1 > drone.arena._EDGE:
                return False
            drone.xCoord += 1
        elif direction == _DIRECTION.UP:
            if drone.yCoord - 1 < 0:
                return False
            drone.yCoord -= 1
        elif direction == _DIRECTION.DOWN:
            if drone.yCoord + 1 > drone.arena._EDGE:
                return False
            drone.yCoord += 1

        


    def setCell(self, x, y, CODE, board):
        if x < 0 or y < 0 or x > self.arena._EDGE or y > self.arena._EDGE:
            return
        if board[x][y] == -1:
            board[x][y] = CODE
            return 
        
    def isSafeDirec(self, x, y):
        if x < 0 or y < 0 or x > self.arena._EDGE or y > self.arena._EDGE:
            return False
        return True
    def getXY(self, direc, x, y):
        if direc == _DIRECTION.RIGHT:
            return x+1, y
        if direc == _DIRECTION.LEFT:
            return x-1, y
        if direc == _DIRECTION.DOWN:
            return x, y+1
        if direc == _DIRECTION.UP:
            return x, y-1

    def play(self):
        direc = {'RIGHT':False, 'DOWN':False, 'LEFT':False, 'UP': False}
        x = self.xCoord
        y = self.yCoord
        pBoard = makeBoard(self.arena._EDGE + 1, -1)
        wBoard = makeBoard(self.arena._EDGE + 1, -1)
        gBoard = makeBoard(self.arena._EDGE + 1, -1)
        bBoard = makeBoard(self.arena._EDGE + 1, -1)
        senses = self.getSenses()
        while not (senses['WUMPUS'] or senses['GOLD'] or senses['PIT']):
            cDirec = ''
            if senses['BREEZE']:
                self.setCell(x-1,y,_NOTATIONS.PIT, pBoard)
                self.setCell(x+1,y,_NOTATIONS.PIT, pBoard)
                self.setCell(x,y-1,_NOTATIONS.PIT, pBoard)
                self.setCell(x,y+1,_NOTATIONS.PIT, pBoard)
            elif senses['STENCH']:
                self.setCell(x-1,y,_NOTATIONS.WUMPUS, pBoard)
                self.setCell(x+1,y,_NOTATIONS.WUMPUS, pBoard)
                self.setCell(x,y-1,_NOTATIONS.WUMPUS, pBoard)
                self.setCell(x,y+1,_NOTATIONS.WUMPUS, pBoard)
            elif senses['GLITTER']:
                self.setCell(x-1,y,_NOTATIONS.GOLD, pBoard)
                self.setCell(x+1,y,_NOTATIONS.GOLD, pBoard)
                self.setCell(x,y-1,_NOTATIONS.GOLD, pBoard)
                self.setCell(x,y+1,_NOTATIONS.GOLD, pBoard)
            
            # Setting Y/N in bBoard
            # Choose next move and set direc
            
            noDir = True
            for d in direc:
                sX, sY = self.getXY(d, x, y)
                if self.isSafeDirec(d, sX, sY):
                    if not (pBoard[sX][xY] == _NOTATIONS.PIT or wBoard[sX][sY] == _NOTATIONS.WUMPUS):
                        direc[d] = True
                        noDir = False
                        cDirec = d
            if noDir:
                break
            self.moveSelf(d)
            self.points -= 10

        if senses['GOLD']:
            self.points+=1000
        print("Points = " + points)