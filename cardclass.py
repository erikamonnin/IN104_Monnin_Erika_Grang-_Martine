class Card:

	def __init__(self, identifier, subject, topside, backside, position):
		self.identifier=identifier
		self.subject=subject
		self.topside=topside
		self.backside=backside
		self.position=position
		self.review=True  #when the card is created, it needs to view a first time

		self.date=0

		print("Now you can choose between : glass bin, compost, recyclable, bouchons, electronics, piles, ampoules, waste")
