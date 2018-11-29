from player import *
from sudoku import *

print('\nPlease enter your name.')
name = input()
print('\nPlease enter the game number.')
num = input()

file = 'puzzle_' + num + '.txt'

s = Sudoku(file)
p = Player(name, s)
p.get_pick()