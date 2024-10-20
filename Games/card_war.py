import random

# Tuples to define the suits and ranks of cards
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

# Dictionary to map card ranks to their corresponding values
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

class Card:
    """
    Single playing card
    Attributes
        suit (str)
            The suit of the card (e.g., 'Hearts')
        rank (str)
            The rank of the card (e.g., 'Two')
        value (int)
            The value of the card based on the rank
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    """
    Deck of 52 playing cards
    Attributes
        all_cards (list)
            A list containing all the cards in the deck
    """

    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    
class Player:
    """
    Player in the card game
    Attributes
        name (str)
            The name of the player
        all_cards (list)
            A list of cards that the player currently holds
    """
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type ([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

# GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

# Split the deck between the two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

# MAIN WHILE LOOP
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One wins!")
        game_on = False
        break
    
    #START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # WHILE AT WAR
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False
        else:
            print("WAR")
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("Player Two wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("Player One wins!")
                game_on = False
                break
            else:
                for num in range():
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())




