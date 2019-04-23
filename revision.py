from cardclass import Card
from class_desk import Deck

def revision_function(a_revoir): 
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
	return None
