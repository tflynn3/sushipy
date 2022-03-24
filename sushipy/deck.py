import random
from card import Card,CardType

class Deck:

    def __init__(self) -> None:
        self.cards = []
        self.build()
    

    def build(self):
        if len(self.cards) == 0:
            self.cards += Card(CardType.TEMPURA)*14
            self.cards += Card(CardType.SASHIMI)*14
            self.cards += Card(CardType.DUMPLING)*14
            self.cards += Card(CardType.MAKI_1)*6
            self.cards += Card(CardType.MAKI_2)*12
            self.cards += Card(CardType.MAKI_3)*8
            self.cards += Card(CardType.EGG_NIGIRI)*5
            self.cards += Card(CardType.SALMON_NIGIRI)*10
            self.cards += Card(CardType.SQUID_NIGIRI)*5
            self.cards += Card(CardType.PUDDING)*10
            self.cards += Card(CardType.WASABI)*6
            self.cards += Card(CardType.CHOPSTICKS)*4
            return self.cards

    def describe(self):
        card_types = list(map(lambda s: s.card_type, self.cards))
        return '\n'.join([str(x) + ' x' + str(card_types.count(x)) for x in [c for c in set(card_types)]])

    def __str__(self):
        return str(list(map(lambda s: str(s.card_type), self.cards)))

    # Shuffle the deck
    def shuffle(self, num=1):
        random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()


# my_deck = Deck()
# my_deck.shuffle()
# print(my_deck)