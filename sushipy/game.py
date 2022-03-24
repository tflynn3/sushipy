from deck import Deck
from player import Player

class Scorer:
    pass

class Round:
    def __init__(self, deck, players) -> None:
        self.deck = deck
        self.players = players
        self.deal()

    def play(self):
        while len(self.players[0].hand) > 1:
            for i, player in enumerate(self.players):
                print(f'Player {i} making selection')
                player.make_selection()

            print("Passing Decks...")
            # store last hand before replaced by the passed hand
            temp_hand = self.players[-1].hand

            # pass hand
            for i in range(1, len(self.players)):
                print(f"Setting {i} players deck")
                self.players[i].hand = self.players[i-1].hand

            # set first hand as last hand
            print("Setting first player deck...")
            self.players[0].hand = temp_hand
    
    def deal(self):
        # Number of cards changes based on number of players
        if len(self.players) == 2:
            for player in self.players:
                player.draw(self.deck, 10)
        elif len(self.players) == 3:
            for player in self.players:
                player.draw(self.deck, 9)
        elif len(self.players) == 4:
            for player in self.players:
                player.draw(self.deck, 8)
        elif len(self.players) == 5:
            for player in self.players:
                player.draw(self.deck, 7)

class Game:
    def __init__(self, n_players) -> None:

        # Prep the deck
        self.deck = Deck()
        self.deck.shuffle()

        # Set number of players
        self.players = list(Player()*n_players)

        self.round1 = Round(self.deck, self.players)
        self.round1.play()


g = Game(2)

print(g.round1.players[0].played_cards)
    
