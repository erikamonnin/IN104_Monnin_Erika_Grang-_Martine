from cardclass import Card
from class_desk import Deck

my_deck=Deck()
flag=True 



choix=raw_input('Do you want to load a deck or not ?\n Y or N')
choix=choix.upper()
if choix == 'Y':
	filename=raw_input('Nom du fichier\n') + '.pickle'
	my_deck.load_the_deck(filename)




while flag:

	choice=raw_input('What do you want to do?\n A - add card \n E - edit a card \n D - Delete a card \n S - save the deck \n L - load a deck\n Q - quit \n')
	choice=choice.upper()
  
	if choice == 'A': 
		id_card=raw_input('Id card?\n')
		for c in my_deck.cards:
			if c.identifier==id_card:
				print("Cette carte existe deja!")
				break
		
		topside=raw_input('Top Side?\n')
		backside=raw_input('Back Side?\n')
		my_deck.add_card_to_deck(id_card,"Waste",topside,backside)
		msg = "You have " + str(len(my_deck.cards)) + " cards"
		print msg
		print("the card as been succesfully added!")
		

	if choice == 'E': 
		id_card=raw_input('Id card?\n')
		attribute=raw_input('Edited attribute?\n')
		if attribute=='identifier' or attribute=='subject' or attribute=='topside' or attribute=='backside':
			change=raw_input('Change?\n')
			my_deck.edit_card(id_card,attribute,change)
			print("the card as been succesfully edited!")
		elif attribute=='review' or attribute=='position':
			change=input('Change?\n')
			my_deck.edit_card(id_card,attribute,change)
			print("the card as been succesfully edited!")
		else :
			print("Attention ! Les attributs possibles sont : identifier, subject, topside, backside, review, position")
		

	if choice == 'D':
		id_card=raw_input('Id_card\n')
		my_deck.delete_card_from_deck(id_card)
	

	if choice == 'L':
		filename=raw_input('Nom du fichier\n') + '.pickle'
		my_deck.load_the_deck(filename)


	if choice == 'S':
		filename=raw_input('Nom du fichier\n') + '.pickle'
		my_deck.save_the_deck(filename)
		

	if choice == 'Q':
		flag=False



choix=raw_input('Have you saved the deck ? Y or N \n')
choix=choix.upper()
if choix== 'N':
	filename=raw_input('Nom du fichier\n') + '.pickle'
	my_deck.save_the_deck(filename)



    
