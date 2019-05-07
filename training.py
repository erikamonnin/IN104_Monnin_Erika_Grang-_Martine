
##########   REVIEW SYSTEM   ###########
# Five bins : 
#	0- reviewed each day
#	1- reviewed all 2 days
#	2- reviewed all 5 days
#	3- reviewed all 7 days
#	4- reviewed all 12 days
########################################



######  USE OF DATETIME   ######
# D= datetime.datetime.now() alors D= AAAA-MM-DD HH:MM:SS.SSSSSS
# D.day= DD     D.hour=HH   etc...
################################








from card_class import Card
from deck_class import Deck
from review_list import to_be_reviewed

import datetime
import random
import time




#######     CHARGEMENT DU PAQUET A REVISER     ########

my_deck=Deck()
filename=input('On which deck do you want to train ?\n') + '.pickle'
my_deck.load_the_deck(filename)




######   CREATION DE LA LISTE DES CARTES A REVISER   ######

today=datetime.datetime.now()
a_revoir=to_be_reviewed(my_deck, today)



########    MELANGER LES CARTES      #########
random.shuffle(a_revoir)



########     ET MAINTENANT REVISONS !    ##########
while len(a_revoir)!=0:
	# Montrer la premiere carte  
	card=a_revoir[0]
	
	# Reception de la reponse 
	print("Vous devez choisir la poubelle adaptee:\n")
	answer=input("%s\n Recyclage ? Compost ? Verre ? Bouchon ? Cendrier ? Electronique ? Piles ? Ordures menageres ? Relais? Ampoules?\n" %(card.topside)).upper()


	###   IF ANSWER CORRECT   ###
	if answer==card.backside.upper():
		print ("Yeah !! Brilliant ! You learn so fast !\n")
		card.position +=1
		time.sleep(3)

	###    IF ANSWER WRONG     ###
	else:
		print ("Owowo... That was not what was expected\n")
		print ("%s was expected\n" %(card.backside))
		card.position = 0
		time.sleep(3)

	###  finalisation   ###
	card.date=today
	card.review=False
	a_revoir.pop(0)

print("Well done !! You have just finished today's session !!\n")



######   SAVING THE DECK  #########

my_deck.save_the_deck(filename)





