class cards:

	def __init__(self, identifer, subject, topside, backside, position):
		self.identifer=identifer
		self.subject=subject
		self.topside=topside
		self.backside=backside
		self.position=position
		self.review=True  #when the card is created, it needs to view a first time

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
		
		
	
def delete_card(self, new_card):
	self.cards.append(card)

