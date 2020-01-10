import numpy as np

class Card:
    def __init__(self, num, suit):
        self._num = num
        self._suit = suit

    def num(self):
        return self._num
    
    def suit(self):
        return self._suit

    def color(self):
        if self._suit in ["H", "D"]:
            return "red"
        else:
            return "black"

class Deck:
    cards = {
        str(num) + suit : Card(num, suit) for suit in ["S", "C", "H", "D"] for num in list(np.arange(1, 11)) + ["J", "Q", "K"]
    }

    def __init__(self):
        self._deal = [[] for _ in range(7)]
        shuffle = np.random.shuffle(Deck.cards.keys())
        shuffle_idx = 0
        for i in np.arange(7):
            for _ in np.arange(i):
                self._deal[i] += [Deck.cards[shuffle[shuffle_idx]]]
                shuffle_idx += 1
            self._deal[i] += [None for _ in np.arange(6-i)]
        self._deck = shuffle[shuffle_idx:]

    def check_valid(self, card, placement):
        card = Deck.cards[card]
        placement = Deck.cards[placement]
        return abs(card.num() - placement.num()) == 1 and placement.color() != card.color()
    
    def deal(self):
        return self._deal
    
    def deck(self):
        return self._deck
