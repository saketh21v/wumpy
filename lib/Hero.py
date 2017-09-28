class Hero(object):
    def __init__(self, board, xCoord, yCoord, drone):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.board = board
        self.drone = drone

    def moveSelf(self, direction):
        if direction == 'left':
            if self.xCoord - 1 < 0:
                return False
            self.xCoord -= 1
        elif direction == 'right':
            if self.xCoord + 1 > self.board.xEdge:
                return False
            self.xCoord += 1
        elif direction == 'up':
            if self.yCoord - 1 < 0:
                return False
            self.yCoord -= 1
        elif direction == 'down':
            if self.yCoord + 1 > self.board.yEdge:
                return False
            self.yCoord += 1
        return True

    def moveDrone(self, direction):
        drone = self.drone
        if direction == 'left':
            if drone.xCoord - 1 < 0:
                return "Invalid"
            drone.xCoord -= 1
        elif direction == 'right':
            if drone.xCoord + 1 > drone.board.xEdge:
                return False
            drone.xCoord += 1
        elif direction == 'up':
            if drone.yCoord - 1 < 0:
                return False
            drone.yCoord -= 1
        elif direction == 'down':
            if drone.yCoord + 1 > drone.board.yEdge:
                return False
            drone.yCoord += 1
