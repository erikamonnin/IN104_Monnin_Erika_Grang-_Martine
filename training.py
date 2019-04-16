
##########   REVIEW SYSTEM   ###########
# Five bins : 
#	0- reviewed each day
#	1- reviewed all 2 days
#	2- reviewed all 5 days
#	3- reviewed all 7 days
#	4- reviewed all 20 days
########################################


from cardclass import Card
from class_desk import Deck
import datetime


##### CHARGEMENT DU PAQUET A REVISER   ######

my_deck=Deck()
filename=raw_input('On which deck do you want to train ?\n') + '.pickle'
my_deck.load_the_deck(filename)





######  USE OF DATETIME   ######
# D= datetime.datetime.now() alors D= AAAA-MM-DD HH:MM:SS.SSSSSS
# D.day= DD     D.hour=HH   etc...
################################



today=datetime.datetime.now()
for card in my_deck.cards:
	if card.date.day != today.day
		card.review=True



