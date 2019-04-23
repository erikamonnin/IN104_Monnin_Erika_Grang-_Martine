import unittest
import datetime
from class_desk import Deck
from cardclass import Card
from revision import revision_function



my_card_minuscule=Card('test_card_min', 'Waste', 'Carte Test minuscule', 'compost')
my_card_majuscule=Card('test_card_maj', 'Waste', 'Carte Test majuscule', 'COMPOST')
l=[]
l.append(my_card_minuscule)
l.append(my_card_majuscule)


def test_user_result(self):
	given_answer=revision_function(l)
	true_answer1=my_card_minuscule.backside				
	true_answer2=my_card_majuscule.backside	
	self.assertEquals(given_answer,true_answer1)
	self.assertEquals(given_answer,true_answer2)


if __name__ == '__main__':
	unittest.main()
	
	
	
