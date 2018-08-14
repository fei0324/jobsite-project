from django.test import TestCase

from .models import User

# Create your tests here.

class AllUserModelTest(TestCase):

	def setUp(self):
		self.candidate = User.objects.create(
			user_type = 'candidate',
			username = 'first_candidate',
		)
		self.employer = User.objects.create(
			user_type = 'employer',
			username = 'first_employer',
		)

	def test_candidate_property(self):

		candidate_user = self.candidate
		self.assertEqual(candidate_user.is_candidate, True)
		self.assertEqual(candidate_user.is_employer, False)

	def test_employer_property(self):

		employer_user = self.employer
		self.assertEqual(employer_user.is_candidate, False)
		self.assertEqual(employer_user.is_employer, True)