import unittest
from cardclass import Card
import datetime
from review_date import review_date_funct

testcard=Card('test_card','test_subject','topside','backside')

today = datetime.datetime.now()
one_day=datetime.timedelta(days=1)
tomorrow=today+one_day



class TestReviewDate(unittest.TestCase):
		
	def test_fonction_output(self):	
		'''review_date should give a datetime output'''
		
		self.assertIsInstance(review_date_funct(testcard),type(today))
		
	def test_fonction_works(self):
		'''review_date should aswer tomorrow's date'''
		self.assertEqual(review_date_funct(testcard).day,tomorrow.day)

if __name__ == '__main__':
	unittest.main()
