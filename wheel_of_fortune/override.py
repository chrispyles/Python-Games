from secret import *
from wheel import *
from board import *
from player import *
from utils import *

class Override:
	def __init__(self, board, current_player):
		self.board = board

		print('\n\nENTER PASSWORD:')
		password = input()
		assert password == 'wheel', 'Incorrect Password. Game Resumed.'
		
		print('\n\nOVERRIDE TYPE:')
		self.type = input()

		if self.type == 'ENDGAME':
			print('\n\nENDING GAME')
			phrase = self.board.secret.phrase
			print(f'\n\nThe phrase was:\n{phrase}')
			print('\n\nGAME ENDED')
			exit()

		elif self.type == 'SETSCORE':
			print('\n\nPLAYER:')
			player = input()
			for p in self.board.players:
				if p.name == player:
					score_set_player = p
			print(f'\n\nCurrent Score: {score_set_player.score}')
			print('\n\nSet score to:')
			new_score = int(input())
			score_set_player.score = new_score

		self.board.get_letter(current_player)