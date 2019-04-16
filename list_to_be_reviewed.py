from cardclass import Card
from class_desk import Deck
import datetime
import review_date

def to_be_reviewed(deck):
	
	today=datetime.datetime.now()
	for card in my_deck.cards:
		if not card.review:
			due_date=review_date(card)
			if today.year>due_date.year:
				card.review=True
			elif today.year=due_date.year and today.month>due_date.month:
				card.review=True
			elif today.year=due_date.year and today.month=due_date.month and today.day>=due_date.day:
				card.review=True
	return
