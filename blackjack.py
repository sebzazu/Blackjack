import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6,
        7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

value_dict = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}

player_hand = []
dealer_hand = []
dealer_value = 0
player_value = 0


def deal():
    global player_value  # Variable not recognized in for loops
    global dealer_value

    dcard1 = random.choice(deck)
    dealer_hand.append(dcard1)
    deck.remove(dcard1)

    pcard1 = random.choice(deck)
    player_hand.append(pcard1)
    deck.remove(pcard1)

    dcard2 = random.choice(deck)
    dealer_hand.append(dcard2)
    deck.remove(dcard2)

    pcard2 = random.choice(deck)
    player_hand.append(pcard2)
    deck.remove(pcard2)

    for card in player_hand:  # Calculate Value immediately after dealing
        if card != 'A':
            card_value = value_dict.get(card)
            player_value += card_value

    for card in dealer_hand:
        if card != 'A':
            card_value = value_dict.get(card)
            dealer_value += card_value

    for card in player_hand:  # Check for state of ace value and add to value calculation
        if card == 'A' and player_value <= 10:
            player_value += 11
        elif card == 'A' and player_value > 10:
            player_value += 1

    for card in dealer_hand:
        if card == 'A' and dealer_value <= 10:
            dealer_value += 11
        elif card == 'A' and dealer_value > 10:
            dealer_value += 1

    print('Your Hand: ')
    print(player_hand)
    print(player_value)

    print('Dealer Hand: ')
    print(dealer_hand)
    print(dealer_value)


def hit_player():
    global player_value  # Variable Scope Issue, receive error without global statement

    new_card = random.choice(deck)
    player_hand.append(new_card)
    deck.remove(player_hand[-1])
    player_value += value_dict.get(new_card)  # Recalculate value after each additional card added

    if new_card == 'A' and player_value <= 10:
        player_value += 11
    elif new_card == 'A' and player_value > 10:
        player_value += 1

    print(player_hand)
    print(player_value)


def hit_dealer():
    global dealer_value  # Variable Scope Issue, receive error without global statement

    new_card = random.choice(deck)
    dealer_hand.append(new_card)
    deck.remove(dealer_hand[-1])
    dealer_value += value_dict.get(new_card)  # Recalculate value after each additional card added

    if new_card == 'A' and dealer_value <= 10:
        dealer_value += 11
    elif new_card == 'A' and dealer_value > 10:
        dealer_value += 1

    print(dealer_hand)
    print(dealer_value)


def play_round():
    player_choice = input('Hit or Stand? ').upper()

    if player_choice == 'HIT' and player_value < 21:
        hit_player()
    elif player_choice == 'STAND':
        while dealer_value < 17:
            hit_dealer()


def main():
    deal()
    play_round()

    print('Your Hand: ')
    print(player_hand)
    print(player_value)

    print('Dealer Hand: ')
    print(dealer_hand)
    print(dealer_value)

    if dealer_value < player_value <= 21:
        print('You Win!')
    elif player_value < dealer_value <= 21:
        print('You Lose!')
    elif player_value == dealer_value:
        print('PUSH!')
    elif player_value > 21 and dealer_value < 21:
        print('You Lose!')
    elif dealer_value > 21 and player_value < 21:
        print('You Win!')


main()
