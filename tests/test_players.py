import unittest
from player import Player
from cards import Card

class TestPlayer(unittest.TestCase):

    def setUp(self):
        # Create some card objects for testing
        self.card1 = Card("RED", 5, "NUMBER")
        self.card2 = Card("BLUE", 2, "DRAW")
        self.card3 = Card("ALL", 0, "WILD")

        # Create player objects for testing
        self.player1 = Player("HUMAN", "Alice")
        self.player2 = Player("COMPUTER", "AI_01")

    def test_player_initialization(self):
        self.assertEqual(self.player1._player_name, "Alice")
        self.assertEqual(self.player1._player_type, "HUMAN")
        self.assertEqual(self.player1._status, "ENGAGED")
        self.assertEqual(len(self.player1._hand), 0)

        self.assertEqual(self.player2._player_name, "AI_01")
        self.assertEqual(self.player2._player_type, "COMPUTER")
        self.assertEqual(self.player2._status, "ENGAGED")
        self.assertEqual(len(self.player2._hand), 0)

    def test_add_card_to_hand(self):
        self.player1.add(self.card1)
        self.assertIn(self.card1, self.player1._hand)
        self.assertEqual(len(self.player1._hand), 1)

        self.player1.add(self.card2, self.card3)  # Add multiple cards
        self.assertEqual(len(self.player1._hand), 3)

    def test_discard_card(self):
        self.player1.add(self.card1, self.card2)
        discarded_card = self.player1._hand.pop(0)  # Simulate discard
        self.assertNotIn(discarded_card, self.player1._hand)

    def test_show_hand(self):
        self.player1.add(self.card1, self.card2)
        self.assertEqual(len(self.player1._hand), 2)
        self.player1.show_hand()  # Should print the hand without error

    def test_next_previous_player(self):
        # Test next player setting and retrieval
        self.player1.set_next_player(self.player2)
        self.assertEqual(self.player1.get_next_player(), self.player2)

        # Test previous player setting and retrieval
        self.player2.set_previous_player(self.player1)
        self.assertEqual(self.player2.get_previous_player(), self.player1)

    def test_won_game(self):
        self.player1.won_game()
        self.assertTrue(self.player1.won())
        self.assertEqual(self.player1._status, "WON")

    def test_lost_game(self):
        self.player2.lost_game()
        self.assertEqual(self.player2._status, "LOST")

if __name__ == "__main__":
    unittest.main()
