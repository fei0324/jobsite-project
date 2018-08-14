# all_users models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	CANDIDATE = 'candidate'
	EMPLOYER = 'employer'

	user_type_choices = (
		(CANDIDATE, 'Candidate'),
		(EMPLOYER, 'Employer'),
	)

	user_type = models.CharField(
		max_length = 50,
		choices = user_type_choices,
		default = CANDIDATE,
	)

	@property
	def is_candidate(self):
		if self.user_type == 'candidate':
			return True
		return False

	@property
	def is_employer(self):
		if self.user_type == 'employer':
			return True
		return False
	
	