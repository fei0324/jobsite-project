# candidate tests.py

from django.test import TestCase

from all_users.models import User
from .models import Candidate_Profile

class CandidateModelTest(TestCase):

	def setUp(self):
		self.first_candidate = User.objects.create(
			user_type = 'candidate',
			username = 'first_candidate',
		)
		self.second_candidate = User.objects.create(
			user_type = 'candidate',
			username = 'second_candidate',
		)


	def test_candidate_username(self):
		first_candidate_profile = Candidate_Profile.objects.create(
			user = self.first_candidate,
			biography = 'I am the first test candidate.'
		)

		self.assertEqual(first_candidate_profile.user.username, 'first_candidate')


	def test_candidate_biography(self):

		first_candidate_profile = Candidate_Profile.objects.create(
			user = self.first_candidate,
			biography = 'I am the first test candidate.'
		)

		self.assertEqual(first_candidate_profile.biography, 'I am the first test candidate.')

	def test_candidate_count(self):

		first_candidate_profile = Candidate_Profile.objects.create(
			user = self.first_candidate,
			biography = 'I am the first test candidate.'
		)

		second_candidate_profile = Candidate_Profile.objects.create(
			user = self.second_candidate,
			biography = 'I am the second test candidate.'
		)

		self.assertEqual(Candidate_Profile.objects.count(), 2)
