import random
#possible values of the cards
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1} #default to 11
#possible suits of the cards
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
#possible ranks of the cards
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace']
p_ace = 0
d_ace = 0


class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__(self):
    return self.rank + " of " + self.suit


class Deck:

  def __init__(self):
    self.all_cards = []
  
    for suit in suits: #assigns cards to deck class
      for rank in ranks:
        created_card = Card(suit, rank)
        self.all_cards.append(created_card)

  def shuffle(self):
      random.shuffle(self.all_cards)

  def hit(self):
      return self.all_cards.pop(0)



class Dealer:

    def __init__(self):
        self.dealer_deck = []
    
    def d_val(self):
      return sum(c.value for c in self.dealer_deck) + d_ace

    def clear_deck(self, player_deck):
      self.deck_deck.clear()

    def __str__(self):      
      if len(self.dealer_deck) > 0:
        return "The Dealer has {} cards. The cards are {}. Their combined value is {}.\n".format(len(self.dealer_deck), ", ".join([str(i) for i in self.dealer_deck]), self.d_val())
      else:
        return "The Dealer has 0 cards.\n"


class Player:

    def __init__(self, name):
        self.name = name
        self.player_deck = []
    
    def p_val(self):
      return sum(c.value for c in self.player_deck) + p_ace
    
    def clear_deck(self, player_deck):
      self.player_deck.clear()

    def __str__(self):
      
      if not self.player_deck:
        return "{} has 0 cards.\n".format(self.name)
      else:
        return "{} has {} cards. The cards are {}. Their combined value is {}.\n".format(self.name, len(self.player_deck), ", ".join([str(i) for i in self.player_deck]), self.p_val())



def hit_stand(): #user decides hit or stand
  global p_ace
  while True: #asks whether they want to hit or stand
    hors = str(input("To hit press 1 and to stand press 0: "))

    if hors not in ["0", "1"]: #checks if input is valid
      print("Invalid Value. Try again.\n")
      continue
    break #if valid --> break out of while loop
  
  if hors == "1": #hit
    new_card = new_deck.hit()
    new_player.player_deck.append(new_card)
    print("{} decided to hit and recieved a {}.\n".format(new_player.name, new_card))
    return True #player hit

  else: #stand
    print("{} decided to stand.\n".format(new_player.name))
    print(new_player)
    if 1 in [c.value for c in new_player.player_deck]: #check if user has ace after standing
      while True: #Take in input until valid value is inputted
        ace = str(input("\nTo make your ace worth 11, press 1, and to make it worth 1, press 0: "))
        if ace not in ["0", "1"]: #valid input check
          print("Invalid Value. Try again.\n")
          continue
        break #if valid --> break out of while loop
      if ace == "1": #make 11
        p_ace = 10
      elif ace == "0": #make 1
        p_ace = 0
      print(new_player)

    return False #player stood



      
def W_check(): #check if player won
  if new_player.p_val() > 21:
    return False #player lost
  else:
    return True #player keeps going


def D_play(d_val):
  global d_ace
  if 1 in [c.value for c in new_dealer.dealer_deck]: #ACE IN DECK
    if (d_val + 10 > 16) and (d_val + 10 < 22): #dealer can stand by changing ace value
      d_ace = 10
      print("The Dealer has changed their Ace to a value of 11\n")
      print(new_dealer)
      return False #dealer changed ace value
    elif (d_val > 16) and (d_val < 22): #dealer's hand is already between 16 and 21
      print('The Dealer decides to stand\n')
      return False #dealer stands
    elif (d_val > 21): #dealer's hand went over 21
      return False #dealer went bust 
    else: #dealer doesn't have to change ace value and can hit another card
      d_card = new_deck.hit()
      new_dealer.dealer_deck.append(d_card)
      print("The Dealer decided to hit and recieved a {}.\n".format(d_card))
      print(new_dealer)
      return True #dealer hit
  else: #NO ACE IN DECK
    if d_val < 17: #dealer hits whenever their hand value is less than 17
      d_card = new_deck.hit()
      new_dealer.dealer_deck.append(d_card)
      print("The Dealer decided to hit and recieved a {}.\n".format(d_card))
      print(new_dealer)
      return True #dealer hit
    elif (d_val > 16) and (d_val < 22): #dealer stands if their hand value is in between 16 and 21
      print('The Dealer decides to stand\n')
      return False #dealer stands
    elif (d_val > 21): #dealer's hand went over 21 
      return False #dealer went bust


def WorL(p_val, d_val): #decides who won the game
  if p_val > 21 and not d_val > 21:
    return ("The Dealer won because {} went bust\n").format(new_player.name)
  elif d_val > 21 and not p_val > 21:
    return ("The Player won because the Dealer went bust\n")
  elif p_val == d_val:
    return ("It's a Tie!")
  elif p_val > d_val:
    return ("{} won!").format(new_player.name)
  elif p_val < d_val:
    return ("The Dealer Won!")

#Start Of Game Logic

print('Welcome to the game of blackjack! In this game, both you and the dealer start with two cards each. You can choose either to hit or to stand. Hitting adds a card to your hand, while standing ends your turn, and you are unable to hit again. The goal of the game is to have the values of your cards be the closest to 21 but not over 21. The cards from 2 - 10 have the values that match themselves, face cards are all worth 10, and ace can either be worth 1 or 11. If you have an ace in your hand you can change the value of the ace after each hit or stand. \n') #explains the directions of the game

#dealer and player with name is made
new_dealer = Dealer()
p_name = str(input("What is your name? "))
new_player = Player(p_name)


#deck is created and shuffled
new_deck = Deck() 
new_deck.shuffle()

while True:
  #reset default ace values
  d_ace = 0
  p_ace = 0
 
  #add two cards to player and dealer hands
  for n in range(2): 
    new_dealer.dealer_deck.append(new_deck.hit())
    new_player.player_deck.append(new_deck.hit())

  #print starting values
  print(new_player)
  print(new_dealer)

  #GAME LOGIC FOR PLAYER
  while hit_stand(): 
    if 1 in [c.value for c in new_player.player_deck]: #check if user has ace
      if not new_player.p_val() > 21 and not p_ace == 0: #avoids unecessary input for ace
        while True: #Take in input until valid value is inputted
          print(new_player)
          ace = str(input("To make your ace worth 11, press 1, and to make it worth 1, press 0: \n"))

          if ace not in ["0", "1"]: #valid input check
            print("Invalid Value. Try again.\n")
            continue
          break #valid input

        if ace == "1": #make 11
          p_ace = 10
        elif ace == "0": #make 1
          p_ace = 0

    if not W_check(): #if player went bust
      print(new_player)
      break
    print(new_player)

  #Dealer Plays if player didn't go bust
  if new_player.p_val() <= 21:
    while D_play(new_dealer.d_val()):
      pass

  #End Game Statement
  print(WorL(new_player.p_val(), new_dealer.d_val()))
  
  #check if deck needs to be renewed
  if len(new_deck.all_cards) <= 13:
    new_deck = Deck() 
    new_deck.shuffle()
    print("The deck is being reshuffled.")

  #clear player and dealer hands
  new_player.player_deck.clear()
  new_dealer.dealer_deck.clear()
  
  #Play again code -----
  while True: #check for valid input
    play_again = str(input("\nWould you like to play again (yes/y or no/n)? "))
    if play_again in ['y', 'yes', 'n', 'no']:
      break
    print("Invalid Input. Please Try Again.\n")
  
  #If they decide to play again
  if play_again in ['y', 'yes']:
    continue
  
  #If they decide to stop
  print("\nThank you for playing!!!")
  break
