import datetime

class Card:

	def __init__(self, identifier, subject, topside, backside):

		self.identifier=identifier
		self.subject=subject
		self.topside=topside
		self.backside=backside
		self.position=0   # numéro de la bin dans laquelle se trouve la carte
		self.review=True  # when the card is created, it needs to view a first time

		self.date=datetime.datetime.now()  # prochaine date

