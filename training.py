
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








from cardclass import Card
from class_desk import Deck
from list_to_be_reviewed import to_be_reviewed
import datetime
import random





#######     CHARGEMENT DU PAQUET A REVISER     ########

my_deck=Deck()
filename=raw_input('On which deck do you want to train ?\n') + '.pickle'
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
	answer=raw_input("%s\n Recyclage ? Compost ? Verre ? Bouchon ? Cendrier ? Electronique ? Piles ? Ordures menageres ?\n" %(card.topside))


	###   IF ANSWER CORRECT   ###
	if answer==card.backside:
		print ("Yeah !! Brilliant ! You learn so fast !\n")
		card.position +=1


	###    IF ANSWER WRONG     ###
	else:
		print ("Owowo... That was not what was expected\n")
		print ("%s\n" %(card.backside))
		card.position = 0

	###  finalisation
	card.date=today
	card.review=False
	a_revoir.pop(0)

print("Well done !! You have just finished today session !!\n")




######   SAVING THE DECK  #########

my_deck.save_the_deck(filename)





