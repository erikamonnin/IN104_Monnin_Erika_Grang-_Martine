class lasagnes:

	def __init__(self, convives, temps_cuisson, couches):
	""" 
		convives: Nombre de convives partageant le plat de lasagne, entier
		couches: nombres de couches que l'on souhaite dans nos lasagnes
		"""
		
		self.convives= convives
		self.tps_cuisson=tps_cuisson
		self.couches=couches
		print('Bon appétit !')


	def getProportions(self):
		return(self.convives)






class bechamel(lasagnes):
	def __init__(self, becha, volume):
		self.becha= {farine : 50, beurre : 50, lait : 60}
		self.volume=volume
	
	def proportions(self, n):
		"""
		n est le nombre par lequel on veut multiplier les proportions pour avoir beaucoup de béchamel
		"""
		I=self.becha
		for i in range(len(I)):
			print("%s :" % I.keys()[i])
			p=n*(I.values()[i])
			print("%s" % p)


	def Temps_preparation_bechamel:
		return(self.cuisson)
		



	
class garniture(lasagnes):
	def __init__(self, vege, ingredients):
	"""     vege : booléen qui dit si le plat doit être végétarien ou non
		ingredients : dictionnaire avec les proportions des ingredients dispo
	"""
		self.vege= vege
		self.ingredients=ingredients

	def lasagnes_vege(self):
		I=self.ingredients
		for ingre in I.keys():
			if ingre!="viande hachée":
				print("%s" % ingre)



	def lasagnes_non_vege(self):
		I=self.ingredients
		for ingre in I.keys():
			print("%s" % ingre)


	def bonne_garniture(self):
		vege=self.vege
		if vege:
			self.lasagnes_vege()
			print("Voici vos lasagnes aux petits légumes !")
		else: 
			self.lasagnes_non_vege()
			print("Voici vos lasagnes du pays !")

	


