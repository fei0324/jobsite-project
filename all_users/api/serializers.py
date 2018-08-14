# all_users/api serializers.py

from rest_framework import serializers

from all_users.models import User

class UserDisplaySerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'user_type',
		]