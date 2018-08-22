# all_users urls.py

from django.urls import path
from .views import UserCreateAPIView, UserDetailView

app_name = 'user-api'

urlpatterns =  [
	path('create/', UserCreateAPIView.as_view(), name='create'),
	path('<int:pk>', UserDetailView.as_view(), name='detail'),
]
