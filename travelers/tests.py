from django.contrib.auth.models import User
from .models import Traveler
from django.test import TestCase


class UserTravelerCountTest(TestCase):
    # make sure that the user is always extended with the traveler model
    def test_user_traveler_count(self):
        user_count = User.objects.count()
        traveler_count = Traveler.objects.count()
        self.assertEqual(user_count, traveler_count)
