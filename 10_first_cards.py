import management

my_cards=[]
my_deck=Deck(0,my_cards,'Waste')

my_deck.add_card_to_deck('card_bouteille_eau','Waste','Bouteille d'eau','Recyclage')
my_deck.add_card_to_deck('card_patate','Waste','Pomme de terre', 'Compost')
my_deck.add_card_to_deck('card_bouteille_vin','Waste','Bouteille de Vin', 'Verre')
my_deck.add_card_to_deck('card_bouchon','Waste','Bouchon de bouteille', 'Bouchon')
my_deck.add_card_to_deck('card_epluchure','Waste','Epluchures de carottes', 'Compost')
my_deck.add_card_to_deck('card_rognures','Waste','Rognures d'ongles', 'Ordures ménagères')
my_deck.add_card_to_deck('card_viande','Waste','Os de poulet', 'Ordures ménagères')
my_deck.add_card_to_deck('card_megot','Waste','Mégot de cigarette', 'Cendrier')
my_deck.add_card_to_deck('card_paquet','Waste','Paquet de pâtes vide', 'Recyclage')


choice=raw_input('What do you want to do?\n A - add card \n E - edit a card \n D - Delete a card \n S - save the deck \n L - load a deck\n Q - quit \n')
  if choice==A
    id_card=raw_input('Id card?'\n)
    subject=raw_input('Subject?'\n)
    topside=raw_input('Top Side?'\n)
    backside=raw_input('Back Side?'\n)
    my_deck.add_card_to_deck(id_card,subject,topside,backside)
    print("the card as been succesfully added!")
  if choice==E
  
