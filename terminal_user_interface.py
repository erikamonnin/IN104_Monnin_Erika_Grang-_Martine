my_cards=[]
my_deck=Deck(0,my_cards,'Waste')


choice=raw_input('What do you want to do?\n A - add card \n E - edit a card \n D - Delete a card \n S - save the deck \n L - load a deck\n Q - quit \n')
  
	if choice == 'A': 
		id_card=raw_input('Id card?'\n)
		subject=raw_input('Subject?'\n)
		topside=raw_input('Top Side?'\n)
		backside=raw_input('Back Side?'\n)
		my_deck.add_card_to_deck(id_card,subject,topside,backside)
		print("the card as been succesfully added!")

	if choice == 'Q':
		loop_flag=False
    
