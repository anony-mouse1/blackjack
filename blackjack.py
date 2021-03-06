from random import shuffle

# set chips
player_chips = 500

# set two dictionaries--one for card distribution and the other for while hitting
change_cards_during = {'A ': [1, 11], 'K ': 10, 'Q ': 10, 'J ': 10}
change_cards_start = {'A ': 11, 'K ': 10, 'Q ': 10, 'J ': 10}


def distribution():
    # global not needed for cards, nor deck
    # global is needed for chips.
    print(player_cards)
    print(dealer_cards)
    print(f"Player Cards: {deck[0]} and {deck[1]}")
    for i in range(2):
        card = deck[i][:2]
        if card in change_cards_start:
            player_cards.append(change_cards_start.get(card))
        else:
            player_cards.append(int(card))

    for i in range(2, 4):
        card = deck[i][:2]
        if card in change_cards_start:
            dealer_cards.append(change_cards_start.get(card))
        else:
            dealer_cards.append(int(card))

    print(f"Dealer Cards: {deck[2]} and {deck[3]}")  # store deck[3] somewhere else.
    print(f"Sum of player card values: {sum(player_cards)}")
    for i in range(4):
        deck.pop(0)

# here will print original deck

# distribution()

# here will print altered deck

def hit(person_cards):
    print(f"\nHITTING...\nThe card is {deck[0]}")
    hitting_card = deck[0][:2]
    hitting_card = change_cards_during.get(hitting_card, hitting_card)
    if hitting_card == [1, 11]:
        if sum(person_cards) > 10:
            person_cards.append(hitting_card[0])
            print(f"You received an Ace valued at {hitting_card[0]}")
        else:
            person_cards.append(hitting_card[1])
            print(f"You received an Ace valued at {hitting_card[1]}")
    else:
        person_cards.append(int(hitting_card))
    print(f"During hit {player_cards}")  # it works
    print(f"Sum of cards during hit {sum(player_cards)}")
    deck.pop(0)
    # len(deck) in and out of function works fine


# hit(player_cards)


# you don't need a naturals function--this does it right for you!!
def player_input():
    global player_status, player_chips
    while (sum(player_cards)) <= 20:
        player_decision = ''
        while player_decision not in ['hit', 'stand']:
            player_decision = input("Player, do you wish to hit or stand? ")
        if player_decision == 'hit':
            hit(player_cards)
        elif player_decision == 'stand':
            print("Player has standed")
            player_status = 'stand'
            break
    else:
        if sum(player_cards) == 21:
            print("Player has received blackjack!")
            player_status = 'blackjack'
            player_chips += 10

        else:
            player_status = 'bust'
            print("Player has busted! No money earned.")


def dealer_input():
    global dealer_status
    print("Dealer's turn...")
    while sum(dealer_cards) <= 16:
        hit(dealer_cards)

    else:
        if 17 <= sum(dealer_cards) <= 20:
            dealer_status = 'stand'
            print("Dealer has standed")


        elif sum(dealer_cards) == 21:
            dealer_status = 'blackjack'
            print("Dealer has received blackjack!")


        else:
            dealer_status = 'bust'
            print("Dealer has busted!")


def payouts():
    # player status at this point has to be stand
    if player_status == 'stand':
        if dealer_status == 'stand':

            # don't need the top two lines ngl
            if sum(player_cards) > sum(dealer_cards):
                print("Player has won standoff.")
            elif sum(player_cards) > sum(dealer_cards):
                print("Dealer has won standoff. ")
            else:
                print("Standoff has resulted in a tie--bets pushed")
        else:
            print("Malfunction")
    else:
        print("Malfunction")


while player_chips >0:
    player_cards = []
    dealer_cards = []
    player_status = ''
    dealer_status = ''
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    deck = [f"{j} of {i}" for j in nums for i in suits]

    '''deck = ['2 of Spades', 'Q of Clubs', 'K of Diamonds', 'J of Spades', 'A of Clubs', '2 of Diamonds',
            '3 of Spades',
            '2 of Clubs', '4 of Diamonds']'''

    # distribute cards to player and dealer, turn them into numerical values.

    while True:
        distribution()
        player_input()
        if player_status == 'blackjack':
            break
        elif player_status == 'bust':
            break
        else:
            dealer_input()
            if dealer_status == 'blackjack':
                break
            if dealer_status == 'bust':
                break
            else:
                payouts()
                break

    print(f"D STATUS {dealer_status}")
    print(f"P STATUS {player_status}")
else:
    print("Insufficient chips")

    #print(player_cards)  # still 'globalled' without calling global
