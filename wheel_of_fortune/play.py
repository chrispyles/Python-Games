from board import *
from wheel import *
from secret import *
from player import *

print('\n\nHow many people are playing?')

num_players = ''

while type(num_players) != int:
	try:
		num_players = int(input())
	except ValueError:
		print('\n\nPlease enter a number.')

w = Wheel()

players = []
for i in range(num_players):
	print(f"\n\nWhat is Player {i+1}'s name?")
	name = input()
	players += [Player(name, w)]

phrase = generate_secret_phrase()
s = SecretPhrase(phrase[0], phrase[1])

b = Board(s, players)

s.assign_board(b)

while not b.secret.is_done():
	for p in b.players:
		try:
			b.get_letter(p)
		except AssertionError as e:
			print(f'\n\n{e}')
			#b.get_letter(p)


final_scores = {}
for p in players:
	final_scores[p.name] = p.score

print(f'\n\n{b.secret.show_status()}')

print('\n\nFinal Scores:')

for p in final_scores:
	print(f'{p}: {final_scores[p]}')

winner = key_of_max(final_scores)
print(f'\n\nThe winner is............{winner}!')