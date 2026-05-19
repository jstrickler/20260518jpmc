class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, value):
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("rank must be a str")
        
    @property # DECORATOR
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError("suit must be a str")

    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"PlayingCard('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = PlayingCard('8', 'Diamonds')
    c2 = PlayingCard('A', 'Clubs')
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")

    print(c1)   # str()  human-friendly
    print(f"{c1 = }")  # repr()  code to reproduce object
    print(f"{c1 = !s}")  # force str()