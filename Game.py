import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'King':10,'Queen':10,'Jack':10,'Ace':11}

playing = True

class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
	def value(self):
		val = values[self.rank]
	def __str__(self):
		return self.rank+ " of"+ self.suit

class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n ' + card.__str__()
		return "The deck has : "+ deck_comp
	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]

		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		
		##### Tricky code line...using int as boolean where 0 = FALSE #####
		while self.value > 21 and self.aces:
			self.value -=10
			self.aces -= 1

class Chips:
	def __init__(self,total = 100):
		self.total = total 
		self.bet = 0

	def win_bet(self):
		self.total = self.total + self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(Chips):
	
	while True:

		try:
			Chips.bet = int(input("Input your bet amount: "))
		except TypeError:
			print("Not an integer!")
			continue
		except:
			print("Not enough funds!")
			continue
		else:
			if Chips.bet > Chips.total :
				print("Not enough funds!")
				continue
			else:
				print("Your bet is successfuly placed!")
			break

	

def hit(deck,hand):

	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing

	while True:
		x = input('Hit or Stand? Enter h or s ')
		if x[0].lower() =='h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print("Player stands ; Dealer's Turn")
			playing = False  

		else:
			print("Sorry, did not understand that, please enter only h or s")
			continue
		break

def player_busts(player,dealer,chips):
	print("BUST PLAYER")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("PLAYER WINS")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("PLAYER WINS! DEALER BUSTED!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("PLAYER BUSTED! DEALER WINS!")
	chips.lose_bet()

def push(player,dealer):
	print('Dealer and Player tie! PUSH')

def show_some(player,dealer):
	print("Dealer's cards: ")
	print("First is hidden!")
	print(dealer.cards[1])
	print('\n')
	print("Player's cards: ")
	for i in player.cards:
		print(i)
def show_all(player,dealer):
	print("Dealer's Cards :")
	for i in dealer.cards:
		print(i)
	print('\n')
	print("Player's Cards :")
	for k in player.cards:
		print(k)



################################
###############################
# GGAAMMEE###################

while True:

	print("WELCOME TO PRADO'S BLACKJACK!!!")

	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())


	player_chips = Chips()

	take_bet(player_chips)

	show_some(player_hand,dealer_hand)

	while playing:

		hit_or_stand(deck,player_hand)

		show_some(player_hand,dealer_hand)

		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)

		break
	if player_hand.value <=21:

		while dealer_hand.value < player_hand.value:
			hit(deck,dealer_hand)

		show_all(player_hand,dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)
	print('\n Player total chips at : {}'.format(player_chips.total))
	
	new_game = input("Wanna play again? answer via y or n")

	if new_game[0].lower() == 'y':
		continue
	elif new_game[0].lower() == 'n':
		break
	else:
		print("Not a viable answer")