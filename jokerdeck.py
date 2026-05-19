from playingcard import PlayingCard
from carddeck import CardDeck

# from module_one import thing
# from module_two import thing

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            card = PlayingCard(f"JOKER{joker_number}", "*** JOKER ***")
            self._cards.append(card)

if __name__ == "__main__":
    j1 = JokerDeck()
    j1.shuffle()
    print(j1)
    print(j1.cards)