from board import *
from categories import *
from questions import *

print('Please enter the game number.')
game_num = input()

print('\n\nPlease enter your name.')
name = input()

cats = 'categories_' + game_num + '.txt'
qs = 'qs_' + game_num + '.txt'
ans = 'an_' + game_num + '.txt'

c = Categories(cats)
q = Questions(qs, ans, c)
b = Board(c, q)
p = Player(name, b)

for _ in range(30):
	p.choose_question()

print(f'Your end score is ${p.score}')