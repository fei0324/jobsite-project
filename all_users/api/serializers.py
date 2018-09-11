# all_users/api serializers.py

from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'user_type',
			'date_joined',
		]

class UserCreationSerializer(serializers.Serializer):

	CANDIDATE = 'candidate'
	EMPLOYER = 'employer'

	user_type_choices = (
		(CANDIDATE, 'Candidate'),
		(EMPLOYER, 'Employer'),
	)
		

	username = serializers.CharField(max_length=200)
	email = serializers.EmailField()
	user_type = serializers.ChoiceField(user_type_choices)
	password = serializers.CharField(max_length=200, style={'input_type':'password'}, write_only=True)
	confirm_password = serializers.CharField(max_length=200, style={'input_type':'password'}, write_only=True)

	def validate_username(self, username):
		
		if User.objects.filter(username=username).exists():
			raise serializers.ValidationError("User already exists.")
		return username

	def validate(self, data):

		if not data['password'] or not data['confirm_password']:
			raise serializers.ValidationError("Please enter both password fields.")

		if data['password'] != data['confirm_password']:
			raise serializers.ValidationError("Passwords don't match.")
		return data


	def create(self, validated_data):

		user = User(
			username = validated_data['username'],
			email = validated_data['email'],
			user_type = validated_data['user_type'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user



# class UserCreationSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'first_name',
# 			'last_name',
# 			'user_type',
# 			'password',
# 		]


# 		extra_kwargs = {
# 			'username': {'required': True},
# 			'password': {'required': True, 'write_only': True},
# 		}

# 		# What is the purpose of this method?
# 		def create(self, validated_data):
# 			user = User(
# 				username = validated_data['username'],
# 				first_name = validated_data['first_name'],
# 				last_name = validated_data['last_name'],
# 				user_type = validated_data['user_type'],
# 			)
# 			user.set_password(validated_data['password'])
# 			user.save()
# 			return user