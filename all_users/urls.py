# all_users urls.py

from django.urls import path
from .views import SignUpView, login_view

app_name = 'all_users'

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	path('login/', login_view, name='login'),
]