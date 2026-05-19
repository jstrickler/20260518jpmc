import random
from playingcard import PlayingCard

class CardDeck:
    # class data
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()


    def __init__(self):  # constructor/initializer
        self._make_deck()

    def _make_deck(self):
        self._cards = []   # storage for cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards
    
    def __len__(self):   # used for len(obj)
        return len(self._cards)
    
    def __repr__(self):
        return f"{type(self).__name__}()"

    def __str__(self):
        return f"{type(self).__name__}/{len(self)}"
    
    def __add__(self, other):  # implement self + other
        new_deck = type(self)()  # create a new instance of the current type
        new_deck._cards = self._cards + other._cards
        return new_deck

    
    @classmethod
    def get_ranks(cls):
        return cls.RANKS

if __name__ == "__main__":
    d1 = CardDeck()
    d1.shuffle()
    print(f"{d1 = !s}")
    print(f"{d1.cards = }")
    for _ in range(5):
        card = d1.draw()
        print(card)
    
    print(f"{len(d1) = }")
    print(f"{d1 = !s}")  # str()
    print(f"{d1 = }")    # repr()
    
    print(f"{CardDeck.get_ranks() = }")
    print(f"{d1.get_ranks() = }")
    d2 = CardDeck()

    d3 = d1 + d2
    print(d3)
    
    