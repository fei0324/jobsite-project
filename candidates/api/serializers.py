# candidates/api serializers.py

from rest_framework import serializers

from all_users.models import User
from candidates.models import CandidateProfile
from all_users.api.serializers import UserDisplaySerializer

class CandidateProfileSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)

	class Meta:
		model = CandidateProfile
		fields = [
			'user',
			'biography',
			'LinkedIn',
			'website',
		]