######################
## Simple Coin list ##
######################

from pathlib import Path
import json


def show_list(coin_list):
    """Displaying the list with numbering."""
    
    print()
    print("*" * 19)
    print("***$ Coin list $***")
    print("*" * 19)
    for i, coin in enumerate(coin_list, start=1):
        print(f"{i}. {coin.title()}")

def add_coin(coin_list):
    """Add new coin to the list."""

    coin = input("\nNew Coin: ").lower()

    if coin == '':
        print("\nEmpty input, Enter a Coin name!")

    elif coin in coin_list:
        print(f"\n{coin.title()} already exists in your Coin list!")
        print("Check your Coin list.")

    else:
        coin_list.append(coin)
        print("\nNew Coin is added to your list!")

def remove_coin(coin_list):
    """Remove coin via input"""
    
    show_list(coin_list)
    try:
        numb = int(input("\nEnter Number do you want to remove: "))
        index = numb -1

        if 0 <= index < len(coin_list):
            removed = coin_list.pop(index)
            print(f"\n{removed.title()} has been removed from the Coin list.")

        else:
            print("\nThis number does not exist in the Coin list.")

    except ValueError:
        print("\nPlease enter a number.")

def save_coin(coin_list):
    """Save Coin list"""

    path = Path('coin_list.json')

    content = json.dumps(coin_list)
    path.write_text(content)
    print("\nCoin list saved.")

def load_coin():
    """Load Coin list"""

    path = Path('coin_list.json')

    try:
        content = path.read_text()
        coins = json.loads(content)
    
    except FileNotFoundError:
        print("\nNo saved list found - starting new list.")
        return []
    
    else:
        return coins

coins = load_coin()

while True:
 
    print()
    print("*" * 20)
    print("******* Menu *******")
    print("*" * 20)
    print(" 1 - Show list")
    print(" 2 - Add Coin")
    print(" 3 - Remove Coin")
    print(" 4 - Save Coin list")
    print(" 5 - Load Coin list")
    print(" 6 - Ended")

    choice = input("\nEnter choice: ")

    if choice == '1':
        show_list(coins)

    elif choice == '2':
        add_coin(coins)

    elif choice == '3':
        remove_coin(coins)

    elif choice == '4':
        save_coin(coins)

    elif choice == '5':
        coins = load_coin()
        print("\nCoin list loaded.")

    elif choice == '6':
        print("\nProgram ended")
        break

    else:
        print("\nIncorrect entry!")
                   