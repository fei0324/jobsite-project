# all_users admin.py

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from all_users.models import User


# Add an extra field to the UserAdmin page. Since the User model has a set
# field set, we need to append my custom field on top of the fields.

class AllUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = User

class AllUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
	
	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	try:
	# 		User.objects.get(username=username)
	# 	except User.DoesNotExist:
	# 		return username
	# 	raise forms.ValidationError(self.error_messages['duplicate_username'])

class AllUserAdmin(UserAdmin):

	form = AllUserChangeForm
	add_form = AllUserCreationForm

	list_display = UserAdmin.list_display + ('user_type',)
	fieldsets = UserAdmin.fieldsets + (
		(None, {
			'classes': ('wide',),
			'fields': ('user_type',)}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'user_type',)}),
	)
    

admin.site.register(User, AllUserAdmin)