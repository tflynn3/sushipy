from deck import Deck
from player import Player
from card import Card, CardType


class Round:
    def __init__(self, deck, players) -> None:
        self.deck = deck
        self.players = players
        self.deal()

    def play(self):
        while len(self.players[0].hand) > 0:
            for i, player in enumerate(self.players):
                print(f'Player {i} making selection')
                player.make_selection()

            # store last hand before replaced by the passed hand
            temp_hand = self.players[-1].hand

            # pass hand
            for i in range(1, len(self.players)):
                self.players[i].hand = self.players[i-1].hand

            # set first hand as last hand
            self.players[0].hand = temp_hand

    def simulate_play(self):
        while len(self.players[0].hand) > 0:
            for i, player in enumerate(self.players):
                player.random_selection()

            # store last hand before replaced by the passed hand
            temp_hand = self.players[-1].hand

            # pass hand
            for i in range(1, len(self.players)):
                self.players[i].hand = self.players[i-1].hand

            # set first hand as last hand
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

    def start(self):
        self.round1 = Round(self.deck, self.players)
        self.round1.play()
        self.score_round()
        self.reset_player_hands()

        self.round2 = Round(self.round1.deck, self.players)
        self.round2.play()
        self.score_round()
        self.reset_player_hands()

        self.round3 = Round(self.round2.deck, self.players)
        self.round3.play()
        self.score_round()
        self.score_final()

    def simulate(self, print_rounds=False):
        self.round1 = Round(self.deck, self.players)
        self.round1.simulate_play()
        self.score_round()

        if print_rounds:
            print('-'*100)
            print('Round 1')
            print('-'*100)
            for i, player in enumerate(self.players):
                print(f'Player {i+1} Played Hand\n{player.played_cards}')
                print(f'Player {i+1} Score: {player.score}')
            print('-'*100)

        self.reset_player_hands()

        self.round2 = Round(self.round1.deck, self.players)
        self.round2.simulate_play()
        self.score_round()
        if print_rounds:
            print('-'*100)
            print('Round 2')
            print('-'*100)
            for i, player in enumerate(self.players):
                print(f'Player {i+1} Played Hand\n{player.played_cards}')
                print(f'Player {i+1} Score: {player.score}')
            print('-'*100)
        self.reset_player_hands()

        self.round3 = Round(self.round2.deck, self.players)
        self.round3.simulate_play()
        self.score_round()
        if print_rounds:
            print('-'*100)
            print('Round 3')
            print('-'*100)
            for i, player in enumerate(self.players):
                print(f'Player {i+1} Played Hand\n{player.played_cards}')
                print(f'Player {i+1} Score: {player.score}')
            print('-'*100)
        
        self.score_final()
        if print_rounds:
            print('-'*100)
            print('Final Score')
            print('-'*100)
            for i, player in enumerate(self.players):
                print(f'Player {i+1} Number of Puddings: {player.puddings}')
                print(f'Player {i+1} Final Score: {player.score}')
            print('-'*100)

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
                                    del played_card_types[j + i]
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
                            self.players[player_i].score += int(3/number_players_tied)
            else:
                players_tied = [i for i, x in enumerate(maki_scores) if x == max_score]
                number_players_tied = len(players_tied)
                for player_i in players_tied:
                    self.players[player_i].score += int(6/number_players_tied)        
        
    def score_final(self):
        # Score most puddings
        puddings_scores = [p.puddings for p in self.players]
        max_score = max(puddings_scores)
        # check if there were any puddings scored
        if max_score > 0:
            number_tied = puddings_scores.count(max_score)
            if number_tied == 1:
                # 1st place
                player_i = puddings_scores.index(max_score)
                del puddings_scores[player_i]
                self.players[player_i].score += 6
            else:
                players_tied = [i for i, x in enumerate(puddings_scores) if x == max_score]
                number_players_tied = len(players_tied)
                for player_i in players_tied:
                    self.players[player_i].score += int(6/number_players_tied) 

        # Score least puddings
        puddings_scores = [p.puddings for p in self.players]
        min_score = min(puddings_scores)
        # check if there were any puddings scored
        if min_score > 0:
            number_tied = puddings_scores.count(min_score)
            if number_tied == 1:
                # 1st place
                player_i = puddings_scores.index(min_score)
                del puddings_scores[player_i]
                self.players[player_i].score -= 6
            else:
                players_tied = [i for i, x in enumerate(puddings_scores) if x == min_score]
                number_players_tied = len(players_tied)
                for player_i in players_tied:
                    self.players[player_i].score -= int(6/number_players_tied)     


g = Game(n_players=2)
g.simulate(print_rounds=True)