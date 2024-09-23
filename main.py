from cards import get_deck
from game import Game
from player import Player


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deck = get_deck()

    player1 = Player("HUMAN", "HAL")
    player3 = Player("HUMAN", "Alice")
    player2 = Player("COMPUTER", "AI_01")
    player4 = Player("COMPUTER", "AI_02")
    print(f"Player1: {player1}", f"\nPlayer2: {player2}", f"\nPlayer3: {player3}", f"\nPlayer4: {player4}")

    game = Game(deck, player1, player2, player3, player4)
    game.start_game()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
