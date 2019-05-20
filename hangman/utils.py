#################################
##### Utilities for Hangman #####
#####    by Chris Pyles     #####
#################################

def repeat(x, n):
	"""
	Returns a list of `x` repeated `n` times.

	Args:
		x - object to repeat
		n - number of repetitions
	"""
	return [x for _ in range(n)]



# Board Status Strings

board_0 = """
      _________
      |       |
      |       
      |       
      |       
      |       
      |       
_____________
"""

board_1 = """
      _________
      |       |
      |       O
      |       
      |       
      |       
      |       
_____________
"""

board_2 = """
      _________
      |       |
      |       O
      |       |
      |       |
      |       
      |       
_____________
"""

board_3 = """
      _________
      |       |
      |       O
      |      /|
      |       |
      |       
      |       
_____________
"""

board_4 = """
      _________
      |       |
      |       O
      |      /|\
      |       |
      |       
      |       
_____________
"""

board_5 = """
      _________
      |       |
      |       O
      |      /|\
      |       |
      |      /
      |       
_____________
"""

board_6 = """
      _________
      |       |
      |       O
      |      /|\
      |       |
      |      / \
      |       
_____________
"""


   

boards = {
	0 : board_0,
	1 : board_1,
	2 : board_2,
	3 : board_3,
	4 : board_4,
	5 : board_5,
	6 : board_6
}