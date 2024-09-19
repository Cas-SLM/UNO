from cards import Card

class Player:
    player_type = str
    player_name = str
    hand = []

    def __init__(self, player_type : str, name : str):
        self.player_type = player_type.upper()
        self.player_name = name
        self.hand = []

    def __init__(self, player_type, name, hand):
        self.player_type = player_type
        self.player_name = name
        self.hand = hand

    def discard(self, card):
        return self.hand.pop(self.hand.index(card))

    def add(self, *cards : Card):
        for card in cards:
            self.hand.append(card)

    def __str__(self):
        if self.player_type == "COMPUTER":
            return self.player_type
        else:
            return f"{self.player_name}"