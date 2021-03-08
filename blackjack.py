from random import shuffle

# set chips
player_chips = 500

# set two dictionaries--one for card distribution and the other for while hitting
change_cards_during = {'A ': [1, 11], 'K ': 10, 'Q ': 10, 'J ': 10}
change_cards_start = {'A ': 11, 'K ': 10, 'Q ': 10, 'J ': 10} #gah this doesn't work for two aces.


def distribution():
    global player_cards, dealer_cards
    # global not needed for cards, nor deck--actually global is needed if you are completely altering the deck, in which case i am.
    # global is needed for chips.
    print(player_cards) #its empty (which is good)
    print(dealer_cards) #its empty (which is good)
    print(f"Player Cards: {deck[0]} and {deck[1]}")
    for i in range(2):
        card = deck[i][:2]
        if card in change_cards_during:
            player_cards.append(change_cards_start.get(card))
        else:
            player_cards.append(int(card))
        if player_cards == [11,11]:
            player_cards = [1,11]



    for i in range(2, 4):
        card = deck[i][:2]
        if card in change_cards_start:
            dealer_cards.append(change_cards_start.get(card))
        else:
            dealer_cards.append(int(card))

        if dealer_cards == [11,11]:
            dealer_cards = [1,11]
    print(f"Dealer Cards: {deck[2]} and x")  # store deck[3] somewhere else--stored in temp
    print(f"Sum of Player Card Values: {sum(player_cards)}")
    print(f"Player's Cards: {player_cards}")
    for i in range(4):
        deck.pop(0)


# here will print original deck

# distribution()

# here will print altered deck

def hit(person_cards):
    #global player_cards, dealer_cards
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
    # print(f"During hit {player_cards}")  # it works
    if sum(person_cards)>21:
        person_cards[:] = [1 if x == 11 else x for x in person_cards]
        print("Ace Values have changed based on the sum of your card values.")

    print(f"Total card values: {sum(person_cards)}")
    print(f"Cards: {person_cards}")
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
            player_chips += (bet * 5 / 2)

        else:
            player_status = 'bust'
            print("Player has busted! No money earned.")


def dealer_input():
    global dealer_status
    print("\nDealer's turn...")
    print(f"Dealer, flipping second card...\nDealer, your cards are {temp[0]} and {temp[1]}")
    print(dealer_cards)
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
    global player_chips
    # player status at this point has to be stand
    if player_status == 'stand':
        if dealer_status == 'stand':
            # don't need the top two lines ngl
            if sum(player_cards) > sum(dealer_cards):
                print("Player has won standoff.")
                player_chips += (bet * 2)
            elif sum(player_cards) < sum(dealer_cards):
                print("Dealer has won standoff. ")
            elif sum(player_cards) == sum(dealer_cards):
                print("Standoff has resulted in a tie--bets pushed")
                player_chips += bet
        else:
            print("Malfunction")
    else:
        print("Malfunction")


while player_chips > 0:

    player_cards = []
    dealer_cards = []
    player_status = ''
    dealer_status = ''
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    deck = [f"{j} of {i}" for j in nums for i in suits]

    shuffle(deck)
    '''deck = ['A of Spades', '2 of Clubs', '6 of Diamonds', '2 of Spades', 'A of Clubs', 'A of Diamonds',
            '3 of Spades',
     '2 of Clubs', '4 of Diamonds', '8 of Spades', '3 of Diamonds', '3 of Hearts', '2 of Diamonds']'''
    temp = [deck[2], deck[3]]
    print("\nNEW ROUND\n")
    print(f"Your chips are: {player_chips}")
    while True:
        try:
            bet = int(input("Betting value: "))
            if int(bet) <= player_chips and int(bet) % 5 == 0 and int(bet) != 0:
                print(f"Your betting value is {bet}")
                player_chips -= bet
                print(f"\nUpdated chips: {player_chips}")
                break
        except:
            print("Not a valid input")
            continue

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

    # print(f"D STATUS {dealer_status}")
    # print(f"P STATUS {player_status}")

else:
    print("Insufficient chips. Rerun program.")

    # print(player_cards)  # still 'globalled' without calling global

# next step- turn into classes