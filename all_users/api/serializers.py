# all_users/api serializers.py

from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'user_type',
		]

class UserCreationSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'user_type',
			'password',
		]


		extra_kwargs = {
			'username': {'required': True},
			'password': {'required': True, 'write_only': True},
		}

		# What is the purpose of this method?
		def create(self, validated_data):
			user = User(
				username = validated_data['username'],
				first_name = validated_data['first_name'],
				last_name = validated_data['last_name'],
				user_type = validated_data['user_type'],
			)
			user.set_password(validated_data['password'])
			user.save()
			return user