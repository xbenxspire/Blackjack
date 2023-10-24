'''
Created on Oct 20, 2023
@author: Benjamin Pierce
This program utilizes the card-dealer.py program to simulate a simplified game of Blackjack (aka 21) between two players.
'''
import random

# Define the deck of cards
deck = {
    'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
    '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
    '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
    '10 of Spades': 10, 'Jack of Spades': 10,
    'Queen of Spades': 10, 'King of Spades': 10,
    
    'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
    '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
    '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
    '10 of Hearts': 10, 'Jack of Hearts': 10,
    'Queen of Hearts': 10, 'King of Hearts': 10,
    
    'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
    '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
    '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
    '10 of Clubs': 10, 'Jack of Clubs': 10,
    'Queen of Clubs': 10, 'King of Clubs': 10,
    
    'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
    '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
    '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
    '10 of Diamonds': 10, 'Jack of Diamonds': 10,
    'Queen of Diamonds': 10, 'King of Diamonds': 10
}

#Create list of card keys for the deck
deck_keys = list(deck.keys())

#Function to calculate total value of a hand
def calculate_hand_value(hand):
    total_value = sum(deck[card] for card in hand)
    aces = [card for card in hand if 'Ace' in card]

    while total_value > 21 and aces:
        total_value -= 10
        aces.pop()

    return total_value

#Function to play Blackjack
def play_blackjack_game():
    random.shuffle(deck_keys)    #shuffle deck function
    player1_hand = []
    player2_hand = []

    while deck_keys:
        player1_card = deck_keys.pop()    #pop function to remove cards from deck after they are drawn
        player2_card = deck_keys.pop()
        player1_hand.append(player1_card)
        player2_hand.append(player2_card)

        player1_total = calculate_hand_value(player1_hand)   #calculate points each player has
        player2_total = calculate_hand_value(player2_hand)

        print(f"Player 1's hand: {', '.join(player1_hand)}, Score: {player1_total}")    #print each player's points with cards in hand
        print(f"Player 2's hand: {', '.join(player2_hand)}, Score: {player2_total}")

        if player1_total == 21 or player2_total > 21:    #conditions for either player to win or bust/lose
            return "Player 1 wins"
        elif player2_total == 21 or player1_total > 21:
            return "Player 2 wins"
        elif player1_total > 21 and player2_total > 21:
            return "Both players bust"

#Play multiple games until the deck is empty
while deck_keys:
    print("New game:")
    result = play_blackjack_game()
    print(result)

print("The cards ran out, end of game.")    #when cards run out in the middle of a game, end of game