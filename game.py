from lib.Arena import Arena
from lib.Hero import Hero
from random import randint


arena = Arena(5)

hero = Hero(arena, None)

arena.printEverything()

points = hero.play()