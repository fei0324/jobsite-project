# all_users urls.py

from django.urls import path
from .views import (
					UserCreateAPIView,
					UserDetailAPIView,
					UserListAdminAPIView,
					UserRetrieveAdminAPIView,
					)

app_name = 'user-api'

urlpatterns =  [
	path('create/', UserCreateAPIView.as_view(), name='create'),
	path('<int:pk>', UserDetailAPIView.as_view(), name='detail'),
	path('admin-list/', UserListAdminAPIView.as_view(), name='admin-list'),
	path('admin-detail/<int:pk>', UserRetrieveAdminAPIView.as_view(), name='admin-detail'),
]
