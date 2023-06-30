from prettytable import PrettyTable

players = {}


def add_player():
    while True:
        choice = input("Do you want to add a player? (Y/N): ")
        if choice.upper() == 'Y':
            player_name = input("Enter the player's name: ")
            players[player_name] = 15000
        elif choice.upper() == 'N':
            break
        else:
            print("Invalid input! Please enter Y or N.")


def display_players():
    table = PrettyTable()
    table.field_names = ["Player", "Balance"]
    for player, balance in players.items():
        table.add_row([player, balance])
    print(table)


def banker_machine():
    print("Welcome to the Monopoly Banker's Machine!")
    add_player()

    while True:
        action = input("What would you like to do? (enter 'D' for deposit, 'W' for withdrawal, 'T' for transfer, "
                       "'Q' to quit, 'P' to display table): ")

        if action.upper() == 'Q':
            print("Thank you for using the Monopoly Banker's Machine. Goodbye!")
            break

        elif action.upper() == 'D':
            player_name = input("Enter the player's name: ")
            amount = int(input("Enter the amount to deposit: "))

            if player_name in players:
                players[player_name] += amount
            else:
                players[player_name] = amount

            print(f"Deposited ${amount} successfully for {player_name}. Current balance: ${players[player_name]}.")

        elif action.upper() == 'W':
            player_name = input("Enter the player's name: ")
            amount = int(input("Enter the amount to withdraw: "))

            if player_name in players:
                if amount > players[player_name]:
                    print("Insufficient funds! Withdrawal unsuccessful.")
                else:
                    players[player_name] -= amount
                    print(
                        f"Withdrew ${amount} successfully for {player_name}. Current balance: ${players[player_name]}.")

            else:
                print(f"Player {player_name} does not exist!")

        elif action.upper() == 'T':
            sender_name = input("Enter the sender's name: ")
            receiver_name = input("Enter the receiver's name: ")
            amount = int(input("Enter the amount to transfer: "))

            if sender_name in players and receiver_name in players:
                if amount > players[sender_name]:
                    print("Insufficient funds! Transfer unsuccessful.")
                else:
                    players[sender_name] -= amount
                    players[receiver_name] += amount
                    print(f"Transferred ${amount} from {sender_name} to {receiver_name}.")

            else:
                print("One or both players do not exist!")

        elif action.upper() == 'P':
            display_players()
            continue

        else:
            print("Invalid input! Please try again.")

        display_players()


banker_machine()
