import os, re


class Deck:

	def __init__(self, deck_path):
		
		self.showing = 0

		with open (deck_path) as f:
			lines = f.readlines()
		
		self.card_strings = self.split_at_whitespace(lines)
	
		self.cards = []	
		for card_string in self.card_strings:
			self.cards.append(Card(card_string))
	
	def split_at_whitespace(self, lines):
		# this is an array of multiline strings.
		strings = []

		string=''
		for line in lines:
			if re.match("[a-zA-Z0-9.]", line):
				string+=line
			else:
				strings.append(string)
				string=''
		
		if string != '':
			strings.append(string)

		return strings 

	def next_card(self):
		if self.showing > len(self.cards):
			self.showing = 0
		else:
			self.showing+=1


		#make sure that card is showing its top
		self.cards[self.showing].reset()

	def prev_card(self):
		if self.showing == 0:
			self.showing = len(self.cards)-1
		else:
			self.showing-=1

		self.cards[self.showing].reset()

	def get_card(self):
		return self.cards[self.showing]	

class Card:
	
	def __init__(self, lines):
		self.showing = 0
		self.sides = []
		ll = lines.split('\n')
		for line in ll:
			if re.match("[a-zA-Z0-9.]", line): 	
				self.sides.append(line)

	def get_side(self):
		return self.sides[self.showing]

	def flip_right(self):
		if self.showing+1 > len(self.sides)-1:
			self.showing = 0
		else:
			self.showing += 1

		return self.get_side()

	def flip_left(self):
		if self.showing == 0:
			self.showing = len(self.sides)-1
		else:
			self.showing -= 1

		return self.get_side()

	def reset(self):
		self.showing = 0


