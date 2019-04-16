##### CALCUL DE LA DATE DE REVISION ########
#
#Cette fonction permet, a l aide de la date de dernier visionnage d une carte et de sa 
# position, de calculer la prochaine date de visionnage. 
#
############################################


def review_date(card):
	former_date=card.date()
	
	def from_position_to_date(position):
		"""
		Une fonction pour convertir la position en duree
		"""	
		switcher={
			0: datetime.timedelta(days=1),
			1: datetime.timedelta(days=2),
			2: datetime.timedelta(days=5),
			3: datetime.timedelta(days=7),
			4: datetime.timedelta(days=12),
			}
		return(switcher[position])
	
	delta=from_position_to_date(card.position())
	
	new_date=former_date + delta
	return(new_date)
