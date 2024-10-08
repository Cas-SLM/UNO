from random import shuffle

from player import Player
from cards import Card


def show_deck(deck: list[Card], name : str = "Deck"):
    i = 1
    print(f"{name}:")
    for card in deck:
        print(f"    {i}: " + card.__str__())
        i += 1

class Game:
    discard = []
    draw = []
    deck = []
    players = []
    direction = 1
    current_player = Player
    winner = Player

    def __init__(self, deck : list[Card], *players : Player):
       self.deck = deck
       self.players = list(players)
       prev_index = len(players) - 1
       next_index = 1
       for current in self.players:
           current.set_next_player(self.players[next_index])
           if next_index == len(self.players) - 1:
               next_index = 0
           else:
                next_index += 1
           current.set_previous_player(self.players[prev_index])
           if prev_index == len(players) - 1:
               prev_index = 0
           else:
               prev_index += 1
       self.deal()

    def deal(self):
        shuffle(self.deck)
        for player in self.players:
            [ player.add(self.deck.pop()) for i in range(7) ]
            player.show_hand()
        card = self.deck.pop()
        while card.get_card_type() != "NUMBER":
            self.draw.append(card)
            card = self.deck.pop()
        self.discard.append(card)
        while len(self.deck) > 0:
            self.draw.append(self.deck.pop())
        # self.top_card()

    def draw_card(self, player):
        player.add(self.draw.pop())
        player.show_hand()
        if len(self.draw) < 5:
            temp_deck = self.discard[:len(self.discard) - 2]
            shuffle(temp_deck)
            self.draw = temp_deck + self.draw

    def top_card(self):
        print(f"Current card: {self.discard[len(self.discard)-1]}")

    def discard_card(self, player : Player, index : int):
        self.discard.append(player.discard(index))
        player.show_hand()

    def start_game(self):
        self.current_player = self.players[len(self.players) - 1]
        while True:
            self.current_player = self.get_turn_player()
            if self.set_winner():
                print(f"{self.winner} won the game!")
                break
            print(f"{self.current_player}'s turn")
            self.top_card()
            self.play()



    def set_winner(self):
        for player in self.players:
            if any([p.won() for p in self.players]) and not player.won():
                player.lost_game()
            elif player.won():
                self.winner = player
                return True

        return any([p.won() for p in self.players])

    def play(self):
        while True:
            print("Play options:\n    0: Draw card")
            index = 1
            current_hand = self.current_player.get_hand()
            for card in current_hand:
                print(f"    {index}: {card}")
                index += 1
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    self.draw_card(self.current_player)
                    break
                elif 0 < choice < len(current_hand):
                    self.discard_card(self.current_player, choice - 1)
                    break
                else:
                    raise AssertionError
            except ValueError:
                print("Invalid choice")
            except AssertionError or IndexError:
                print("That's not a in the list of cards")
                self.show_hand()


    def get_turn_player(self):
        return self.current_player.get_previous_player() if self.direction == -1 else self.current_player.get_next_player()


