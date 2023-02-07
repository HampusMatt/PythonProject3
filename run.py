import random

def start_game():
    while True:
        player_name = input("Welcome to the blackjack-table!\nPlease enter your name: ")
        if validate_name(player_name):
            break
    
    while True:
         buy_in = input("How much would you like to bet today? ")
         if validate_buy_in(buy_in):
            break
    
    return player_name, buy_in

def validate_name(player_name):
    correct_name = player_name.isalpha()
    if correct_name == True:
        print(f"Nice to meet you, {player_name}!\n")
        return True
    else:
        print("Please enter a valid name using only letters.\n")
        return False

def validate_buy_in(buy_in):
    if buy_in.isdigit() and 50 <= int(buy_in) <= 5000:
        print(f"Wonderful! {buy_in} it is!\n")
        return True
    else:
        print("Please enter a valid buy-in amount between 50 and 5000.\n")
        return False

def rules():
    print("Before we start, would you like to go over the rules?")
    answer = input("Press y for yes and n for no: ")
    while answer not in ['y', 'n']:
        print("Please enter a valid answer.")
        answer = input("Press y for yes and n for no: ")
    
    if answer == 'y':
        print("Here are the rules...")
    elif answer == 'n':
        print("Great, let's get started!\n")

def deal_cards():
    dealer_hand = [random.randint(1, 13), random.randint(1, 13)]
    player_hand = [random.randint(1, 13), random.randint(1, 13)]

    print(f"Dealers hand: {dealer_hand}")
    print(f"Players hand: {player_hand}")
    player_hand = new_card(player_hand)

def new_card(player_hand):
    while sum(player_hand) <= 21:
        hit_or_stay = input("Would you like to hit or stay? ").lower()
        if hit_or_stay == "hit":
            player_hand.append(random.randint(1, 13))
            print(f"player's hand: {player_hand}")
        elif hit_or_stay == "stay":
            break
        else:
            print("Please enter either 'hit' or 'stay'.")
    return player_hand

def main():
    start_game()
    rules()
    deal_cards()
    new_card(player_hand)

main()