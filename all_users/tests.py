from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate


from django.contrib.auth import get_user_model


User = get_user_model()

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

class AllUserTests(APITestCase):

	def setUp(self):

		super().setUp()

		self.first_candidate = User.objects.create(
			user_type = 'candidate',
			username = 'first_candidate',
		)
		self.second_candidate = User.objects.create(
			user_type = 'candidate',
			username = 'second_candidate',
		)
		self.client.force_authenticate(self.second_candidate)

	def test_nonowner_cannot_view_user_detail(self):

		# This test is not working as expected
		endpoint = reverse('user-api:detail', kwargs={'pk':self.first_candidate.pk})
		print(endpoint)
		resp = self.client.get(endpoint)
		self.assertEqual(resp.status_code, 403)

class AllUserAdminViewTests(APITestCase):

	def setUp(self):

		super().setUp()

		self.candidate = User.objects.create(
			user_type = 'candidate',
			username = 'first_candidate',
		)
		self.client.force_authenticate(self.candidate)

	def test_users_cannot_view_user_list(self):

		endpoint = reverse('user-api:admin-list')
		resp = self.client.get(endpoint)
		self.assertEqual(resp.status_code, 403)
