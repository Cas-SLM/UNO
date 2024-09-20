import unittest
from cards import *

class TestCardDeck(unittest.TestCase):

    def test_get_number_cards(self):
        cards = get_number_cards()
        self.assertEqual(len(cards), 76)  # There are 19 cards per color (0 once and 1-9 twice) and 4 colors
        for card in cards:
            self.assertIn(card._color, colors[:-1])  # Excluding "ALL"
            self.assertGreaterEqual(card._number, 0)
            self.assertLessEqual(card._number, 9)
            self.assertEqual(card._card_type, "NUMBER")

    def test_get_draw2_cards(self):
        cards = get_draw2_cards()
        self.assertEqual(len(cards), 8)  # 2 cards per color and 4 colors (excluding "ALL")
        for card in cards:
            self.assertIn(card._color, colors[:-1])  # Excluding "ALL"
            self.assertEqual(card._number, 2)
            self.assertEqual(card._card_type, "DRAW")

    def test_get_reverse_cards(self):
        cards = get_reverse_cards()
        self.assertEqual(len(cards), 8)  # 2 cards per color and 4 colors (excluding "ALL")
        for card in cards:
            self.assertIn(card._color, colors[:-1])  # Excluding "ALL"
            self.assertEqual(card._number, -1)
            self.assertEqual(card._card_type, "REVERSE")

    def test_get_skip_cards(self):
        cards = get_skip_cards()
        self.assertEqual(len(cards), 8)  # 2 cards per color and 4 colors (excluding "ALL")
        for card in cards:
            self.assertIn(card._color, colors[:-1])  # Excluding "ALL"
            self.assertEqual(card._number, 1)
            self.assertEqual(card._card_type, "SKIP")

    def test_get_wild_cards(self):
        cards = get_wild_cards()
        self.assertEqual(len(cards), 4)  # 4 wild cards
        for card in cards:
            self.assertEqual(card._color, "ALL")
            self.assertEqual(card._number, 0)
            self.assertEqual(card._card_type, "WILD")

    def test_get_wild_draw_cards(self):
        cards = get_wild_draw_cards()
        self.assertEqual(len(cards), 4)  # 4 wild draw cards
        for card in cards:
            self.assertEqual(card._color, "ALL")
            self.assertEqual(card._number, 4)
            self.assertEqual(card._card_type, "WILD DRAW")

    def test_get_deck(self):
        deck = get_deck()
        self.assertEqual(len(deck), 108)  # Total cards in the deck

        # Count the number of each card type in the deck
        number_cards = [card for card in deck if card._card_type == "NUMBER"]
        draw_cards = [card for card in deck if card._card_type == "DRAW"]
        reverse_cards = [card for card in deck if card._card_type == "REVERSE"]
        skip_cards = [card for card in deck if card._card_type == "SKIP"]
        wild_cards = [card for card in deck if card._card_type == "WILD"]
        wild_draw_cards = [card for card in deck if card._card_type == "WILD DRAW"]

        self.assertEqual(len(number_cards), 76)
        self.assertEqual(len(draw_cards), 8)
        self.assertEqual(len(reverse_cards), 8)
        self.assertEqual(len(skip_cards), 8)
        self.assertEqual(len(wild_cards), 4)
        self.assertEqual(len(wild_draw_cards), 4)


if __name__ == '__main__':
    unittest.main()
