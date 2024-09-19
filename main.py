from cards import get_deck
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
    i = 1
    for card in deck:
        print(f"{i}: " + card.__str__())
        i += 1

    player1 = Player("HUMAN", "HAL")
    player2 = Player("COMPUTER", "HAL")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
