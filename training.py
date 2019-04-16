
##########   REVIEW SYSTEM   ###########
# Five bins : 
#	0- reviewed each day
#	1- reviewed all 2 days
#	2- reviewed all 5 days
#	3- reviewed all 7 days
#	4- reviewed all 12 days
########################################


from cardclass import Card
from class_desk import Deck
import datetime


#######     CHARGEMENT DU PAQUET A REVISER     ########

my_deck=Deck()
filename=raw_input('On which deck do you want to train ?\n') + '.pickle'
my_deck.load_the_deck(filename)





######  USE OF DATETIME   ######
# D= datetime.datetime.now() alors D= AAAA-MM-DD HH:MM:SS.SSSSSS
# D.day= DD     D.hour=HH   etc...
################################





######   CREATION DE LA LISTE DES CARTES A REVISER   ######

today=datetime.datetime.now()
for card in my_deck.cards:
	if not card.review:
		due_date=fonction_Erika()
		if today.year>due_date.year:
			card.review=True
		elif today.year=due_date.year and today.month>due_date.month:
			card.review=True
		elif today.year=due_date.year and today.month=due_date.month and today.day>=due_date.day:
			card.review=True






########    MELANGER LES CARTES      #########






########     MONTRER LA CARTE SUIVANTE     ##########






#######       IF ANSWER CORRECT   ########






#######       IF ANSWER WRONG     ########






######   SAVING THE DECK  #########

my_deck.save_the_deck(filename)





