# candidates models.py

from django.db import models

from all_users.models import User

class CandidateProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	biography = models.TextField()
	LinkedIn = models.URLField(blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.user.username

