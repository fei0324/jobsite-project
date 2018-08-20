# candidate tests.py

from django.test import TestCase
from django.db.utils import IntegrityError

from all_users.models import User
from .models import CandidateProfile

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
		first_candidate_profile = CandidateProfile.objects.create(
			user = self.first_candidate,
			biography = 'I am the first test candidate.'
		)

		self.assertEqual(first_candidate_profile.user.username, 'first_candidate')


	def test_candidate_biography(self):

		first_candidate_profile = CandidateProfile.objects.create(
			user = self.first_candidate,
			biography = 'I am the first test candidate.'
		)

		self.assertEqual(first_candidate_profile.biography, 'I am the first test candidate.')

	def test_candidate_count(self):

		first_candidate_profile = CandidateProfile.objects.create(
			user = self.first_candidate,
			biography = 'I am the first test candidate.'
		)

		second_candidate_profile = CandidateProfile.objects.create(
			user = self.second_candidate,
			biography = 'I am the second test candidate.'
		)

		self.assertEqual(CandidateProfile.objects.count(), 2)

	def test_one_profile_per_user(self):

		with self.assertRaises(IntegrityError):

			first_candidate_profile = CandidateProfile.objects.create(
				user = self.first_candidate,
				biography = 'I am the first test candidate profile.'
			)

			second_candidate_profile = CandidateProfile.objects.create(
				user = self.first_candidate,
				biography = 'I am the second test candidate profile by the same user.'
			)

	def test_employer_cannot_create_candidate_profile(self):

		with self.assertRaises(IntegrityError):

			test_employer = User.objects.create(
				user_type = 'employer',
				username = 'first_employer',
			)

			test_candidate_profile = CandidateProfile.objects.create(
				user = test_employer,
				biography = 'This profile should not be created.'
			)
		

