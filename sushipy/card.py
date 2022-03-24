from enum import Enum

class CardType(Enum):
    TEMPURA = 1
    SASHIMI = 2
    DUMPLING = 3
    MAKI_1 = 4
    MAKI_2 = 5
    MAKI_3 = 6
    EGG_NIGIRI = 7
    SALMON_NIGIRI = 8
    SQUID_NIGIRI = 9
    PUDDING = 10
    WASABI = 11
    CHOPSTICKS = 12

    def __str__(self):
        return self.name.replace('_', ' ').title()

    def __repr__(self) -> str:
        return self.name.replace('_', ' ').title()

class Card:
    def __init__(self, card_type: CardType):
        self.card_type = card_type



    def __mul__(self, other):
        return [Card(self.card_type) for i in range(other)]




# print(Card(CardType(1)))