from lib.Arena import Arena
from lib.Agent import Agent
from random import randint


arena = Arena(5)

hero = Agent(arena)

arena.printEverything()

points = hero.play()