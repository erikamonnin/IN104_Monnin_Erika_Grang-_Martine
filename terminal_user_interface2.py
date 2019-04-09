my_cards=[]
my_deck=Deck(0,my_cards,'Waste')


choice=raw_input('What do you want to do?\n A - add card \n E - edit a card \n D - Delete a card \n S - save the deck \n L - load a deck\n Q - quit \n')
  
	if choice == 'A': 
		id_card=raw_input('Id card?\n')
		subject=raw_input('Subject?\n')
		topside=raw_input('Top Side?\n')
		backside=raw_input('Back Side?\n')
		my_deck.add_card_to_deck(id_card,subject,topside,backside)
		print("the card as been succesfully added!")
		
	if choice == 'E': 
		id_card=raw_input('Id card?\n')
		attribute=raw_input('Edited attribute?\n')
		change=raw_input('Change?\n')
		my_deck.edit_card(id_card,attribute,change)
		print("the card as been succesfully edited!")
			
	if choice == 'D':
		id_card=raw_input('Id_card\n')
		my_deck.delete_card_from_deck(id_card)
	
	if choice == 'L':
		filename=raw_input('Nom du fichier\n')
		my_deck.load_the_deck(filename)

	if choice == 'S':
		filename=raw_input('Nom du fichier\n')
		my_deck.save_the_deck(filename)

	if choice == 'Q':
		quit()
    
