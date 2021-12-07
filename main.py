## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
from replit import clear
import random

wants_to_play = input("Do you want to play a game of Blackjack? type 'y' for yes and 'n' for no. ").lower()


def blackjack():
  print(logo)
  players_hand = []
  computers_hand = []

  def deal_card(hand):
    """
    Deals one random card to the hand that is passed in. 
    """
    card = random.choice(cards)
    hand.append(card)

  for card in range(2):
    deal_card(players_hand)
    deal_card(computers_hand)

  # build function to hit or stay so this behavior can be called multiple times
  def hit_or_stay():
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if hit == "y":
      clear()
      deal_card(players_hand)
      players_hand_total = sum(players_hand)
      computers_hand_total = sum(computers_hand)
      if computers_hand_total < 17:
        deal_card(computers_hand)
      choose_winner()
    else:
      players_hand_total = sum(players_hand)
      computers_hand_total = sum(computers_hand)
      if players_hand_total > computers_hand_total and not players_hand_total > 21:
        print(f"You win! 🔥 - Your hand: {players_hand} - Total score: {players_hand_total}")
      else:
        print(f"You lose. Computer has {computers_hand_total} with their hand - {computers_hand}")

  def choose_winner():
    players_hand_total = sum(players_hand)
    computers_hand_total = sum(computers_hand)

    if 11 in players_hand and sum(players_hand) > 21:
      players_hand.remove(11)
      players_hand.append(1)

    if players_hand_total > 21:
      print(f"You went over with {players_hand_total}. you lose - {players_hand}")
      return
    elif computers_hand_total > 21:
      print(f"The computer went over with {computers_hand_total} and had a hand of {computers_hand}. You win 😘")
      return
    elif players_hand_total == computers_hand_total:
      print( f"It's a draw - Players hand {players_hand_total} \nComputers hand {computers_hand_total}")
      return
    elif players_hand_total == 21:
      print(f"You win you got blackjack! {players_hand}")        
      return
    elif computers_hand_total == 21:
      print(f"You lose. The computer got blackjack. {computers_hand}")
      return
    else:
      print(f"Your cards: {players_hand}. Current score {sum(players_hand)} \n")
      print(f"Computers hand: {computers_hand[0]}")
      hit_or_stay()

  choose_winner()

  play_again = input("\nWould you like to play another hand of Blackjack? ")       

  if play_again == "y":
    clear()
    blackjack()
  else:
    print("Thanks for playing! Goodbye.")
    return
        
if wants_to_play == 'y':
  blackjack()
