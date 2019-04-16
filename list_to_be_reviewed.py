from cardclass import Card
from class_desk import Deck
import datetime
import review_date




def to_be_reviewed(deck, today):
	due_cards=[]
	for card in deck.cards:
		if not card.review:
			due_date=review_date(card)
			if today.year>due_date.year:
				card.review=True
				due_cards.append(card)
			elif today.year==due_date.year and today.month>due_date.month:
				card.review=True
				due_cards.append(card)
			elif today.year==due_date.year and today.month==due_date.month and today.day>=due_date.day:
				card.review=True
				due_cards.append(card)
		else:
			due_cards.append(card)
	return(due_cards)
