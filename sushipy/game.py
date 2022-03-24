from numpy import number
from deck import Deck
from player import Player
from card import Card, CardType


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

        # Start game
        #self.start()

    def start(self):
        self.round1 = Round(self.deck, self.players)
        self.round1.play()
        self.score_round(self.players)
        # self.reset_player_hands()

        # self.round2 = Round(self.round1.deck, self.players)
        # self.round2.play()
        # self.score_round(self.players)
        # self.reset_player_hands()

        # self.round3 = Round(self.round2.deck, self.players)
        # self.round3.play()
        # self.score_round(self.players)
        #self.score_final(self.players)

    def reset_player_hands(self):
        for player in self.players:
            player.maki = 0
            player.played_cards = []

    def score_round(self):
        # Score cards independently
        for player in self.players:

            # Get played cards types
            played_card_types = list(map(lambda s: s.card_type, player.played_cards))

            # Score Tempura
            player.score += int(played_card_types.count(CardType.TEMPURA)/2) * 5

            # Score Sashimi
            player.score += int(played_card_types.count(CardType.SASHIMI)/3) * 10

            # Score Dumplings
            if played_card_types.count(CardType.DUMPLING) == 1:
                player.score += 1
            elif played_card_types.count(CardType.DUMPLING) == 2:
                player.score += 3
            elif played_card_types.count(CardType.DUMPLING) == 3:
                player.score += 6
            elif played_card_types.count(CardType.DUMPLING) == 4:
                player.score += 10
            elif played_card_types.count(CardType.DUMPLING) >= 5:
                player.score += 15

            # Score Egg Nigiri
            player.score += played_card_types.count(CardType.EGG_NIGIRI)

            # Score Salmon Nigiri
            player.score += played_card_types.count(CardType.SALMON_NIGIRI) * 2

            # Score Squid Nigiri
            player.score += played_card_types.count(CardType.SQUID_NIGIRI) * 3

            # Score Wasabi
            while CardType.WASABI in played_card_types:

                # Loop through all cards
                for j, c in enumerate(played_card_types):
                    
                    # check if card is wasabi and not the last played card
                    if c == CardType.WASABI and j != len(played_card_types):
                        # Get the cards played after the wasabi
                        remaining_cards = played_card_types[j + 1:]
                        if CardType.EGG_NIGIRI in remaining_cards or CardType.SALMON_NIGIRI in remaining_cards or CardType.SQUID_NIGIRI in remaining_cards:
                            for i, card in enumerate(remaining_cards):
                                # add remaining points from wasabi combo
                                if card == CardType.EGG_NIGIRI:
                                    player.score += 2
                                    del played_card_types[j]
                                    del played_card_types[j + i]
                                    break
                                elif card == CardType.SALMON_NIGIRI:
                                    player.score += 4
                                    del played_card_types[j]
                                    del played_card_types[j + i]
                                    break
                                elif card == CardType.SQUID_NIGIRI:
                                    player.score += 6
                                    del played_card_types[j]
                                    del played_card_types[j + i + 1]
                                    break
                        else:
                            del played_card_types[j]

            # Score Maki 1
            player.maki += played_card_types.count(CardType.MAKI_1)

            # Score Maki 2
            player.maki += played_card_types.count(CardType.MAKI_2) * 2

            # Score Maki 3
            player.maki += played_card_types.count(CardType.MAKI_3) * 3

            # Score Puddings
            player.puddings += played_card_types.count(CardType.PUDDING)
        
        # Score Maki
        maki_scores = [p.maki for p in self.players]
        max_score = max(maki_scores)
        # check if there were any maki scored
        if max_score > 0:
            number_tied = maki_scores.count(max_score)
            if number_tied == 1:
                # 1st place
                player_i = maki_scores.index(max_score)
                del maki_scores[player_i]
                self.players[player_i].score += 6
                # 2nd place
                max_score = max(maki_scores)
                # check if there were any maki scored
                if max_score > 0:
                    number_tied = maki_scores.count(max_score)
                    if number_tied == 1:
                        player_i = maki_scores.index(max_score)
                        self.players[player_i].score += 3
                    else:
                        players_tied = [i for i, x in enumerate(maki_scores) if x == max_score]
                        number_players_tied = len(players_tied)
                        for player_i in players_tied:
                            self.players[player_i] += int(3/number_players_tied)
            else:
                players_tied = [i for i, x in enumerate(maki_scores) if x == max_score]
                number_players_tied = len(players_tied)
                for player_i in players_tied:
                    self.players[player_i] += int(6/number_players_tied)        
        



    def score_final(self):
        pass


g = Game(2)
g.players[0].played_cards = [Card(CardType.WASABI), Card(CardType.WASABI), Card(CardType.SALMON_NIGIRI), Card(CardType.WASABI), Card(CardType.SALMON_NIGIRI), Card(CardType.MAKI_1)]
g.players[1].played_cards = [Card(CardType.MAKI_3), Card(CardType.MAKI_3), Card(CardType.SASHIMI), Card(CardType.SASHIMI), Card(CardType.TEMPURA), Card(CardType.TEMPURA)]
g.score_round()
print(g.players[0].score)
print(g.players[1].score)