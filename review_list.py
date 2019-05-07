from card_class import Card
from deck_class import Deck
import datetime
import review_date




def to_be_reviewed(deck, today):
	due_cards=[]
	for card in deck.cards:
		if not card.review:
			due_date=review_date.review_date_funct(card)
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
