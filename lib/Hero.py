from lib.Arena import _NOTATIONS


class Hero(object):
    def __init__(self, arena, drone):
        self.xCoord = arena.heroX
        self.yCoord = arena.heroY
        self.arena = arena
        self.board = arena.board
        self.drone = drone

    def getSensoryInput(self):
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
        if direction == 'left':
            print("Turning left")
            if self.xCoord - 1 < 0:
                return False
            self.xCoord -= 1
        elif direction == 'right':
            print("Turning right")
            if self.xCoord + 1 > self.arena._EDGE:
                return False
            self.xCoord += 1
        elif direction == 'up':
            print("Turning up")
            if self.yCoord - 1 < 0:
                return False
            self.yCoord -= 1
        elif direction == 'down':
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
        if direction == 'left':
            if drone.xCoord - 1 < 0:
                return "Invalid"
            drone.xCoord -= 1
        elif direction == 'right':
            if drone.xCoord + 1 > drone.arena._EDGE:
                return False
            drone.xCoord += 1
        elif direction == 'up':
            if drone.yCoord - 1 < 0:
                return False
            drone.yCoord -= 1
        elif direction == 'down':
            if drone.yCoord + 1 > drone.arena._EDGE:
                return False
            drone.yCoord += 1
