from lib.board import Board
from lib.hero import Hero

board = Board(4);

hero = Hero(board, 0,0)

hero.move('right');
print(hero.xCoord,", ", hero.yCoord)