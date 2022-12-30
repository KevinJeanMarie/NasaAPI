from django.test import TestCase
from datetime import datetime
from nasa.models import Nasa

# Create your tests here.


class NasaTestCase(TestCase):

    def test_create_nasa(self):

        nbr_of_nasas_before_add = Nasa.objects.count()
        new_nasa = Nasa()
        new_nasa.title = '2010 PK9'
        new_nasa.due_data = datetime.today()
        new_nasa.kilometers = 0.1160259082
        new_nasa.meters = 116.0259082094
        new_nasa.miles = 0.0720951346
        new_nasa.feet = 380.6624406898

        new_nasa.save()

        nbr_of_nasas_after_add = Nasa.objects.count()

        self.assertTrue(nbr_of_nasas_after_add == nbr_of_nasas_before_add + 1)

#  1 voir combien d'éléments sont présent dans la BDD (nasa)
# 2 ajouter un objet dans la BDD
# 3 valider que le nombre d'objet à été incrémenté de 1
