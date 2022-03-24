import random
from card import Card,CardType

class Deck:

    def __init__(self) -> None:
        self.cards = []
        self.build()
    

    def build(self):
        if len(self.cards) == 0:
            
            # 14x Tempura
            # 14x Sashimi
            # 14x Dumpling
            # 6x 1 Maki roll
            # 12x 2 Maki rolls
            # 8x 3 Maki rolls
            # 5x Egg Nigiri
            # 10x Salmon Nigiri
            # 5x Squid Nigiri
            # 10x Pudding
            # 6x Wasabi
            # 4x Chopsticks
            self.cards += Card(CardType(1))*14
            self.cards += Card(CardType(2))*14
            self.cards += Card(CardType(3))*14
            self.cards += Card(CardType(4))*6
            self.cards += Card(CardType(5))*12
            self.cards += Card(CardType(6))*8
            self.cards += Card(CardType(7))*5
            self.cards += Card(CardType(8))*10
            self.cards += Card(CardType(9))*5
            self.cards += Card(CardType(10))*10
            self.cards += Card(CardType(11))*6
            self.cards += Card(CardType(12))*4
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

my_deck = Deck()
my_deck.shuffle()
print(my_deck)