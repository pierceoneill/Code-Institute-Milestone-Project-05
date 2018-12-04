from django.test import TestCase
from .models import Babysitter

# Create your tests here.
class BabysitterTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post models
    """
    
    def test_str(self):
        test_name = Babysitter(name='A babysitter')
        self. assertEqual(str(test_name), 'A babysitter')
