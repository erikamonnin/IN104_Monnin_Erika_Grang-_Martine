class Waste:
	def __init__(self, name, mass, timeOfUse, timeOfDegradation):
		"""
		name: name of the waste
		mass: mass of the waste
		timeOfUse: time (in months) of how longt the waste has been used
		timeOfDegradation: time (in years) of how long it takes for the waste to desintegrate in the nature 
		"""

		self.name = name
		self.mass = mass
		self.timeOfUse = timeOfUse
		self.timeOfDegradation = timeOfDegradation
		print("Our waste is %s." %(name))

class OrganicWaste(Waste):
	def __init__(self,composter,origin):
		"""
		origin: gives the type of organic waste (e.g.: vegeteble,fruit,flowers)
		"""
		print "I am an organic waste"
		self.composter = composter
		self.timeOfDegradation = 0.5 
		self.origin = origin

	def useComposter(self):
		print("I am an organic waste: throw me in a composter!")




	def timeOfDeg(self):
		time=self.timeOfDegradation*self.mass
		print("I take %f years to desintegrate." %(time))
		return(time)
		




class GalssWaste(Waste):
	def __init__(self,glassBean,funFact):
		print "I am a glass waste"
		self.glassBean = glassBean 
		self.funFact = funFact 

	def timeOfDeg(self):
		print("I take %f years to desintegrate. You should check my fun fact!" %(self.degradation))

	def funFact(self):
		print("Did you know? I am infinitely recyclable!")

	def glassBean(self):
		print("throw me in a glass bean!")
