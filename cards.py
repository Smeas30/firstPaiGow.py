import random
import itertools
# from player import player1

def main():
	class Card(object):
		def __init__(self,value,suit):
			self.value = value
			self.suit = suit
	# __repr__ allows us to represent a card object on a terminal
		def __repr__(self):
			value_name = ""
			suit_name = ""
			#if self.value equal 0, then value.name equal two
			if self.value == 0:
				value_name = "2"
			if self.value == 1:
				value_name = "3"
			if self.value == 2:
				value_name = "4"
			if self.value == 3:
				value_name = "5"
			if self.value == 4:
				value_name = "6"
			if self.value == 5:
				value_name = "7"
			if self.value == 6:
				value_name = "8"
			if self.value == 7:
				value_name = "9"
			if self.value == 8:
				value_name = "10"
			if self.value == 9:
				value_name = "J"
			if self.value == 10:
				value_name = "Q"
			if self.value == 11:
				value_name = "K"
			if self.value == 12:
				value_name = "A"
			if self.suit == 0:
				suit_name = "D"
			if self.suit == 1:
				suit_name = "C"
			if self.suit == 2:
				suit_name = "H"
			if self.suit == 3:
				suit_name = "S"
			# to return another value use '+'
			return value_name + " " + suit_name

	class Player(object):
		def __init__(self):
			self.cards = []
			self.score = 0
		

	# we are appending self because self is the deck that is the list
	# this mean it goes through a value and goes through all the suit for that value and put that in self as a card and it continues. the result would be 4*13 cards which is 52
	class Deck(list):
		def __init__(self):
			super().__init__()
			# there are 4 suits in a deck, range value is 0-3
			suits = list(range(4))
			# create a list of numbers 0-12
			values = list(range(13))
			# this will take the variable 'j' from suits (h,d,s,c)
			for suit in suits:
			# this will take a number from the range of 0-12
				for value in values:
					#this will take the suit(j) and value(i) and combine them ie. 12 3, order depends on placement
					self.append(Card(value, suit))

			# [[self.append(Card(i, j)) for j in suits] for i in values]
		
		def shuffle(self):
		#this will make the deck print in random order instead of lowest to highest
			random.shuffle(self)

# this will pop the card off of the deck, starting at index 0, it pops the card and take it out of the list
#location will be the player
		def deal(self, location):
			# location.cards.append(self.pop(0))
			for _ in range(0,13,1):
				location.cards.append(self.pop(0))

#create AI to play against

	class Robot(object):
		def __init__(self):
			self.cards = []
			self.score = 0
			self.top_three = []
			self.mid_five = []
			self.last_five = []

		# def ai_gameplay(self):
		# 	top_play = 

		# def ai_play(self):
		# 	deck.deal(robot)
		# 	if robot.cards == 
			

		def eval_hand(self):
			# Return ranking followed by tie-break information.
			# 8. Straight Flush
			# 7. Four of a Kind
			# 6. Full House
			# 5. Flush
			# 4. Straight
			# 3. Three of a Kind
			# 2. Two pair
			# 1. One pair
			# 0. High card

			values = sorted([c[0] for c in hand], reverse=True)
			suits = [c[1] for c in hand]
			straight = (values == list(range(values[0], values[0]-5, -1))
						or values == [14, 5, 4, 3, 2])
			flush = all(s == suits[0] for s in suits)

			if straight and flush: return 8, values[1]
			if flush: return 5, values
			if straight: return 4, values[1]

			trips = []
			pairs = []
			for v, group in itertools.groupby(values):
				count = sum(1 for _ in group)
				if count == 4: return 7, v, values
				elif count == 3: trips.append(v)
				elif count == 2: pairs.append(v)

			if trips: return (6 if pairs else 3), trips, pairs, values
			return len(pairs), pairs, values

# function for placing first 3 cards
		# def card_setup(self):
		# 	deck.deal(player1)
		# 	while True:
		# 		print("You hand", (player1.cards))
		# 		first_hand = input("Set first highest 3 cards: ")
		# 		second_hand = input("Set second highest 5 cards: ")
		# 		third_hand = input("Set highest hand: " )
			
		# 		print("\nFirst 3 card set: ", first_hand)
		# 		print("\nSecond 5 card set: ", second_hand)
		# 		print("\nFinal 5 card set: ", third_hand )
		# 		input_answer = input("do you want to play this hand? \nYes/No: ")
		# 		if input_answer == "Yes":
		# 			break
		# 		elif input_answer == "No":
		# 			continue



# # scoring against AI
# 	class Score(object):
# 		def __init_(self,first_hand,second_hand,third_hand):
# 			self.first_hand = first_hand
# 			self.second_hand = second_hand
# 			self.third_hand = third_hand

# 		def first_round(self):
			
# sort card function



						
	# create an instance of a standard deck
	# player1 = Player()
	robot = Robot()
	deck = Deck()
	#this will call method to shuffle the deck
	deck.shuffle()
	# deck.deal(player1)
	# print(player1.cards)
	# print(deck)
	# deck.sort_card()
	# deck.card_setup()
	# print(player1.cards)
	# deck.deal(robot)
	# robot.ai_play()
	# robot.eval_hand()
	# print("player cards:\n", player1.cards)
	print("Robots card: \n", robot.cards)
	print(len(deck))
	print(Card.value)	

if __name__ == "__main__":
	main()