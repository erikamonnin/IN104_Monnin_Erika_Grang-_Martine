import unittest
import datetime
from list_to_be_reviewed import to_be_reviewed
from class_desk import Deck
from cardclass import Card

class TestARevoir(unittest.TestCase):
	my_deck=Deck()

	card1=Card('card_test1', 'waste', 'bouchon', 'bouchon')
	card1.position=1
	card1.review=False
	card1.date=datetime.date(2019,04,15)

	card2=Card('card_test2', 'waste', 'bouchon', 'bouchon')
	card2.position=0
	card2.review=False
	card2.date=datetime.date(2019,04,15)

	card3=Card('card_test3', 'waste', 'bouchon', 'bouchon')
	card3.position=4
	card3.review=False
	card1.date=datetime.date(2019,04,01)
	
	my_deck.cards=[card1,card2,card3]
	today=datetime.date(2019,04,16)

	def test_fonction(self):
		result=to_be_reviewed(self.my_deck, self.today)
		self.assertEqual(result, [card2,card3])

if __name__ == '__main__':
	unittest.main()
