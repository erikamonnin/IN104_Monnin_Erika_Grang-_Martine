import unittest
from Monnin_Waste_class import Waste
from Monnin_Waste_class import OrganicWaste

class KnownValues(unittest.TestCase):
	bois=OrganicWaste('bois', 'biomasse')
	bois.mass=10
	feuilles=OrganicWaste('feuilles', 'biomasse')
	feuilles.mass=1
	epluchures=OrganicWaste('epluchures de carottes', 'legumes')
	epluchures.mass=0.5
	known_values=((bois, 5.0), (feuilles, 0.5), (epluchures, 0.25))	

	def test_timeOfDeg(self):

		for (matiere, time) in self.known_values:
			result=OrganicWaste.timeOfDeg(matiere)
			self.assertEqual(result,time)


if __name__ == '__main__':
	unittest.main()
