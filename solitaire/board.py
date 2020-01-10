from .deck import Deck

class Board:
    def __init__(self):
        self._deck = Deck()
        self._board_secret = self._deck.deal()
        self._board = []
        for col in self._board_secret:
            self._board += [[col[i] if]]
