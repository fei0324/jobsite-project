# candidate tests.py

from django.test import TestCase
from django.db.utils import IntegrityError
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from django.contrib.auth import get_user_model
from .models import CandidateProfile

User = get_user_model()

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

	# def test_employer_cannot_create_candidate_profile(self):

	# 	with self.assertRaises(IntegrityError):

	# 		test_employer = User.objects.create(
	# 			user_type = 'employer',
	# 			username = 'first_employer',
	# 		)

	# 		test_candidate_profile = CandidateProfile.objects.create(
	# 			user = test_employer,
	# 			biography = 'This profile should not be created.'
	# 		)
		
class CandidateProfileTests(APITestCase):

	def setUp(self):

		self.employer = User.objects.create(
			user_type = 'employer',
			username = 'first_employer',
		)
		self.candidate = User.objects.create(
			user_type = 'candidate',
			username = 'first_candidate',
		)

	def test_employer_cannot_create_candidate_profile(self):

		self.client.force_authenticate(self.employer)
		endpoint = reverse('candidate-api:create')
		resp = self.client.post(endpoint, {'biography':'I am an employer'})
		self.assertEqual(resp.status_code, 403)

	def test_candidate_create_profile(self):

		self.client.force_authenticate(self.candidate)
		endpoint = reverse('candidate-api:create')
		resp = self.client.post(endpoint, {'biography': 'Hi I am the first candidate.'})
		self.assertEqual(resp.status_code, 201)

	def test_nonowner_cannot_edit(self):

		self.client.force_authenticate(self.employer)
		endpoint = reverse('candidate-api:detail', kwargs={'pk': 1})
		resp = self.client.put(endpoint, {'biography': 'I am not the owner of the post'})
		self.assertEqual(resp.status_code, 404)

	def test_owner_can_edit(self):

		self.client.force_authenticate(self.employer)
		endpoint = reverse('candidate-api:detail', kwargs={'pk':1})
		print(endpoint)
		resp = self.client.put(endpoint, {'biography': 'I am the owner I can edit.'})
		self.assertEqual(resp.status_code, 202)


