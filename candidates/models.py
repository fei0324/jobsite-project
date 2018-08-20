# candidates models.py

from django.db import models
from django.urls import reverse

from all_users.models import User

class CandidateProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	biography = models.TextField()
	LinkedIn = models.URLField(blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('candidate-api:reverse')
