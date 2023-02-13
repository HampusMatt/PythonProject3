import random

class PlayerInfo:
    def __init__(self, name=None, buy_in=None, player_hand=None, is_dealer=False):
        self.player_name = name or self.get_name()
        self.buy_in = buy_in or self.get_buy_in_value()
        self.player_hand = get_initial_cards()
        self.wager = None
        self.is_dealer = is_dealer

    def player_turn(self):
        """
        Lets the player get another card or stay the turn.
        """
        if self.is_dealer:
            self.dealer_turn()
            return
        while sum(self.player_hand) < 21:
            player_input = input("Would you like to hit or stay? ")
            if player_input.lower() == "hit":
                self.player_hand.append(random.randint(1, 10))
                print("Player hand: ", self.player_hand)
            elif player_input.lower() == "stay":
                print("Player's turn over.\nDealer's turn.\n")
                break
            else:
                print("Invalid input, please try again. \n")
        if sum(self.player_hand) == 21:
            print("BlackJack!")
        elif sum(self.player_hand) > 21:
            print("You're over 21! Busted!\n")

    def dealer_turn(self):
        """
        Gives the dealer a new random card. The function makes sure that the dealer never busts and that it always hits 18 or better.
        """
        dealer_hand = self.player_hand
        while sum(dealer_hand) <= 18:
            new_card = random.randint(1, 10)
            dealer_hand.append(new_card)
            if sum(dealer_hand) > 21:
                dealer_hand.remove(new_card)
            else:
                print("Dealer is dealing")
                print(dealer_hand)
        return dealer_hand

    def get_name(self):
        """
        Lets the player input a name.
        """
        try:
            player_name = input("Please enter your name: ")
            if validate_name(player_name):
                return player_name
            else:
                raise ValueError()
        except ValueError:
            return self.get_name()

    def set_hands(self):
        self.player_hand = get_initial_cards()

    def get_buy_in_value(self):
        """
        Asks the player for an amount to be gambled with. Update this to an try-except.
        """
        while True:
            buy_in = input("How much would you like to bet today? ")
            if validate_buy_in(buy_in):
                break
        
        return int(buy_in)


    def set_player_wager(self):
        """
        Asks for a wager to be gambled on every round and checks if it's within the buy-in amount.
        """
        while True:
            wager = int(input("How much would you like to wager? "))
            if wager <= self.buy_in:
                print(f"You have wagered {wager} on this turn\n")
                break
            else:
                print("Your wager can't be larger than your buy-in. Please try again.")
        self.wager = wager

    def set_updated_buy_in(self, updated_buy_in):
        self.buy_in = updated_buy_in

def validate_name(player_name):
    """
    Checks if the players name is letters only.
    """
    correct_name = player_name.isalpha()
    if correct_name:
        print(f"Nice to meet you, {player_name}!\n")
        return True
    else:
        print("Please enter a valid name using only letters.\n")
        return False

def validate_buy_in(buy_in):
    """
    Checks if the buy in is a number and within accepted range.
    """
    if buy_in.isdigit() and 50 <= int(buy_in) <= 5000:
        print(f"Wonderful! {buy_in} it is!\n")
        return True
    else:
        print("Please enter a valid buy-in amount between 50 and 5000.\n")
        return False

def ask_to_show_rules():
    """
    Asks the player if they would like to have the rules explained before the game.
    """
    print("Before we start, would you like to go over the rules?")
    answer = input("Press y for yes and n for no: ")
    while answer not in ['y', 'n']:
        print("Please enter a valid answer.")
        answer = input("Press y for yes and n for no: ")
    
    if answer == 'y':
        print("You get 2 cards. The goal is to get as close to 21 as possible without going over. You can either get another card (hit), or stay where you are. You play against the dealer. Whomever is closest to 21 wins.\n")
    elif answer == 'n':
        print("Great, let's get started!\n")

def get_initial_cards():
    """
    A function that randomises the initial cards.
    """
    return [random.randint(1, 11), random.randint(1, 10)]

def check_results(player_hand, dealer_hand):
    """
    Checks the winner of the round by comparing the sum of the player hand and the dealer hand.
    """
    player_sum = sum(player_hand)
    dealer_sum = sum(dealer_hand)
    if player_sum > 21:
        print("You lost!")
        return "loose"
    elif player_sum > dealer_sum:
        print("You won!")
        return "win"
    elif dealer_sum > player_sum:
        print("You lost!")
        return "loose"
    else:
        print("It's a draw!")
        return "draw"

def get_updated_buy_in(player, result):
    updated_value = player.buy_in
    if result == "win":
        updated_value = player.buy_in + player.wager
    elif result == "loose":
        updated_value = player.buy_in - player.wager
    elif result == "draw":
        print("\nYour buy-in stays the same")
        updated_value = player.buy_in
    print("\nYour new buy-in is: ", updated_value)
    return updated_value

def main():
    player = PlayerInfo()
    ask_to_show_rules()
    player.set_player_wager()
    dealer = PlayerInfo("dealer", "NA", None, True)

    while True:
        print("New round")
        player.set_hands()
        dealer.set_hands()
        print("Dealer hand:", dealer.player_hand)
        print("\nPlayer hand:", player.player_hand)
        player.player_turn()
        dealer.player_turn()
        print("\nPlayer hand: ", player.player_hand)
        print("Dealer hand: ", dealer.player_hand)
        result = check_results(player.player_hand, dealer.player_hand)
        updated_buy_in = get_updated_buy_in(player, result)
        player.set_updated_buy_in(updated_buy_in)

        #Do you want to play, if no, then break out of the loop


main()