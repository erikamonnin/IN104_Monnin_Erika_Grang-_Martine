import pickle

class Card:

	def __init__(self, identifer, subject, topside, backside, position):
		self.identifer=identifer   #string du type card_dechet
		self.subject=subject
		self.topside=topside
		self.backside=backside
		self.position=position
		self.review=True  #when the card is created, it needs to be viewed a first time

		self.date=0

		print("Now you can choose between : glass bin, compost, recyclable, bouchons, electronics, piles, ampoules, waste")


class Deck:
	def __init__(self,number,cards,subject):
	"""
	number = the number of cards in the deck
	cards = a list containing all the cards added
	"""
		self.number = number
		self.cards = cards
		self.subject = subject
		
		
		
	def add_card_to_deck(self,id_card,subject,top_side,back_side):
	"""
	this program creates a new card (attributes are the inputs) and add it to the current deck
	"""
		new_card = Card(id_card, subject, top_side, back_side)
		self.cards.append(card)
		self.number += 1
		return 
	
	def delete_card_from_deck(self,obsolete_id_card):
	"""
	this program deletes a card (thanks to its id) from the current deck
	"""
		for x in self.cards:
			if x.identifier==obsolete_id_card:
				self.cards.pop(x.position)
				self.number -=1
		return
	

	def edit_card(self,card_id,edited_attribute, change):
	"""
	this program edits one attribute of a card (the card is find in the deck thanks to its id)
	"""
		for x in self.cards:
			if x.identifier==card_id :		
				x.edited_attribute = change
		return



def save_the_deck(deck, filename):
	#filename est une chaine de caractère entre '' !!!
	with_open(filename,_'wb')_as_f:
		pickle.dump(deck,_f)
		
		
