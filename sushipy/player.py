import enum


class Player(object):
    def __init__(self) -> None:
        self.hand = []
        self.played_cards = []
        self.score = 0
        self.puddings = 0

    def __mul__(self, other):
        return [Player() for _ in range(other)]

    def draw(self, deck, count=1):
        for _ in range(count):
            card = deck.deal()
            self.hand.append(card)

    # Score hand
    def scoreHand(self):
        pass

    def select_card(self, card):
        self.played_cards.append(card)

    def make_selection(self):
        poss_selections = []
        for i, card in enumerate(self.hand):
            poss_selections.append(i)
            print(f'[{i}] {card}')
        
        selection = -1
        while selection not in poss_selections:
            selection = int(input("Select a card: "))

        self.select_card(self.hand[selection])
        del self.hand[selection]
        


# print(len(Player()*2))