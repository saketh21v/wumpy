from lib.Arena import Arena
from lib.Hero import Hero
from random import randint


arena = Arena(5)

hero = Hero(arena, None)

arena.printEverything()

print("Moved = ", hero.moveSelf('right'))
arena.printBoard()
print(hero.xCoord, ", ", hero.yCoord)
print(hero.getSensoryInput())

print("Moved = ", hero.moveSelf('right'))
arena.printBoard()
print(hero.xCoord, ", ", hero.yCoord)
print(hero.getSensoryInput())

print("Moved = ", hero.moveSelf('right'))
arena.printBoard()
print(hero.xCoord, ", ", hero.yCoord)
print(hero.getSensoryInput())
