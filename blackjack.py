import random
import tkinter
from tkinter import *

global deck,player,dealer,playerValue,dealerValue,splitValue,split
m=tkinter.Tk()

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
def hitPlayer():
    print("deal")
    random.shuffle(deck)
    card = deck.pop()
    player.append(card)
    player_label.config(text='Your hand: ' +str(player))
    global playerValue
    playerValue=calculate(player)
    playerValue_label.config(text='Value: '+str(playerValue))
    if(playerValue>21):
        playerValue_label.config(text='BUST')
        buttonH.config(state=DISABLED)
        print(splitValue)
        if(len(split)==0 or splitValue>21):
            Winner()


def hitDealer(deck):
    print("deal")
    random.shuffle(deck)
    card = deck.pop()
    dealer.append(card)

def standPlayer():
    print('stand')
    buttonH.config(state=DISABLED)

    global dealerValue
    dealerValue = calculate(dealer)
    while(dealerValue<17):
        dealer_label.config(text='Dealer hand: '+str(dealer)+'\nDealer Value: '+str(dealerValue))    
        if(dealerValue<17):
            hitDealer(deck)
            dealerValue=calculate(dealer)
    dealer_label.config(text='Dealer hand: '+str(dealer)+'\nDealer Value: '+str(dealerValue))    
    if(dealerValue>21):
        dealer_label.config(text='Dealer hand: '+str(dealer)+'\nDealer Value: BUST')    
    Winner()
    if(len(split)>0):
        splitWinner()

def hitSplit():
    print('splithit')
    random.shuffle(deck)
    card = deck.pop()
    split.append(card)
    split_label.config(text='Your split: ' +str(split))
    global splitValue
    splitValue=calculate(split)
    splitValue_label.config(text='Split Value: '+str(splitValue))
    if(splitValue>21):
        splitValue_label.config(text='BUST')
        buttonSp.config(state=DISABLED)
        if(playerValue>21):
            Winner()
            splitWinner()

def splitPlayer():
    print('split')
    split.append(player[1])
    random.shuffle(deck)
    card = deck.pop()
    player.remove(player[1])
    player.append(card)
    card2 = deck.pop()
    split.append(card2)
    global splitValue
    splitValue=calculate(split)
    global playerValue 
    playerValue=calculate(player)
    if(splitValue == 21):
        splitWinner()
    player_label.config(text='Your hand: ' +str(player))
    playerValue_label.config(text='Value: '+str(playerValue))
    split_label.config(text='Your split: ' +str(split))
    splitValue_label.config(text='Split value: '+str(splitValue))
    buttonSp.config(text='Hit Split' ,command=hitSplit)


def Winner():
    buttonH.config(state=DISABLED)
    buttonSp.config(state=DISABLED)
    dealerValue = calculate(dealer)
    playerValue = calculate(player)
    if(playerValue==21 and len(player)==2):
        winner_label.config(text='Blackjack! You Win!')    
    elif(dealerValue==21 and len(dealer)==2):
        winner_label.config(text='Blackjack! You Lose!')        
    elif(playerValue>21):
        winner_label.config(text='You Lose')
    elif(dealerValue>21):
        winner_label.config(text='You Win!')
    elif(playerValue==dealerValue):
        winner_label.config(text='You Draw')
    elif(playerValue>dealerValue):
        winner_label.config(text='You Win!')
    elif(dealerValue>playerValue):
        winner_label.config(text='You Lose')

def splitWinner():
    buttonH.config(state=DISABLED)
    buttonSp.config(state=DISABLED)
    dealerValue = calculate(dealer)
    splitValue = calculate(split)
    if(splitValue==21 and len(split)==2):
        splitWinner_label.config(text='Blackjack! Your split Wins!')    
    elif(dealerValue==21 and len(dealer)==2):
        splitWinner_label.config(text='Blackjack! You Lose!')        
    elif(splitValue>21):
        splitWinner_label.config(text='Your split Loses')
    elif(dealerValue>21):
        splitWinner_label.config(text='Your split Wins!')
    elif(splitValue==dealerValue):
        splitWinner_label.config(text='Your split Draws')
    elif(splitValue>dealerValue):
        splitWinner_label.config(text='You split Wins!')
    elif(dealerValue>splitValue):
        splitWinner_label.config(text='You split Loses')
def reset():
    global deck
    deck = generateDeck()
    global player
    global dealer
    global split
    split.clear()
    player = deal(deck)
    dealer= deal(deck)
    playerValue = calculate(player)
    dealerValue = calculate(dealer)
    if(playerValue==21):
        Winner()
    if(dealerValue==21):
        Winner()
    m.title('BlackJack')
    dealer_label.config(text='dealer has a: '+str(dealer[0]))
    player_label.config(text='Your hand: ' +str(player))
    playerValue_label.config(text='Value: '+str(playerValue))
    buttonSp.config(text='Split',command = splitPlayer,state = DISABLED)
    split_label.config(text='')
    splitValue_label.config(text='')
    winner_label.config(text='')
    splitWinner_label.config(text='')
    if(player[0] == player[1]):
      buttonSp.config(state = ACTIVE)
    buttonH.config(state=ACTIVE)
    buttonS.config(state=ACTIVE)


deck = generateDeck()
#player = deal(deck)
player = [2,2]
split=[]
dealer = deal(deck)
playerValue = calculate(player)
dealerValue = calculate(dealer)
if(playerValue==21):
    Winner()
if(dealerValue==21):
    Winner()
m.title('BlackJack')
messageVar = Message(m, text = 'Lets Play BlackJack!',width=300) 
dealer_label = Label(m,text='dealer has a: '+str(dealer[0]))
player_label =Label(m,text='Your hand: ' +str(player))
playerValue_label=Label(m,text='Value: '+str(playerValue))
split_label=Label(m,text='')
splitValue_label=Label(m,text='')
winner_label=Label(m,text='')
splitWinner_label=Label(m,text='')
messageVar.pack()  
dealer_label.pack()
player_label.pack()
playerValue_label.pack()
split_label.pack()
splitValue_label.pack()
winner_label.pack()
splitWinner_label.pack()
w = Canvas(m, width=400, height=300) 
w.pack() 
button = tkinter.Button(m, text='Restart', width=20, command=reset)
buttonSp = tkinter.Button(m, text='Split', width=20, command = splitPlayer,state = DISABLED)
if(player[0] == player[1]):
    buttonSp.config(state = ACTIVE)
buttonH = tkinter.Button(m, text='Hit', width=20, command=hitPlayer)
buttonS = tkinter.Button(m, text='Stand', width=20, command=standPlayer)
button.pack(side=LEFT) 
buttonSp.pack(side=LEFT)
buttonH.pack(side=LEFT) 
buttonS.pack(side=LEFT) 
m.mainloop()

