from board import *
from categories import *
from questions import *

print('Please enter the game number.')
game_num = input()

print('\n\nHow many players?')
players = int(input())

names = []
for i in range(players):
	print(f"\n\nPlease enter Player {i+1}'s name.")
	names += [input()]

cats = 'categories_' + game_num + '.txt'
qs = 'qs_' + game_num + '.txt'
ans = 'an_' + game_num + '.txt'

c = Categories(cats)
q = Questions(qs, ans, c)
b = Board(c, q)
p = Player(name, b)

while not b.is_done():
	p.choose_question()

print(f'Your end score is ${p.score}')