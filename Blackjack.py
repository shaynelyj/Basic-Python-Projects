suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def shuffle(self):
        import random
        random.shuffle(self.deck)
        
    def deal(self):
        q = self.deck.pop()
        return q
    
class Hand:
    
    def __init__(self):
        self.card = []
        self.value = 0
        self.ace = 0
        
    def add_card(self,card):
        self.card.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.ace += 1
            
    def adjust_for_aces(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1
            
class Chip:
    
    def __init__(self,total = 100):
        self.total = total
        self.bet = 0
        
    def take_bet(self):
        while True:
            try:
                self.bet = int(input("Bet: "))
            except:
                print ("Please input an integer")
            else:
                if self.bet > self.total:
                    print (f"Insufficient funds! Your current balance is: {self.total}")
                else:
                    break
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet

def show_some(dealer,player):
    print ("\nDealer's hand")
    print ("Hidden card")
    print (dealer.card[1])
    print ("\nPlayer's hand")
    for a in player.card:
        print (a)
        
def show_all(dealer,player):
    print ("\nDealer's hand")
    for q in dealer.card:
        print (q)
    print ("\nPlayer's hand")
    for a in player.card:
        print (a)
        
def hit_or_stand(hand,deck):
    global playing
    
    while playing:
        q = input("Hit or stand").lower()[0]
    
        if q == 'h':
            hand.add_card(deck.deal())
            hand.adjust_for_aces()
        elif q == 's':
            print ("Player stands. Dealer's turn.")
            playing = False
        else:
            continue
        break
        
player_chip = Chip()
playing = True

while True:
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    print ("Welcome to Blackjack!")
    print (f"Your current balance is {player_chip.total}")
    player_chip.take_bet()
    
    while playing:
        show_some(dealer_hand,player_hand)
        hit_or_stand(player_hand,deck)
        
        if player_hand.value > 21:
            show_all(dealer_hand,player_hand)
            print("Player bust!")
            player_chip.lose_bet()
            playing = False
            
    if player_hand.value <= 21:
        while player_hand.value > dealer_hand.value:
            dealer_hand.add_card(deck.deal())
            dealer_hand.adjust_for_aces()
        show_all(dealer_hand,player_hand)
        
        if dealer_hand.value > 21:
            print ("Dealer bust!")
            player_chip.win_bet()
        elif dealer_hand.value > player_hand.value:
            print ("Dealer wins!")
            player_chip.lose_bet()
        elif dealer_hand.value == player_hand.value:
            print ("Tie!")
            
    replay = input("Play again? Y or N: ").lower()
    
    if replay == "y":
        playing = True
        continue
    else:
        print ("Thanks for playing!")
        break
