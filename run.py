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
        print("Here are the rules...\n")
    elif answer == 'n':
        print("Great, let's get started!\n")

def generate_cards():
    dealer_hand = [random.randint(1, 11), random.randint(1, 10)]
    player_hand = [random.randint(1, 11), random.randint(1, 10)]
    return dealer_hand, player_hand

def player_turn(player_hand):
    while sum(player_hand) < 21:
        player_input = input("Would you like to hit or stay? ")
        if player_input.lower() == "hit":
            player_hand.append(random.randint(1, 10))
            print("Player hand: ", player_hand)
        elif player_input.lower() == "stay":
            print("Player's turn over.\nDealer's turn.\n")
            break
        else:
            print("Invalid input, please try again. \n")
    if sum(player_hand) > 21:
        print("Game over")
    
def dealer_turn(dealer_hand):
    while sum(dealer_hand) <= 18:
        new_card = random.randint(1, 10)
        dealer_hand.append(new_card)
        if sum(dealer_hand) > 21:
            dealer_hand.remove(new_card)
    return dealer_hand

def main():
    start_game()
    rules()
    dealer_hand, player_hand = generate_cards()
    print("Dealer hand:", dealer_hand)
    print("Player hand:", player_hand)
    player_turn(player_hand)
    dealer_turn(dealer_hand)
    print("Dealer hand: ", dealer_hand)
    print("Player hand: ", player_hand)

main()