import random

suits = ["♠", "♣", "♥", "♦"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

class Card:
    def __init__ (self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__ (self):
        return(f"*- - -*\n|{self.suit}    |\n|  {self.rank}  |\n|    {self.suit}|\n*- - -*")

class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return 'The deck has:' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        # card passed in from Deck.deal() -> single card (suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1 

class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips! You have: {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or Stand (h/s)? ")
        if x[0].lower() == "h":
            hit(deck,hand)
        elif x[0].lower() == "s":
            print("Player stand\nDealer's turn")
            playing = False
        else:
            print("Sorry, I did not understand that. Please enter h or s only")
            continue
        break

def show_some(player, dealer):
    #show only one of the dealer's cards
    print("\nDealer's hand:")
    print("First card hidden!\n*- - -*\n|x    |\n|  x  |\n|    x|\n*- - -*")
    print(dealer.cards[1])
    
    #show all (2 cards) of the player's cards
    print("\nPlayer's hand: ", *player.cards, sep="\n")

def show_all(player,dealer):
    print("\nDealer's hand: ", *dealer.cards, sep="\n")    
    print(f"Value of dealer's hand is: {dealer.value}")

    print("\nPlayer's hand: ", *player.cards,  sep="\n")    
    print(f"Value of player's hand is: {player.value}")

def player_busts(player, dealer, chips):
    print("PLAYER BUSTED! DEALER WINS")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("DEALER BUSTED! PLAYER WINS")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and player tie! PUSH")

playing = True

print("WELCOME TO BLACKJACK")
total_chips = int(input("Enter the total amount of chips you want to start with: "))
player_chips = Chips(total_chips)
while player_chips.total > 0:
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
        
    print("\nPlayer total chips are at: {}".format(player_chips.total))

    if player_chips.total == 0:
        print("You have run out of chips! Game over.")
        break

    new_game = input("Would you like to play another hand? ")
    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing")
        break


