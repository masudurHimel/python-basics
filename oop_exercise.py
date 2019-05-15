from random import shuffle

# to make the ranking things

suite = "H D S C"
suite.split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A"
ranks.split()


class Deck():
    def __init__(self):
        print("Creating new order deck")
        self.all_cards = [(s, r) for s in suite for r in ranks]

    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.all_cards)

    def split_in_half(self):
        return (self.all_cards[:26], self.all_cards[26:])


class Hand():

    def __init__(self, card):
        self.card = card

    def __str__(self):
        # how many cards
        print("Contains {} cards".format(len(self.card)))

    def add(self, added_cards):
        # add cards to the hand
        self.card.extend(added_cards)

    def remove_card(self):
        # removes  card from hand
        return self.card.pop()


class Player():

    def __init__(self, name, hand):
        # initialization
        self.name = name
        self.hand = hand

    def play_card(self):
        # drawn card and printing the drawn card and return the drawn card
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.hand, drawn_card))
        print()
        return drawn_card

    def remove_war_cards(self):
        # war_cards and append 3 cards as per the rule
        war_cards = []
        for i in range(3):
            war_cards.append(self.hand.remove_card())

        return war_cards

    def still_has_card(self):
        # return true if player still has card in hand
        return len(self.hand.card) != 0

# Gameplay Starts here

# create a new deck
# and split it in half
#need to implement the gameplay part


