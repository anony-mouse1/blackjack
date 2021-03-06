# set chips
player_chips = 500

# set two dictionaries--one for card distribution and the other for while hitting
change_cards_during = {'A ': [1, 11], 'K ': 10, 'Q ': 10, 'J ': 10}
change_cards_start = {'A ': 11, 'K ': 10, 'Q ': 10, 'J ': 10}

# creating deck
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
deck = [f"{j} of {i}" for j in nums for i in suits]
deck = ['2 of Spades', 'Q of Clubs', 'K of Diamonds', 'J of Spades', 'A of Clubs', '2 of Diamonds', '3 of Spades',
        '2 of Clubs', '4 of Diamonds']
player_cards = []
dealer_cards = []
player_status = ''
dealer_status = ''


# distribute cards to player and dealer, turn them into numerical values.


def distribution():
    # global not needed for cards, nor deck
    # global is needed for chips.
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

    print(f"Player Cards: {deck[2]} and x")  # store deck[3] somewhere else.
    for i in range(4):
        deck.pop(0)
    # print(deck)


# here will print original deck

distribution()


# print(player_cards, dealer_cards)


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


hit(player_cards)


# you don't need a naturals function--this does it right for you!!
def player_input():
    global player_status
    while (sum(player_cards)) <= 20:
        player_decision = ''
        while player_decision not in ['hit', 'stand']:
            player_decision = input("Player, do you wish to hit or stand? ")
        if player_decision == 'hit':
            hit(player_cards)
        elif player_decision == 'stand':
            print("Player has standed")
            player_status = 'stand'
            return
    else:
        if sum(player_cards) == 21:
            print("Player has received blackjack!")
            player_status = 'blackjack'

            return
        else:
            player_status = 'bust'
            print("Player has busted! No money earned.")
            return


def dealer_input():
    global dealer_status

    if sum(dealer_cards) <= 16:
        hit(dealer_cards)

    elif 17 <= sum(dealer_cards) <= 20:
        print("Dealer has standed")
        dealer_status = 'stand'
        return

    elif sum(dealer_cards) == 21:
        dealer_status = 'blackjack'
        print("Dealer has received blackjack!")
        return

    else:
        dealer_status = 'bust'
        print("Dealer has busted!")
        return


player_input()
dealer_input()

print(f"D STATUS {dealer_status}")
print(f"P STATUS {player_status}")


def payouts():
    if player_status == dealer_status:



print(player_cards)  # still 'globalled' without calling global
