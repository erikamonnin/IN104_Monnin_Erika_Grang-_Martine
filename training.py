
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
filename=raw_input('On which deck do you want to train ?\n') + '.pickle'
my_deck.load_the_deck(filename)




######   CREATION DE LA LISTE DES CARTES A REVISER   ######

today=datetime.datetime.now()
a_revoir=to_be_reviewed(my_deck, today)



########    MELANGER LES CARTES      #########
random.shuffle(a_revoir)



########     ET MAINTENANT REVISONS !    ##########
succes = 0
echecs = 0
L= 0
print("\n       Courage, seulement %s cartes a reviser aujourd'hui  :) \n" %(len(a_revoir)))
time.sleep(0.5)

while len(a_revoir)!=0:
	# Montrer la premiere carte  
	card=a_revoir[0]
	L= L+1

	# Reception de la reponse 

	answer=raw_input("\n O- Ordures menageres \n R- Recyclage \n C- Compost \n V- Verre \n B- Bouchon \n M- Cendrier \n E- Electronique \n P- Piles \n T- Relais \n A- Ampoules \n Q- Quitter \n  \n Quelle est la poubelle adaptee a ce dechet : %s ? \n \n" %(card.topside))
	answer=answer.upper()

	
	if answer=='Q':
		my_deck.save_the_deck(filename)
		print ("Don't forget to come back latter to finish your session ;-)\n")
		time.sleep(1.5)
		quit()

	###   IF ANSWER CORRECT   ###
	if answer==card.backside.upper():
		print ("Yeah !! Brilliant ! You learn so fast !\n")
		card.position +=1
		succes = succes +1
		

	###    IF ANSWER WRONG     ###
	else:
		print ("Owowo... That was not what was expected\n")
		print ("%s was expected\n" %(card.backside))
		card.position = 0
		echecs = echecs +1
		

	###  finalisation   ###
	card.date=today
	card.review=False
	a_revoir.pop(0)
	ps = int((float(succes)/L)*100)
	pe = int((float(echecs)/L)*100)
	print ("Succes : %s %% \nEchecs : %s %%\n \n" %(ps, pe))
	time.sleep(0.5)
	print("Deja %s cartes revisees ! \nAllez, plus que %s cartes !\n" %(L,len(a_revoir)))
	time.sleep(1.5)
	

print("Well done !! You have just finished today's session !! See you tomorrow !!\n")



######   SAVING THE DECK  #########

my_deck.save_the_deck(filename)





