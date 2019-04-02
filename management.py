import pickle

class cards:

	def __init__(self, identifer, subject, topside, backside, position):
		self.identifer=identifer   #string du type card_dechet
		self.subject=subject
		self.topside=topside
		self.backside=backside
		self.position=position
		self.review=True  #when the card is created, it needs to be viewed a first time

		self.date=0

		print("Now you can choose between : glass bin, compost, recyclable, bouchons, electronics, piles, ampoules, waste")


class deck:
	def __init__(self,number,cards):
	"""
	number = the number of cards in the deck
	cards = a list containing all the cards added
	"""
		self.number = number
		self.cards = cards
		

	
	
	
def add_card_to_deck(card,deck):
	deck.cards.append(card)
	deck.number += 1
	return 



def edit_topside(deck, identity, new_topside):
	for card in deck.cards:
		if card.identifer==identity:
			card.topside= new_topside
	return




def edit_backside(deck, identity, new_backside):
	for card in deck.cards:
		if card.identifer==identity:
			card.backside= new_backside
	return



def delete_card_from_deck(obsolete_card, deck):
	deck.cards.pop(obsolete_card.position)
	deck.number -=1
	return



def save_the_deck(deck, filename):
	#filename est une chaine de caractère entre '' !!!
	with_open(filename,_'wb')_as_f:
		pickle.dump(deck,_f)
		
		
