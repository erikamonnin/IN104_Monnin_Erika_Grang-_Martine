import pickle
from cardclass import Card

class Deck:
	def __init__(self,subject="Waste"):
		"""
		cards = a list containing all the cards added
		"""
		self.cards = []
		self.subject = subject
	

	def add_card_to_deck(self,id_card,subject,top_side,back_side):
		"""
		this program creates a new card (attributes are the inputs) and add it to the current deck
		"""
		new_card = Card(id_card, subject, top_side, back_side)
		self.cards.append(new_card)
		return 
	
	def delete_card_from_deck(self,obsolete_id_card):
		"""
		this program deletes a card (thanks to its id) from the current deck
		"""
		i=0
		for x in self.cards:
			if x.identifier==obsolete_id_card:
				self.cards.pop(i)
			i+=1
		return
	

	def edit_card(self,card_id,edited_attribute, change):
		"""
		this program edits one attribute of a card (the card is find in the deck thanks to its id)
		"""
		for x in self.cards:
			if x.identifier==card_id :		
				x[edited_attribute] = change
		return



	def save_the_deck(self, filename):
		"""
		filename est une chaine de caracteres entre simples guillemets !!!
		"""
		with open(filename, 'wb') as f:
			pickle.dump(self.cards, f)
		return	



	def load_the_deck(self, filename):
		with open(filename, 'rb') as f:
			self.cards=pickle.load(f)
		return(self)

