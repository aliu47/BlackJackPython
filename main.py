import random
import tkinter
from tkinter import *
def faceCard(card):
    if(card == 1):
        card = "Ace"
    if(card == 11):
        card = "Jack"
    if(card == 12):
        card = "Queen"
    if(card == 13):
        card = "King"
    return card
def generateDeck():
    deck = []
    for i in range(1, 53):
        if(i <= 13):
            j = 14-i
            j = faceCard(j)
            # card=str(j)+" of Spades"
        if(14 <= i <= 26):
            j = 27-i
            j = faceCard(j)
            # card=str(j)+" of Hearts"
        if(27 <= i <= 39):
            j = 40-i
            j = faceCard(j)
            # card=str(j)+" of Clubs"
        if(40 <= i < 52):
            j = 53-i
            j = faceCard(j)
            # card=str(j)+" of Diamonds"
        card = j
        print(card)
        deck.append(card)
    return deck
def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand
def calculate(hand):
  value=0
  for card in hand:
    if card == "Jack" or card == "Queen" or card == "King":
       value+= 10
    elif card == "Ace":
      if value >= 11: 
        value+=1 
      else: 
        value+= 11
    else:
	    value += card
  return value
def hit(hand,deck):
    print("deal")
    random.shuffle(deck)
    card = deck.pop()
    hand.append(card)
    return card
def play():
    choice = 0
    deck = generateDeck()
    dealer = deal(deck)
    player = deal(deck)
    playerValue = calculate(player)
    dealerValue = calculate(dealer)
    print("Lets play blackjack!")
    while choice != "S":  
      print("dealer Has a  " + str(dealer[0]))
      print(player)
      print("player Hand value "+str(playerValue))
      choice = input("Do you want to [H]it, [S]tand").upper()
      if choice == "H":
        player = hit(player)
        playerValue = calculate(player)
      if choice == "S":
        #Dealer hits
        print("Dealer has "+str(dealerValue))
        if(dealerValue>=playerValue):
          print("You Lose")
        else:
          print("You Win!")
def playGUI():
  m=tkinter.Tk()
  deck = generateDeck()
  player = deal(deck)
  m.setvar(name='player', value=player)
  dealer = deal(deck)
  playerValue = calculate(m.getvar(name='player'))
  dealerValue = calculate(dealer)
  m.title('BlackJack')
  ourMessage ='Lets Play BlackJack!'
  messageVar = Message(m, text = ourMessage,width=300) 
  messageVar.pack()  
  player_label =Label(m,text=player)
  playerHand_label = Label(m, text="Your hand:\n"+str(m.getvar(name='player'))+"\nValue: "+str(playerValue))
  player_label.pack()
  #playerHand_label.pack()
  w = Canvas(m, width=400, height=500) 
  w.pack() 
  button = tkinter.Button(m, text='Stop', width=20, command=m.destroy)
  buttonH = tkinter.Button(m, text='Hit', width=20, command=player.append(hit(player,deck)))
  buttonS = tkinter.Button(m, text='Stand', width=20, command=m.destroy)
  button.pack(side=LEFT) 
  buttonH.pack(side=LEFT) 
  buttonS.pack(side=LEFT) 
  m.mainloop()

playGUI()
