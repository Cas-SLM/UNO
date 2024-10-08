from __future__ import annotations

from cards import Card

class Player:
    _player_type = str
    _player_name = str
    _hand = []
    _status = str
    _next = None
    _previous = None

    def __init__(self, player_type : str, name : str, hand : list[Card] = None):
        self._player_type = player_type
        self._player_name = name
        self._hand = hand if hand else []
        self._status = "ENGAGED"
        self._next = None
        self._previous = None

    def __str__(self):
        if self._player_type == "COMPUTER":
            return f"{self._player_type} - {self._player_name}"
        else:
            return f"{self._player_name}"

    def __repr__(self):
        if self._player_type == "COMPUTER":
            return f"Player: {self._player_type} - {self._player_name}"
        else:
            return f"Player: {self._player_name}"

    def discard(self, card_index : int) :
        """
        Returns the card the player chooses to play.
        :param card_index: index of the card to play
        :return: card that will be played
        :raises IndexError: if card_index is out of range
        """
        self.show_hand()
        return self._hand.pop(card_index)
        # while True:
        #     try:
        #         index = int(input("Which card do you want to play?"))
        #         if 0 < index <= len(self._hand):
        #             return self._hand.pop(index - 1)
        #         else:
        #             raise AssertionError("Not enough cards for that number!")
        #     except ValueError:
        #         print("That's not a number!")
        #     except AssertionError or IndexError:
        #         print("That's not a in the list of cards")
        #         self.show_hand()

    def show_hand(self):
        print(f"{self}'s cards:")
        index = 1
        for card in self._hand:
            print(f"    {index}. {card}")
            index += 1

    def get_hand(self):
        return self._hand.copy()

    def add(self, *cards : Card):
        for card in cards:
            self._hand.append(card)

    def won(self):
        return self._status == "WON"

    def won_game(self):
        self._status = "WON"

    def set_next_player(self, player : Player):
        self._next = player

    def get_next_player(self):
        return self._next

    def set_previous_player(self, player : Player):
        self._previous = player

    def get_previous_player(self):
        return self._previous

    def lost_game(self):
        self._status = "LOST"