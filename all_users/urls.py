# all_users urls.py

from django.urls import path
from .views import SignUpView

app_name = 'all_users'

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
]